from enum import Enum


class TypesOfRecipes(str, Enum):
    FIRST_MEAL = 'First meal'
    SECOND_MEAL = 'Second meal'
    SALAD = 'Salad'
    SNACKS = 'Snacks'
    DESSERTS = 'Desserts'
    SWEET_PASTRIES = 'Sweet pastries'
    SAUCE = 'Sauce'
    OTHER = 'Other'
