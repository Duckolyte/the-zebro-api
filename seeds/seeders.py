import datetime
import random

from flask_seeder import Seeder, Faker, generator

from application.models import User
from application.models.mission import Mission
from seeds import generators

"""
Seeding helper methods. 
"""


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


"""
User seeds section.
"""


class UserUuidsContainer:
    def __init__(self, uuids):
        """
        This container class holds...

        A list of uuids for users. When a user db record is inserted the inserted id
        gets removed. Prevents unique constraint errors.

        A copy of the uuids list for users. This list is used for the missions referencing
        users by their id (uuid). Necessary because the foreign keys must match the
        users ids at transaction commit.

        """
        self.user_uuids_generated = uuids
        self.copy = uuids


gen_user_uuids = [generators.Uuid().generate() for i in range(5)]
user_uuids_container = UserUuidsContainer(gen_user_uuids)

random_first_names = [generator.Name().generate() for i in range(10)]
random_last_names = [generator.Name().generate() for i in range(10)]
random_user_names = [generator.Name().generate() for i in range(10)]

rock_solid_passwords = ['12345', 'admin']
date_of_birth_start = datetime.datetime.strptime('2019-01-01 11:11:11', '%Y-%m-%d %H:%M:%S')
date_of_birth_end = datetime.datetime.strptime('2020-04-01 11:11:11', '%Y-%m-%d %H:%M:%S')


class UserSeeder(Seeder):

    def run(self):
        faker = Faker(
            cls=User,
            init={
                'first_name': generator.Name(),
                'second_name': generator.Name(),
                'last_name': generator.Name(),
                'date_of_birth': generators.DateTime(
                    start_date=date_of_birth_start,
                    end_date=date_of_birth_end
                ),
                'user_name': generators.Username(user_names=random_user_names),
                'email': generators.Email(
                    first_names=random_first_names,
                    last_names=random_last_names
                ),
                'password': generators.GenericListItem(generic_list=rock_solid_passwords),
                'id': generators.UserUuid(user_uuids_container)
            }
        )

        # Create 5 users
        for user in faker.create(5):
            print("Adding user: %s" % user)
            self.db.session.add(user)


"""
Mission seeds section.
"""
parc_sections = ['H', 'M']
d1 = datetime.datetime.strptime('2019-01-01 11:11:11', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime('2020-04-01 11:11:11', '%Y-%m-%d %H:%M:%S')


class MissionSeeder(Seeder):

    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=Mission,
            init={
                'userId': generators.ToUserUuid(user_uuids_container),
                'parcSection': generators.GenericListItem(generic_list=parc_sections),
                'timeStamp': generators.DateTime(start_date=d1, end_date=d2),
                'id': generators.Uuid(),
            }
        )

        # Create 5 users
        for mission in faker.create(10):
            print("Adding mission: %s" % mission)
            self.db.session.add(mission)
