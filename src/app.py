# Joel Hernández @ 2023
# Github profile: https://github.com/JoelHernandez343

from .cli import init_cli, Arguments

from . import config


def user_info(args: Arguments) -> None:
    if args.id or args.auto:
        config.set_user_info(user_id=args.id, email=args.email)
    elif args.get_config_path:
        print(config.CONFIG_FILE)
    else:
        user_info = config.get_user_info()

        if user_info:
            print(f"user_id: {user_info[0]}, email: {user_info[1]}")
        else:
            print("Not configured")


def run() -> None:
    cli = init_cli()
    args: Arguments = cli.parse_args()

    command = args.command

    if hasattr(args, "subcommand"):
        subcommand = args.subcommand

    if command == "config":
        user_info(args)
