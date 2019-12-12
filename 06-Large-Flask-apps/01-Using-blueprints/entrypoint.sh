#!/usr/bin/env bash
flask db init
flask db migrate -m "first migration"
flask db upgrade
python3 app.py