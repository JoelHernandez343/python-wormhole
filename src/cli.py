from argparse import ArgumentParser


def init_cli() -> ArgumentParser:
    cli_parser = ArgumentParser(description="Command to share git bundles using email")
    cli_commands = cli_parser.add_subparsers(dest="command", help="available commands", required=True)

    # init command
    init_cmd = cli_commands.add_parser("init", help="initialize tracking on repo")
    init_cmd.add_argument("uuid", help="tracker id", nargs="?")

    # send command
    send_cmd = cli_commands.add_parser("send", help="bundle and send branches to a target")
    send_cmd.add_argument("branches", nargs="*", help="array of branches")
    send_cmd.add_argument("--to", dest="id", required=True, help="target id to send the bundle")
    send_cmd.add_argument("--all", dest="include_all_branches")
    send_cmd.add_argument(
        "--store_only", action="store_true", help="only save bundle in default and remote's path if any"
    )

    # sync command
    sync_cmd = cli_commands.add_parser("sync", help="download bundle from remote")
    sync_cmd.add_argument("branches", nargs="*", help="array of branches")
    sync_cmd.add_argument("--from", dest="id", required=True, help="remote id remote from where to sync")
    sync_cmd.add_argument("--all", dest="include_all_branches")

    # remote command
    remote_cmd = cli_commands.add_parser("remote", help="add or remove")
    remote_subcommands = remote_cmd.add_subparsers(dest="subcommand", help="remote subcommands", required=True)

    # remote add subcommand
    add_remote_subcmd = remote_subcommands.add_parser("add", help="add remote")
    add_remote_subcmd.add_argument("id", help="remote to add")
    add_remote_subcmd.add_argument("--email", help="remote's email")
    add_remote_subcmd.add_argument("--path", help="path where copy the bundle")
    add_remote_subcmd.add_argument("--update", help="if exists, update the remote's info", action="store_true")

    # remote remove subcommand
    remove_remote_subcmd = remote_subcommands.add_parser("remove", help="remove remote")
    remove_remote_subcmd.add_argument("id", help="remote to remove")

    return cli_parser
