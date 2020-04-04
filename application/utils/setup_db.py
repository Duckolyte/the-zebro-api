import datetime
import random
import uuid

from application.models import Mission


# Helper methods.
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


# Method to setup DB with random records.
def setup_db(db):
    # Setup User records.
    random_user_ids = [uuid.uuid4() for i in range(5)]
    # TODO create user db records

    # Setup missions records.
    parc_sections = ['H', 'M']
    d1 = datetime.strptime('2019-01-01 11:11:11', '%Y-%m-%d %H:%M:%S')
    d2 = datetime.strptime('2020-04-01 11:11:11', '%Y-%m-%d %H:%M:%S')

    for i in range(10):
        new_mission = Mission(
            id=uuid.uuid4(),
            userId=random_user_ids[random.randint(0, 1)],
            parcSection=parc_sections[random.randint(0, 1)],
            timeStamp=random_date(d1, d2)
        )
        db.session.add(new_mission)
        db.session.commit()
