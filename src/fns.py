import subprocess


def greetings() -> None:
    print("Hello world")


def check_git():
    output = subprocess.run(
        ["powershell.exe", "git", "--version"], check=True, capture_output=True
    )
    print(output.stdout.decode("utf-8"))
