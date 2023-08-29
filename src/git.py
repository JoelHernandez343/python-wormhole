# libs
import subprocess


from typing import NamedTuple


# types
class ExecutionResults(NamedTuple):
    out: str
    err: str
    code: int


def gitex(arguments: list[str]) -> ExecutionResults:
    process = subprocess.run(
        ["powershell.exe", "git"] + arguments,
        capture_output=True,
    )

    out = process.stdout.decode("utf-8")
    err = process.stderr.decode("utf-8")
    code = process.returncode

    return ExecutionResults(out=out, err=err, code=code)


def exists() -> bool:
    return gitex(["--version"]).code == 0


def is_repo() -> bool:
    return gitex(["rev-parse", "--is-inside-work-tree"]).code == 0


def head_detached_or_no_commits() -> bool:
    return gitex(["rev-parse", "--abbrev-ref", "HEAD"]).out == "HEAD\n"


def current_branch() -> str | None:
    if branch := gitex(["branch", "--show-current"]).out.replace("\n", ""):
        return branch
    else:
        return None
