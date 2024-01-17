from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from schemas import NewRecipesData, SavedRecipe

from storage import storage

templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix="", tags=["WEB", "Recipes"])


@router.get("/")
@router.post("/search")
def main_recipes(request: Request, search_param: str = Form(None)):
    if search_param:
        recipes = storage.get_recipe(search_param=search_param)
    else:
        recipes = storage.get_recipe(0, limit=10)
    context = {
        "request": request,
        "title": "Результати пошуку" if search_param else "Головна сторінка",
        "recipes": recipes,
    }
    return templates.TemplateResponse("index.html", context=context)


@router.get("/add_book")
def add_recipes_form(request: Request):
    context = {
        'request': request,
        'title': 'Створити нову книгу',
    }
    return templates.TemplateResponse('new_recipe.html', context=context)


@router.get("/about us")
def get_info_about_us(request: Request):
    context = {
        'request': request,
        'title': 'О нас',
    }
    return templates.TemplateResponse('about_us.html', context=context)


@router.post("/add_recipe")
def add_recipe(
        request: Request,
        title: str = Form(),
        cover: str = Form(),
        description: str = Form(),
):
    recipe = NewRecipesData(
        title=title,
        cover=cover,
        description=description,
    )
    saved_recipe = storage.create_recipe(recipe.model_dump())
    context = {
        "request": request,
        "title": "Новий рецепт",
        "recipes": [saved_recipe],
    }
    return templates.TemplateResponse("index.html", context=context)


@router.get('/book/{recipe_uuid}')
def recipe_info(request: Request, recipe_uuid: str):
    saved_recipe = storage.get_recipes_info(recipe_uuid)
    if saved_recipe:
        context = {
            'request': request,
            'title': f'Інформація про книгу {recipe_uuid}',
            'recipe': saved_recipe,
        }
        response = templates.TemplateResponse('details.html', context=context)
        return response

    context = {
        'request': request,
        'title': f'Інформація про книгу {recipe_uuid} не знайдено',
        'recipe': saved_recipe,
    }
    return templates.TemplateResponse('http404.html', context=context)
