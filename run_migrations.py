# run_migrations.py
import django
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "repair_project.settings")
django.setup()

from django.core.management import call_command

call_command("makemigrations")
call_command("migrate")
