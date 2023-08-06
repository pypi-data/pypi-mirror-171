import json
import os
import subprocess as sp
import traceback
from pathlib import Path
import sys

from batchx import bx

from .CTE import DEFAULT_MEMORY_MB, DEFAULT_VCPUS
from .debug import debug_print
from .error import (
    handle_called_process_error,
    handle_unknown_exception,
    handle_value_error,
)
from .io import save_json

from functools import partial


def check_for_custom_exception(
    stderr: str,
    custom_exceptions: list | None = None,
):
    if custom_exceptions is None:
        custom_exceptions = []

    for custom_exception in custom_exceptions:
        if custom_exception.is_applicable(stderr):
            debug_print(
                "{id} Stderr".format(id=custom_exception.IDENTIFIER), stderr, long=False
            )
            sys.exit(custom_exception.BX_ERROR_CODE)
        else:
            pass
    return


def check_for_acceptable_exit_code(
    identifier: str = "",
    error_message: str | None = None,
    exit_code: int | None = None,
    acceptable_exit_codes: tuple[int, ...] = (0,),
    verbose: bool = True,
    raise_error: bool = False,
):
    debug_print(
        "{} Exit code".format(identifier),
        exit_code,
        verbose=verbose,
        long=False,
    )

    if exit_code not in acceptable_exit_codes:
        error_message = """
        Exit code {c} not in acceptable exit codes {ac}.
        StdErr:
            {error_msg}
        """.format(
            error_msg=error_message,
            c=exit_code,
            ac=acceptable_exit_codes,
        )
        if raise_error:
            raise ValueError(error_message) from None
        else:
            return exit_code
    else:
        return exit_code


def get_bx_request(
    job_service,
    identifier: str,
    tool: str,
    inputs: dict,
    environment: str | None = None,
    vcpus=DEFAULT_VCPUS,
    memory_mb=DEFAULT_MEMORY_MB,
    timeout_s: int = 15 * 60,
    verbose: bool = True,
):
    if environment is None:
        environment = os.environ["BATCHX_ENV"]

    request = job_service.SubmitRequest(
        environment=environment,
        image=tool,
        vcpus=vcpus,
        memory=memory_mb,
        timeout=timeout_s,
        input_json=json.dumps(inputs),
    )
    debug_print("{} Request".format(identifier), request, verbose=verbose)
    return request


def inspect_bx_response(
    response,
    identifier: str,
    acceptable_exit_codes: tuple[int, ...] = (0,),
    inacceptable_exit_code_raise_error: bool = False,
    verbose: bool = True,
):
    # check potential error message
    error_message = getattr(response, "error_message", None)
    exit_code = getattr(response, "exit_code", None)

    if error_message not in {None, ""}:
        debug_print(
            "{} Error message".format(identifier),
            error_message,
            verbose=verbose,
            long=False,
        )

    # check exit code
    exit_code = check_for_acceptable_exit_code(
        identifier=identifier,
        error_message=error_message,
        exit_code=exit_code,
        acceptable_exit_codes=acceptable_exit_codes,
        raise_error=inacceptable_exit_code_raise_error,
    )
    return exit_code


def run_command(
    command: str,
    identifier: str = "",
    output_fp: Path | str | None = None,
    verbose: bool = True,
    cwd=None,
    shell: bool = True,
    reraise: bool = True,
    custom_exceptions: list | None = None,
    acceptable_exit_codes: tuple[int, ...] = (0,),
    inacceptable_exit_code_raise_error: bool = False,
):

    debug_print("{} command".format(identifier), command, verbose=verbose, long=False)
    run_subprocess = partial(
        sp.run,
        command,
        cwd=cwd,
        shell=shell,
        stderr=sp.PIPE,
        encoding="utf-8",
    )

    try:
        if output_fp is None:
            completed_subprocess = run_subprocess()
        else:
            with open(output_fp, "w") as f:
                completed_subprocess = run_subprocess(stdout=f)
    except Exception as e:
        handle_unknown_exception(exception=e, identifier=identifier, reraise=reraise)

    # see if the output is good or we need to trigger an error of some kind.
    stderr = completed_subprocess.stderr
    check_for_custom_exception(stderr, custom_exceptions=custom_exceptions)

    exit_code = completed_subprocess.returncode
    exit_code = check_for_acceptable_exit_code(
        identifier=identifier,
        error_message=stderr,
        exit_code=exit_code,
        acceptable_exit_codes=acceptable_exit_codes,
        raise_error=inacceptable_exit_code_raise_error,
    )
    return exit_code


def run_bx_job(
    tool: str,
    inputs: dict,
    output_fp=None,
    environment: str | None = None,
    vcpus=DEFAULT_VCPUS,
    memory_mb=DEFAULT_MEMORY_MB,
    timeout_s: int = 15 * 60,
    verbose: bool = True,
    reraise: bool = True,
    acceptable_exit_codes: tuple[int, ...] = (0,),
    inacceptable_exit_code_raise_error: bool = False,
):
    # Initialize
    output_json = dict()
    identifier = "{t} bx job submit".format(t=tool)

    bx.connect()
    job_service = bx.JobService()

    request = get_bx_request(
        job_service,
        identifier=identifier,
        tool=tool,
        inputs=inputs,
        environment=environment,
        vcpus=vcpus,
        memory_mb=memory_mb,
        timeout_s=timeout_s,
        verbose=verbose,
    )

    try:
        response = job_service.Run(request)
        debug_print("{} Response".format(identifier), response, verbose=verbose)

        output_json = json.loads(getattr(response, "output_json", "{}"))
        if output_fp is not None:
            save_json(output_json, output_fp)
        else:
            pass
    except Exception as e:
        handle_unknown_exception(exception=e, identifier=identifier, reraise=reraise)

    exit_code = inspect_bx_response(
        identifier=identifier,
        acceptable_exit_codes=acceptable_exit_codes,
        inacceptable_exit_code_raise_error=inacceptable_exit_code_raise_error,
        verbose=verbose,
    )

    return exit_code, output_json
