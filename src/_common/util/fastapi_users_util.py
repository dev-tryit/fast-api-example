from beanie import Document
from fastapi_users_db_beanie import BeanieBaseUser, BeanieUserDatabase
from passlib.handlers.bcrypt import bcrypt
from pymongo.client_session import ClientSession


class UserModel(BeanieBaseUser, Document):
    pass


class FastapiUsersUtil:

    async def get_user_db(self):
        yield BeanieUserDatabase(UserModel)

    def verify_password(self, plain_password, hashed_password):
        return bcrypt.verify(plain_password, hashed_password)

    async def authenticate_user(self, session: ClientSession, email: str, password: str):
        user = await UserModel.find(UserModel.email == email, session=session).first_or_none()

        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user
