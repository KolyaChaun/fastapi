from abc import ABC, abstractmethod


class BaseStorage:
    @abstractmethod
    def create_bag(self):
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

    def create_bag(self):
        raise NotImplemented

    def get_bags(self):
        raise NotImplemented

    def get_bags_by_title(self):
        raise NotImplemented

    def update_bag(self):
        raise NotImplemented

    def delete_bag(self):
        raise NotImplemented


storage = MongoStorage()
