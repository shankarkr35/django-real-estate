from __future__ import absolute_import
import os
from celery import Celery
from real_estate.settings import base
from dotenv import load_dotenv

# Set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate.settings.developement')

# Create the Celery app instance
app = Celery("real_estate")

# Load the configuration from the specified settings module with a 'CELERY' namespace
app.config_from_object("real_estate.settings.developement", namespace="CELERY")

# Automatically discover tasks from installed apps
app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
