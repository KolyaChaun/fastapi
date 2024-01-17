from abc import ABC, abstractmethod
import config
import pymongo
import certifi
from uuid import uuid4


class BaseStorage:
    @abstractmethod
    def create_recipe(self, bag: dict):
        pass

    @abstractmethod
    def get_recipe(self):
        pass

    @abstractmethod
    def get_recipes_info(self, recipe_uuid: str):
        pass

    @abstractmethod
    def update_recipe(self, recipe_uuid: str, new_description: str):
        pass

    @abstractmethod
    def delete_recipe(self, recipe_uuid: str):
        pass


class MongoStorage(BaseStorage):
    def __init__(self):
        url = "mongodb+srv://user_mykola:wT0r4UG9MUlL5o25@mykola.nweq7k5.mongodb.net/?retryWrites=true&w=majority".format(
            user=config.USER_MONGO,
            password=config.PASSWORD_MONGO,
        )

        client = pymongo.MongoClient(url, tlsCAFile=certifi.where())

        db = client["Recipes"]
        self.collection = db["Recipes"]

    def create_recipe(self, recipe: dict) -> dict:
        recipe["uuid"] = str(uuid4())
        self.collection.insert_one(recipe)
        return recipe

    def get_recipe(self, skip: int = 0, limit: int = 10, search_param: str = None):
        query = {}
        if search_param:
            query = {"title": {"$regex": search_param.strip()}}
        return self.collection.find(query).skip(skip).limit(limit)

    def update_recipe(self, recipe_uuid: str, new_description: str):
        filter_data = {"uuid": recipe_uuid}
        new_data = {"$set": {"description": new_description}}
        processed = self.collection.update_one(filter_data, new_data)
        return processed

    def delete_recipe(self, recipe_uuid: str):
        filter_data = {"uuid": recipe_uuid}
        self.collection.delete_one(filter_data)

    def get_recipes_info(self, recipe_uuid: str):
        filter_data = {'uuid': recipe_uuid}
        return self.collection.find(filter_data)


storage = MongoStorage()
