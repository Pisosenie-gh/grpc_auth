from pydantic import BaseModel, EmailStr, constr, validator

from utils.password import pwd_context


class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class LoginPasswordValidator(BaseModel):
    password: str
    db_password: str

    @validator('password')
    def validate_password(cls, value, values):
        if 'db_password' in values and not pwd_context.verify(value, values['db_password']):
            raise ValueError('Passwords do not match.')
        return value
