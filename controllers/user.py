import grpc

from models.users import User as UserModel
from sqlalchemy import or_
from grpc import ServicerContext as context
from config.database import get_db
from utils.password import get_password_hash, pwd_context


class UserController(object):
    db = next(get_db())

    def get_user_by_email(self, email: str) -> UserModel:
        if db_user := self.db.query(UserModel).filter(UserModel.email == email).first():
            return db_user

    def get_user_by_id(self, id: str) -> UserModel:
        if db_user := self.db.query(UserModel).filter(UserModel.id == int(id)).first():
            return db_user
        context.abort(grpc.StatusCode.NOT_FOUND, "User not found")

    def get_user(self, email: str, id: str) -> UserModel:
        if db_user := self.db.query(UserModel).filter(
                or_(UserModel.id == int(id), UserModel.email == email)).first():
            return db_user
        context.abort(grpc.StatusCode.NOT_FOUND, "User not found")

    def create_user(self, name: str, email: str, password: str) -> UserModel:
        hashed_password = get_password_hash(password)
        db_user = UserModel(name=name, email=email, password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, id: str, email: str, name: str) -> UserModel:
        db_user = self.get_user_by_id(id)
        db_user.name = name
        db_user.email = email

        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def change_password(self, id: str, new_password: str, old_password: str) -> None:
        db_user = self.get_user_by_id(id)
        if not pwd_context.verify(old_password, db_user.password):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Old password is incorrect")

        db_user.password = get_password_hash(new_password)
        self.db.commit()

    def delete_user(self, id: str) -> None:
        db_user = self.get_user_by_id(id)
        self.db.delete(db_user)
        self.db.commit()
