from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root() -> dict:
    return {'try': 'OK'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8500)
