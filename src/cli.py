# Joel Hernández @ 2023
# Github profile: https://github.com/JoelHernandez343

# typing
import __future__
from typing import NamedTuple, Literal

# libs
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter


# types
class Arguments(NamedTuple):
    command: Literal["config", "init", "send", "sync", "remote"]
    subcommand: Literal["list", "add", "remove"]

    id: str

    email: str
    auto: bool
    show: bool
    get_config_path: str

    uuid: str

    branches: list[str]
    all: bool
    store_only: bool
    from_ref: str
    no_tag: bool

    path: str
    update: bool


# constants
CURRENT_VERSION = "pre-0.0.1"
COPYRIGHT = "Copyright 2023 Joel Harim Hernández Javier under MIT License"
DESCRIPTION = "Wormhole: Git bundler helper. Allows syncing repos when direct access is not available using email"


def init_cli() -> ArgumentParser:
    cli_parser = ArgumentParser(
        description=DESCRIPTION,
        epilog=COPYRIGHT,
        formatter_class=RawDescriptionHelpFormatter,
    )
    cli_commands = cli_parser.add_subparsers(
        dest="command",
        help="available commands",
        required=True,
    )

    # configuration command
    config_cmd = cli_commands.add_parser("config", help="configure personal information")
    config_cmd.add_argument(
        "--id",
        help="config own id",
        metavar="<id>",
        required="--email" in sys.argv,
    )
    config_cmd.add_argument(
        "--email",
        help="config own email",
        metavar="<email>",
        required="--id" in sys.argv,
    )
    config_cmd.add_argument(
        "--auto",
        help="get username and email from git itself",
        action="store_true",
    )
    config_cmd.add_argument(
        "--show",
        action="store_true",
        help="shows current configuration",
    )
    config_cmd.add_argument(
        "--get-config-path",
        action="store_true",
        help="shows config path",
    )

    # init command
    init_cmd = cli_commands.add_parser(
        "init",
        help="initialize tracking on repo",
    )
    init_cmd.add_argument(
        "uuid",
        help="tracker id",
        nargs="?",
    )

    # send command
    send_cmd = cli_commands.add_parser(
        "send",
        help="bundle and send branches to a target",
    )
    send_cmd.add_argument(
        "branches",
        nargs="*",
        help="array of branches to bundle",
        metavar="<branch>",
    )
    send_cmd.add_argument(
        "--to",
        dest="id",
        required=True,
        help="target id to send the bundle",
        metavar="<target_id>",
    )
    send_cmd.add_argument(
        "--all",
        action="store_true",
        help="indicate if include all branches",
    )
    send_cmd.add_argument(
        "--store-only",
        action="store_true",
        help="only save bundle in default and remote's path if any",
    )
    send_cmd.add_argument(
        "--from-ref",
        help="use custom ref instead of current branch, ignored when multiple branches to bundle are provided",
        metavar="<reference>",
    )
    send_cmd.add_argument(
        "--no-tag",
        action="store_true",
        help="do not create a new bundle tag",
    )

    # sync command
    sync_cmd = cli_commands.add_parser(
        "sync",
        help="download bundle from remote",
    )
    sync_cmd.add_argument(
        "branches",
        nargs="*",
        help="array of branches",
        metavar="<branch>",
    )
    sync_cmd.add_argument(
        "--from",
        dest="id",
        required=True,
        help="remote id remote from where to sync",
        metavar="<target_id>",
    )
    sync_cmd.add_argument(
        "--all",
        action="store_true",
        help="indicate if include all branches",
    )

    # remote command
    remote_cmd = cli_commands.add_parser(
        "remote",
        help="add or remove",
    )
    remote_subcommands = remote_cmd.add_subparsers(
        dest="subcommand",
        help="remote subcommands",
        required=True,
    )

    # remote list subcommand
    list_remote_subcmd = remote_subcommands.add_parser("list", help="list remotes")

    # remote add subcommand
    add_remote_subcmd = remote_subcommands.add_parser("add", help="add remote")
    add_remote_subcmd.add_argument(
        "id",
        help="remote's id to add",
    )
    add_remote_subcmd.add_argument(
        "--email",
        help="remote's email",
    )
    add_remote_subcmd.add_argument(
        "--path",
        help="path where copy the bundle",
    )
    add_remote_subcmd.add_argument(
        "--update",
        help="if exists, update the remote's info",
        action="store_true",
    )

    # remote remove subcommand
    remove_remote_subcmd = remote_subcommands.add_parser(
        "remove",
        help="remove remote",
    )
    remove_remote_subcmd.add_argument(
        "id",
        help="remote's id to remove",
    )

    # version
    cli_parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=CURRENT_VERSION,
    )

    return cli_parser
