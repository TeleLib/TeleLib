import os


def generator_path(path):
    return os.path.realpath(
        os.path.dirname(__file__) + '/../generated/' + path
    )
