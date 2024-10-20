import os
import subprocess

tasks = """
git init
cat test.md
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ls -lha
python main.py
git add .
git status
"""
"""List of commands to run after project generation."""

def post_gen_project():
    """Run tasks after project generation.

    This function reads a list of tasks from a global variable `tasks`, splits them into individual commands,
    and executes them sequentially in a bash shell. Each command is prefixed with an echo statement that 
    prints the task number and the command being executed in blue text.

    Raises:
        subprocess.CalledProcessError: If any of the commands return a non-zero exit status.
    """
    command_list = tasks.strip().split("\n")
    commands = "\n".join(
        [
            f"echo -e '\\033[34mRunning task {i+1} of {len(command_list)}: {cmd}\\033[0m' && {cmd}"
            for i, cmd in enumerate(command_list)
        ]
    )
    subprocess.run(["bash", "-c", commands], check=True)


if __name__ == "__main__":
    if os.path.exists(".git"):
        print("\033[1;33mGit repository already initialized. Skipping python tasks.\033[0m")
    else:
        post_gen_project()
