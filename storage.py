from abc import ABC, abstractmethod
import config
import pymongo
import certifi


class BaseStorage:
    @abstractmethod
    def create_bag(self, bag: dict):
        pass

    @abstractmethod
    def get_bags(self):
        pass

    @abstractmethod
    def get_bags_by_title(self):
        pass

    @abstractmethod
    def update_bag(self):
        pass

    @abstractmethod
    def delete_bag(self):
        pass


class MongoStorage(BaseStorage):
    def __init__(self):
        url = "mongodb+srv://user_mykola:wT0r4UG9MUlL5o25@mykola.nweq7k5.mongodb.net/?retryWrites=true&w=majority".format(
            user=config.USER_MONGO,
            password=config.PASSWORD_MONGO,
        )

        client = pymongo.MongoClient(url, tlsCAFile=certifi.where())

        db = client['Bags']
        self.collection = db['Bags']

    def create_bag(self, bag: dict):
        self.collection.insert_one(bag)

    def get_bags(self):
        raise NotImplemented

    def get_bags_by_title(self):
        raise NotImplemented

    def update_bag(self):
        raise NotImplemented

    def delete_bag(self):
        raise NotImplemented


storage = MongoStorage()
