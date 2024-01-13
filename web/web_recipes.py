from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from storage import storage

templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix='',
    tags=['WEB', 'Recipes']
)


@router.get('/')
def index(request: Request):
    recipes = storage.get_recipe(0, limit=10)
    context = {
        'request': request,
        'page': 'page 1',
        'title': 'first page',
        'recipes': recipes
    }
    return templates.TemplateResponse('index.html', context=context)


@router.get('/second')
def index(request: Request):
    context = {
        'request': request,
        'page': 'page 2',
        'title': 'second page'
    }
    return templates.TemplateResponse('index.html', context=context)
