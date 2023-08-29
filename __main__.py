from .src.cli import init_cli
from .src import git

if __name__ == "__main__":
    if git.exists():
        print(git.is_repo())
        print(git.head_detached_or_no_commits())

    # cli = init_cli()
    # args = cli.parse_args()

    # if args.command == "init":
    #     print("init")
    # elif args.command == "send":
    #     print("send")
    # elif args.command == "sync":
    #     print("sync")
    # elif args.command == "remote":
    #     if args.subcommand == "add":
    #         print("remote add")
    #     elif args.subcommand == "remove":
    #         print("remote remove")
