from celery import Celery
from appcore.settings import get_config

app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def do_claim_ad(account_id, ad_id):
    return True
