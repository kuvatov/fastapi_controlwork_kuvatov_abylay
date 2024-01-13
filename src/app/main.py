from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def get_hello():
    return {'Hello': 'World'}


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', )
    