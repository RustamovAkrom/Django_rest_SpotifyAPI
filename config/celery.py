import os
from celery import Celery
<<<<<<< HEAD

=======
from django.conf import settings
>>>>>>> 8ba28da (update dir in push)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")
<<<<<<< HEAD
app.autodiscover_tasks()
=======
app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
>>>>>>> 8ba28da (update dir in push)
