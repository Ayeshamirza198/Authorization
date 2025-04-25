from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Nested class for extra user info
class UserInfo(BaseModel):
    ip_address: str
    device: str

# Main request model including username, password, and nested UserInfo
class LoginData(BaseModel):
    username: str
    password: str
    user_info: UserInfo

@app.post("/register")
def login(data: LoginData):
    return {
        "message": "Login successful",
        "username": data.username,
        "ip": data.user_info.ip_address,
        "device": data.user_info.device
    }
{
  "username": "Ayesha",
  "password": "secure123",
  "user_info": {
    "ip_address": "192.168.1.10",
    "device": "Chrome on Windows"
  }
}