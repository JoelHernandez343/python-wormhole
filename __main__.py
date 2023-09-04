# Copyright 2023 Joel Harim Hernández Javier under MIT License
# Github profile: https://github.com/JoelHernandez343
#        _________________
#       /                 \
#      /      .  -  .      \
#     /      { \   / }      \
#    /        '-___-'        \
#   /_________________________\
#        _______: :_______
#       /       | |       \
#      /       /   \       \
#     /      :'     ':      \
#    /        '-----'        \
#   /______ wormhole.git _____\
#
# Wormhole: Wormhole: Git bundler helper.
# Allows syncing repos when direct acces is not available
# using email
# Based on http://stackoverflow.com/a/3639182/2877364
# Art based in Henry Segerman's


from .src.cli import init_cli
from .src import app, git

if __name__ == "__main__":
    app.run()

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
