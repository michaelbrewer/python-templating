# Experiments with templates

This repo has 2 types of python templates: [copier](https://copier.readthedocs.io/en/latest/) and [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/).

## Basic Differences

- **Copier**:
  - Uses a YAML configuration file.
  - Supports advanced templating features like inheritance and conditional logic.
  - Can update existing projects with new template versions.

- **Cookiecutter**:
  - Uses a JSON configuration file.
  - Focuses on simplicity and ease of use.
  - Does not support updating existing projects with new template versions.

## Task Hooks

Both Copier and Cookiecutter support task hooks, which allow you to run arbitrary commands at different stages of the templating process.

### Copier Task Hooks

Copier uses a `_tasks` section in the YAML configuration file to define hooks. You can specify commands to run before or after certain events.

Example `copier.yml`:

```yaml
_tasks:
    # Strings get executed under system's default shell
    - "git init"
    - "rm {{ name_of_the_project }}/README.md"
    # Arrays are executed without shell, saving you the work of escaping arguments
    - [invoke, "--search-root={{ _copier_conf.src_path }}", after-copy]
    # You are able to output the full conf to JSON, to be parsed by your script
    - [invoke, end-process, "--full-conf={{ _copier_conf|to_json }}"]
    # Your script can be run by the same Python environment used to run Copier
    - ["{{ _copier_python }}", task.py]
    # OS-specific task (supported values are "linux", "macos", "windows" and `None`)
    - command: rm {{ name_of_the_project }}/README.md
      when: "{{ _copier_conf.os in  ['linux', 'macos'] }}"
    - command: Remove-Item {{ name_of_the_project }}\\README.md
      when: "{{ _copier_conf.os == 'windows' }}"
```

### Cookiecutter Task Hooks

Cookiecutter uses a `hooks` directory to define pre-generation and post-generation hooks. You can create Python or shell scripts to run at these stages.

Example directory structure:

```text
cookiecutter-template/
├── cookiecutter.json
├── hooks/
│   ├── pre_gen_project.py
│   └── post_gen_project.py
└── {{cookiecutter.project_slug}}/
```

Example `pre_gen_project.py`:

```python
print("Running pre-generation hook")
```

Example `post_gen_project.py`:

```python
print("Running post-generation hook")
```

## Usage

Install the required packages:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Copier

Running the copier example code:

```bash
python main_copier.py
```

### Cookiecutter

Running the cookiecutter example code:

```bash
python main_cookiecutter.py
```
