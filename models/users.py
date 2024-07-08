from pydantic import BaseModel, EmailStr

class UserInDB(BaseModel):
    email: EmailStr
    name: str
    hashed_password: str = None

