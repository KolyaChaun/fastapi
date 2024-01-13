from fastapi import FastAPI
from api import api_recipes
from web import web_recipes

app = FastAPI()
app.include_router(api_recipes.router)
app.include_router(web_recipes.router)


# @app.get('/')
# def root() -> dict:
#     return {'try': 'OK'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8500)
