from enum import Enum


class MyEnvironment(Enum):
    local = 0,
    dev = 1,
    qa = 2,
    prod = 3,
