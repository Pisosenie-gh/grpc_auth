from pydantic import BaseModel, EmailStr, constr, validator


class UserBase(BaseModel):
    id: int


class UserCreate(BaseModel):
    name: constr(min_length=1)
    email: EmailStr
    password: constr(min_length=6)


class UserUpdate(UserBase):
    name: constr(min_length=1)
    email: EmailStr


class ChangePassword(UserBase):
    old_password: constr(min_length=6)
    new_password: constr(min_length=6)

    @validator('new_password')
    def validate_password_complexity_and_match(cls, value, values):
        min_length = 8
        errors = ''
        if len(value) < min_length:
            errors += 'Password must be at least 8 characters long. '
        if not any(character.islower() for character in value):
            errors += 'Password should contain at least one lowercase character. '
        if not any(character.isupper() for character in value):
            errors += 'Password should contain at least one uppercase character. '
        if not any(character.isdigit() for character in value):
            errors += 'Password should contain at least one digit. '
        if not any(character in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for character in value):
            errors += 'Password should contain at least one special character. '
        if 'new_password' in values and value != values['new_password']:
            raise ValueError('Passwords do not match.')
        if errors:
            raise ValueError(errors)
        return value


class UserDelete(UserBase):
    ...


class UserGet(UserBase):
    ...
