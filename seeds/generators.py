import datetime
import uuid

from flask_seeder.generator import Generator


class GenericListItem(Generator):
    def __init__(self, generic_list, **kwargs):
        super().__init__(**kwargs)
        self.generic_list = generic_list

    def generate(self):
        result = self.generic_list[self.rnd.randint(0, len(self.generic_list) - 1)]
        return result


class Uuid(Generator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def generate(self):
        gen_uuid = str(uuid.uuid4())
        return gen_uuid


class UserUuid(Generator):
    def __init__(self, uuid_container, **kwargs):
        super().__init__(**kwargs)
        self.uuid_container = uuid_container

    def generate(self):
        selected_uuid = self.uuid_container.user_uuids_generated[
            self.rnd.randint(0, len(self.uuid_container.user_uuids_generated) - 1)
        ]
        self.uuid_container.user_uuids_generated.remove(selected_uuid)
        return selected_uuid


class RelationalPrimaryKey(Generator):
    def __init__(self, uuid_container, **kwargs):
        super().__init__(**kwargs)
        self.uuid_container = uuid_container

    def generate(self):
        selected_uuid = self.uuid_container.user_uuids_generated[
            self.rnd.randint(0, len(self.uuid_container.user_uuids_generated) - 1)
        ]
        self.uuid_container.user_uuids_generated.remove(selected_uuid)
        return selected_uuid


class ToUserUuid(Generator):
    def __init__(self, uuid_container, **kwargs):
        super().__init__(**kwargs)
        self.uuid_container = uuid_container

    def generate(self):
        selected_uuid = self.uuid_container.copy[
            self.rnd.randint(0, len(self.uuid_container.copy) - 1)
        ]
        return selected_uuid


class RelationalForeignKey(Generator):
    def __init__(self, uuid_container, **kwargs):
        super().__init__(**kwargs)
        self.uuid_container = uuid_container

    def generate(self):
        selected_uuid = self.uuid_container.copy[
            self.rnd.randint(0, len(self.uuid_container.copy) - 1)
        ]
        return selected_uuid


# class UserUuid(Generator):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#     def generate(self):
#         gen_uuid = str(uuid.uuid4())
#         UserUuidsGenerated.append(gen_uuid)
#         return gen_uuid
#
#
# class MissionUuid(Generator):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#     def generate(self):
#         gen_uuid = str(uuid.uuid4())
#         MissionUuidsGenerated.append(gen_uuid)
#         return gen_uuid


# class UuidFromReferenceList(Generator):
#     def __init__(self, reference_list, **kwargs):
#         super().__init__(**kwargs)
#         self.reference_list = reference_list
#
#     def generate(self):
#         result = self.reference_list[self.rnd.randint(0, len(self.reference_list) - 1)]
#         return result


class Email(Generator):
    def __init__(self, first_names, last_names, **kwargs):
        super().__init__(**kwargs)
        self.first_names = first_names
        self.last_names = last_names

    def generate(self):
        result = '{0}.{1}@zebro.com'.format(
            self.first_names[self.rnd.randint(0, len(self.first_names) - 1)],
            self.last_names[self.rnd.randint(0, len(self.last_names) - 1)],
        )
        return result


class Username(Generator):
    def __init__(self, user_names, **kwargs):
        super().__init__(**kwargs)
        self.user_names = user_names

    def generate(self):
        result = '{0} the zebro'.format(
            self.user_names[self.rnd.randint(0, len(self.user_names) - 1)]
        )
        return result


class DateTime(Generator):

    def __init__(self, start_date, end_date, **kwargs):
        super().__init__(**kwargs)
        self.start_date = start_date
        self.end_date = end_date

    def random_date(self, start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = self.rnd.randrange(int_delta)
        return start + datetime.timedelta(seconds=random_second)

    def generate(self):
        result = self.random_date(start=self.start_date, end=self.end_date)
        return result
