# Example

Testing {{ cookiecutter.answer }}

{% if cookiecutter.emails %}Emails:

{% for email, name in cookiecutter.emails|dictsort %}- {{ email }} - {{ name }}
{% endfor %}
{% endif %}
