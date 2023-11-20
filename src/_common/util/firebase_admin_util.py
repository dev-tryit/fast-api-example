import os

import firebase_admin
from firebase_admin import credentials, auth

from _common.decorator.singleton import singleton
from _common.util.path_util import PathUtil


@singleton
class FirebaseAdminUtil:
    def __init__(self):
        self.app = None

    def init(self):
        service_account_path = os.path.join(PathUtil().get_project_path(), 'ringdoc-service-account-key.json')

        cred = credentials.Certificate(service_account_path)
        self.app = firebase_admin.initialize_app(cred)

    def get_auth(self):
        return auth
