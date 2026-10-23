# we will use a fast api framework here
from fastapi import FastAPI
from system_utils import get_system_details


app = FastAPI(title = "Devops Utilities API")

@app.get("/hello")
def hello():
    return{"message" : "Hello Dosto, Welcome to the Jungle API"}


@app.get("/metrics")
def metrics():
    '''This api shows the memory of system and informations'''  #this ''' makes documentation 
    return get_system_details()

