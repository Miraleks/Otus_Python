#!/usr/bin/env sh

echo Run prestart script

sleep 30;

flask --app start_app.py db upgrade
