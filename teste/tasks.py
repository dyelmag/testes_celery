from celery import task 
from celery import shared_task 
# We can have either registered task 
@shared_task(bind=True) 
def send_notifiction(id1, id2):
    print('ID:' + id1)
    print('ID2:' + id2)
    print('-----------------')
    
     # Another trick


@task(name="teste")
def send_feedback_email_task():
    """sends an email when feedback form is filled successfully"""
    arquivo = open('novo-arquivo.txt', 'w')
    arquivo.write('nova linha')
    arquivo.close()