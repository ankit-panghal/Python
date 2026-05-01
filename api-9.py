from fastapi import FastAPI
import httpx
from pydantic import BaseModel, EmailStr #Daten Validation
from google import genai
from dotenv import load_dotenv
import os

app = FastAPI() #Erstelle den Server

'''@app.get('/users') #Wenn '/users' aufruft, fuhrt die Funktion darunter (users) aus
async def users():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            'https://api.freeapi.app/api/v1/public/randomusers'
        )
        daten = response.json()
        return daten'''


'''url1 = "https://api.freeapi.app/api/v1/users/register"
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}
class RegisterData(BaseModel):
    email: EmailStr
    password : str
    username : str
    role : str

class loginData(BaseModel):
   username : str
   password : str


#data.model_dump() Pydantic object → Python dictionary

@app.post('/register')
async def register(data:RegisterData):
    async with httpx.AsyncClient() as client:
        response = await client.post(url=url1,json=data.model_dump(),headers=headers)
        return response.json()
    

@app.get('/')
async def home():
    return {"nachricht" : 'Home Page'}


url2 = 'https://api.freeapi.app/api/v1/users/login'

@app.post('/login')
async def login(data:loginData):
    async with httpx.AsyncClient() as client:
        response = await client.post(url2,json=data.model_dump(),headers=headers)
        return response.json()'''

load_dotenv()
class Frage(BaseModel):
    frage : str

client =  genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.post('/chat')
async def chat(data:Frage):
     try:
      response = client.models.generate_content(
      model="gemini-3-flash-preview",contents=data.frage
      )
      return {
        "user_input" : data.frage,
        "llm_response" : response.candidates[0].content.parts[0].text
      }

     except Exception as e:
      return {"error" : str(e)}
    


