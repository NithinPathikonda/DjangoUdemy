import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myFirstProject.settings')


import django
django.setup()


import random 
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen=Faker()
topics=['Search','Social','Market Place','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top=add_topic()

        #creating the fake data for the entry 
        fake_url=fakegen.url()
        fake_name=fakegen.company()
        fake_date=fakegen.date()

        webpg=Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        access_record=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]



if __name__ == '__main__':
    print('Populating Script!!')
    populate(20)
    print('Populating Complete')
