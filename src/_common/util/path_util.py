import os

from _common.decorator.singleton import singleton


@singleton
class PathUtil:
    def __init__(self):
        self.project_path = None

    def get_current_path(self, *, file):
        return os.path.dirname(os.path.abspath(file))

    def get_project_path(self):
        return self.project_path

    def set_project_path(self, *, main_file):
        self.project_path = self.get_current_path(file=main_file)
