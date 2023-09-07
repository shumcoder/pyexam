from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    list = [1,2,3]

    return {"item_id": list}

@app.get("/items/{id1}/{id2}")
async def read_item(id1: int,id2: int):
    sum = id1 + id2

    return {"item_id": sum}

# git remote add origin https://[TOKEN]@github.com/[REPO-OWNER]/[REPO-NAME]
# git remote add origin https://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@github.com/shumcoder/pyexam.git