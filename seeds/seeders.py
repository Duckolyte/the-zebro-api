import datetime
import random

from flask_seeder import Seeder, Faker, generator

from application.models import User, Spot
from application.models.mission import Mission
from application.models.spot import GpsPoint
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


class RelationalPrimaryKeyContainer:
    def __init__(self, uuids):
        """
        This container class holds...

        A list of uuids for users. When a user db record is inserted the inserted id
        gets removed. Prevents unique constraint errors.

        A copy of the uuids list for users. This list is used for the missions referencing
        users by their id (uuid). Necessary because the foreign keys must match the
        users ids at transaction commit.

        """
        self.user_uuids_generated = uuids[:]
        self.copy = uuids[:]


gen_user_uuids = [generators.Uuid().generate() for i in range(5)]
user_uuids_container = RelationalPrimaryKeyContainer(uuids=gen_user_uuids)

gen_mission_uuids = [generators.Uuid().generate() for i in range(10)]
mission_uuids_container = RelationalPrimaryKeyContainer(uuids=gen_mission_uuids)

gen_spot_uuids = [generators.Uuid().generate() for i in range(10)]
spot_uuids_container = RelationalPrimaryKeyContainer(uuids=gen_spot_uuids)

gen_gps_uuids = [generators.Uuid().generate() for i in range(10)]
gps_uuids_container = RelationalPrimaryKeyContainer(uuids=gen_gps_uuids)

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
                'id': generators.RelationalPrimaryKey(user_uuids_container)
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
        faker = Faker(
            cls=Mission,
            init={
                'userId': generators.RelationalForeignKey(user_uuids_container),
                'parcSection': generators.GenericListItem(generic_list=parc_sections),
                'timeStamp': generators.DateTime(start_date=d1, end_date=d2),
                'id': generators.RelationalPrimaryKey(mission_uuids_container)
            }
        )

        for mission in faker.create(10):
            print("Adding mission: %s" % mission)
            self.db.session.add(mission)


"""
Spots seeds section.
"""
obs_quality_codes = ['A', 'B', 'C', 'D']
obs_date_start = datetime.datetime.strptime('2019-01-01 11:11:11', '%Y-%m-%d %H:%M:%S')
obs_date_end = datetime.datetime.strptime('2020-04-01 11:11:11', '%Y-%m-%d %H:%M:%S')


class SpotSeeder(Seeder):

    def run(self):
        faker = Faker(
            cls=Spot,
            init={
                'missionId': generators.RelationalForeignKey(mission_uuids_container),
                'observationQualityCode': generators.GenericListItem(generic_list=obs_quality_codes),
                'observationDateTime': generators.DateTime(start_date=obs_date_start, end_date=obs_date_end),
                'id': generators.RelationalPrimaryKey(spot_uuids_container)
            }
        )

        for spot in faker.create(10):
            print("Adding spot: %s" % spot)
            self.db.session.add(spot)


"""
Gps seeds section.
"""
gps_lat_lon = ['52.518611', '13.376111', '48.208031', '16.358128', '13.380000', '52.520000']


class GpsPointSeeder(Seeder):

    def run(self):
        faker = Faker(
            cls=GpsPoint,
            init={
                'spotId': generators.RelationalForeignKey(spot_uuids_container),
                'lat': generators.GenericListItem(gps_lat_lon),
                'lon': generators.GenericListItem(gps_lat_lon),
                'id': generators.RelationalPrimaryKey(gps_uuids_container)
            }
        )

        for gps in faker.create(10):
            print("Adding gps: %s" % gps)
            self.db.session.add(gps)
