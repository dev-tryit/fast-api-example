import os

import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin._auth_utils import UserNotFoundError

from _common.decorator.singleton import singleton
from _common.exception.my_api_exception import MyApiException
from _common.util.path_util import PathUtil


@singleton
class FirebaseAdminUtil:

    def init(self):
        service_account_path = os.path.join(PathUtil().get_project_path(), 'ringdoc-service-account-key.json')

        cred = credentials.Certificate(service_account_path)
        self.app = firebase_admin.initialize_app(cred)

    def get_uid_by_firebase_token(self, firebase_token: str):
        try:
            decoded_token = auth.verify_id_token(firebase_token)
            uid = decoded_token['uid']
            return uid
        except:
            # 토큰이 유효하지 않거나 만료된 경우
            return None

    def set_claims_for_firebase_user(self, uid: str, new_firebase_claims: dict):
        try:
            auth.set_custom_user_claims(uid, new_firebase_claims)
        except UserNotFoundError as e:
            raise MyApiException(status_code=404, detail=e.default_message)
