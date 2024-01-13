from fastapi import APIRouter, status
from pydantic import BaseModel, Field
import constants
from storage import storage

router = APIRouter(
    prefix='/api/recipes',
    tags=['API', 'Recipes']
)


class NewRecipesData(BaseModel):
    title: str = Field(min_length=3, examples=['Recipe name'])
    cover: str
    tags: list[constants.TypesOfRecipes] = []
    description: str = None


class SavedRecipe(NewRecipesData):
    uuid: str = Field(examples=['9a7d8328-542d-437a-9ccb-fcff0eddd3b0'])


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_recipe(recipe: NewRecipesData) -> SavedRecipe:
    saved_recipe = storage.create_recipe(recipe.model_dump())
    return saved_recipe


@router.get('/')
def get_recipes(search_param: str = None, skip: int = 0, limit: int = 10) -> list[SavedRecipe]:
    recipes = storage.get_recipe(skip, limit, search_param)
    result = []

    for recipe in recipes:
        instance = SavedRecipe(
                **{'title': recipe['title'], 'cover': recipe['cover'], 'tags': recipe['tags'],
                    'description': recipe['description'], 'uuid': recipe['uuid']})
        result.append(instance)
    return result


# @router.get('/')
# def get_recipes_by_title() -> list[dict]:
#     pass


@router.patch('/update/{recipe_id}')
def update_recipe(recipe_id: str, description: str):
    storage.update_recipe(recipe_id, description)
    return {'result': 'OK'}


@router.delete('/delete/{recipe_id}')
def delete_recipe(recipe_id: str):
    storage.delete_recipe(recipe_id)
    return {'deleted': 'OK'}
