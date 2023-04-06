from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id = 1, name = "user1", surname = "surname1", url = "github.com", age = 25),
        User(id = 2, name = "user2", surname = "surname2", url = "github1.com", age = 26),
        User(id = 3,name = "user3", surname = "surname3", url = "github2.com", age = 27)]

@app.get("/users")
async def users():
    return users_list

#PATH
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
    
#QUERY    
@app.get("/user/")
async def user(id: int):
    return search_user(id)

#POST
@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"Error:" "El usuario ya existe"}
    else:
        users_list.append(user)

#PUT
@app.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"Error": "No se ha encontrado el usuario"}

#DELETE


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "No se ha encontrado el usuario"}


