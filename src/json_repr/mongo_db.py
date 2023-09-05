import json


class MongoDbType:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({json.dumps(self.value, ensure_ascii=False)})"
        )


class ObjectId(MongoDbType):
    pass


class NumberInt(MongoDbType):
    pass


def mongo_db_globals():
    global null
    null = None

    global true
    true = True

    global false
    false = False
