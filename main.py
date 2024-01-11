from fastapi import FastAPI
from api import api_bags

app = FastAPI()
app.include_router(api_bags.router)


@app.get('/')
def root() -> dict:
    return {'try': 'OK'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8500)
