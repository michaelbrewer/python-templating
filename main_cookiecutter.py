import os
from tempfile import TemporaryDirectory

from cookiecutter.main import cookiecutter


def main(temp_dir):
    cookiecutter(
        template="cookie_template",
        output_dir=temp_dir,
        no_input=True,
        extra_context={
            "answer": "My Project",
            "apm": "APM1111",
            "name": "My Name",
            "description": "My Description",
            "emails": {
                "test1@fiserv.com": "Mike",
                "test2@fiserv.com": "John",
            },
        },
    )
    print(f"Project created at {temp_dir}")


if __name__ == "__main__":
    with TemporaryDirectory(dir=os.getcwd()) as temp_dir:
        print(f"Created temporary directory at {temp_dir}")
        main(temp_dir)
