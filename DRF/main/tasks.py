from DRF.celery import app

from main.service import lol
from main.models import (Company, Employer,
                         Offices, Person)

@app.task
def check_models():
    models = [Company, Employer, Offices, Person]
    lol(models)
