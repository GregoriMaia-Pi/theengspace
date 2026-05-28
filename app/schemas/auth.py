from pydantic import BaseModel, constr


class UserRegister(BaseModel):
    username: constr(strip_whitespace=True, min_length=1, max_length=64)
    password: constr(min_length=6, max_length=6, pattern=r'^\d{6}$')


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    created_at: str

    class Config:
        from_attributes = True
