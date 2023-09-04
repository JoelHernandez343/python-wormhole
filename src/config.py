# Joel Hernández @ 2023
# Github profile: https://github.com/JoelHernandez343

# typing
import __future__

# libs
import yaml, os

# local libs
from . import git
from .constants import CONFIG_FILE


def set_user_info(user_id: str, email: str) -> None:
    if not user_id and not email:
        user_id, email = git.get_current_user_info()
        print(f"! Warning: using git config values: {user_id} {email}")

    if not CONFIG_FILE.parent.exists():
        CONFIG_FILE.parent.mkdir()

    with open(CONFIG_FILE, mode="w", encoding="utf-8") as config_file:
        new_config = {
            "user_information": {
                "user_id": user_id,
                "email": email,
            }
        }

        config_file.write(yaml.safe_dump(new_config))


def get_user_info() -> tuple[str, str] | None:
    if not CONFIG_FILE.exists():
        return None

    with open(CONFIG_FILE, mode="r", encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file)
        user_info = config["user_information"]

        return user_info["user_id"], user_info["email"]
