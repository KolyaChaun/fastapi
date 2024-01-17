from fastapi import APIRouter, status

from storage import storage
from schemas import NewRecipesData, SavedRecipe

router = APIRouter(prefix="/api/recipes", tags=["API", "Recipes"])


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_recipe(recipe: NewRecipesData) -> SavedRecipe:
    saved_recipe = storage.create_recipe(recipe.model_dump())
    return saved_recipe


@router.get("/")
def get_recipes(
    search_param: str = None, skip: int = 0, limit: int = 10
) -> list[SavedRecipe]:
    recipes = storage.get_recipe(skip, limit, search_param)
    result = []

    for recipe in recipes:
        instance = SavedRecipe(
            **{
                "title": recipe["title"],
                "cover": recipe["cover"],
                "tags": recipe["tags"],
                "description": recipe["description"],
                "uuid": recipe["uuid"],
            }
        )
        result.append(instance)
    return result


@router.patch("/update/{recipe_id}")
def update_recipe(recipe_id: str, description: str):
    storage.update_recipe(recipe_id, description)
    return {"result": "OK"}


@router.delete("/delete/{recipe_id}")
def delete_recipe(recipe_id: str):
    storage.delete_recipe(recipe_id)
    return {"deleted": "OK"}
