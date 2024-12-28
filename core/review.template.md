# 🚀 {{ repo.full_name }}

![GitHub last commit](https://img.shields.io/github/last-commit/{{ repo.full_name }}?style=flat-square)
![GitHub Repo stars](https://img.shields.io/github/stars/{{ repo.full_name }}?style=flat-square)

{% for label in repo.topics %} `{{ label }}` {% endfor %}

> {{ repo.description }}

- 🌐 {{ repo.html_url }}