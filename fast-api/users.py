from  fastapi import FastAPI
from pydantic import BaseModel
#Api  para usuarios!"




app = FastAPI()

#entidad user

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int
    
users_list =  [User("edwin","gallego","https://www.emgb.dev",41),
               User("mauricio","brown","https://www.emgb.dev",42),
               User("diana","panesso","https://www.dcpa.dev",43)]  

@app.get("/usersjson")
async def usersjson():
    return[ {"name":"edwin", "surname":"gallego","url": "https://www.emgb.dev","age":30},
           {"name":"mauricio", "surname":"brown","url": "https://www.emgb.dev", "age":45}]



@app.get("/users")
async def users():
    return users_list