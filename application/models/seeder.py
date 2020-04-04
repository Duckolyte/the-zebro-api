import uuid
from datetime import datetime
from random import random

from flask_seeder import Seeder, Faker

from .mission import Mission


# Helper methods.
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


random_user_ids = [uuid.uuid4() for i in range(5)]
parc_sections = ['H', 'M']
d1 = datetime.strptime('2019-01-01 11:11:11', '%Y-%m-%d %H:%M:%S')
d2 = datetime.strptime('2020-04-01 11:11:11', '%Y-%m-%d %H:%M:%S')


class MissionSeeder(Seeder):

    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=Mission,
            init={
                'id': uuid.uuid4(),
                'userId': random_user_ids[random.randint(0, 1)],
                'parcSection': parc_sections[random.randint(0, 1)],
                'timeStamp': random_date(d1, d2)
            }
        )

        # Create 5 users
        for mission in faker.create(10):
            print("Adding mission: %s" % mission)
            self.db.session.add(mission)
