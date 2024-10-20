import copier
import os
from tempfile import TemporaryDirectory


def run_copier(temp_dir):
    copier.run_copy(
        src_path="copier_template",
        dst_path=temp_dir,
        data={
            "answer": "My Project",
            "apm": "APM1001",
            "name": "My Name",
            "description": "My Description",
            "emails": { 
                "test1@fiserv.com": "Mike Brewer",
                "test2@fiserv.com": "John"
            },
        },
        quiet=False,
        unsafe=True,
    )
    print(f"Project created at {temp_dir}")


if __name__ == "__main__":
    with TemporaryDirectory(dir=os.getcwd()) as temp_dir:
        print(f"Created temporary directory at {temp_dir}")
        run_copier(temp_dir)
