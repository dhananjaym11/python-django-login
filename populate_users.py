import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login_project.settings')

import django
django.setup()

from userapp.models import User
from faker import Faker
import random
# Configure settings for project
# Need to run this before calling models from application!

# Import settings
fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # Create new Webpage Entry
        user_data = User.objects.get_or_create(
            first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]



if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')