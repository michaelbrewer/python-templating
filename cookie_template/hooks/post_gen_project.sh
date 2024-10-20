#!/bin/bash
git init
cat test.md
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ls -lha
python main.py
git add .
git status
