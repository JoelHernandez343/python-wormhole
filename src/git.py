# Joel Hernández @ 2023
# Github profile: https://github.com/JoelHernandez343

# typing
import __future__
from typing import NamedTuple

# libs
import subprocess


# types
class ExecutionResults(NamedTuple):
    out: str
    err: str
    code: int


def gitex(args: list[str]) -> ExecutionResults:
    process = subprocess.run(["git.exe"] + args, capture_output=True)

    out = process.stdout.decode("utf-8")
    err = process.stderr.decode("utf-8")
    code = process.returncode

    return ExecutionResults(out=out, err=err, code=code)


def exists() -> bool:
    try:
        return gitex(["--version"]).code == 0
    except FileNotFoundError:
        return False


def is_repo() -> bool:
    return gitex(["rev-parse", "--is-inside-work-tree"]).code == 0


def is_head_detached_or_no_commits() -> bool:
    return gitex(["rev-parse", "--abbrev-ref", "HEAD"]).out == "HEAD\n"


def is_merging_in_progress() -> bool:
    return gitex(["merge", "HEAD"]).code != 0


def are_uncommited_changes() -> bool:
    return len(gitex(["status", "--porcelain"]).out.split("\n")) > 1


def get_tags_w_commits(remote: str, branch: str) -> list[list[str]]:
    tags = gitex(
        [
            "for-each-ref",
            "--sort=-creatordate",
            "--format",
            r"%(refname)-%(objectname)",
            f"refs/tags/wormhole/{remote}/{branch}",
        ]
    ).out.split("\n")

    return [tag.replace("refs/tags/", "").split("-") for tag in tags if tag]


def current_branch() -> str | None:
    if branch := gitex(["branch", "--show-current"]).out.replace("\n", ""):
        return branch
    else:
        return None


def current_commit() -> str:
    return gitex(["rev-parse", "HEAD"]).out.replace("\n", "")
