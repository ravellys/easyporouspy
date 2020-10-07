import os

import pytest


@pytest.fixture(scope='module')
def path_env():
    path_env_ = r"../../environment_test/"
    if 'tests' == os.getcwd()[-5:]:
        path_env_ = r"../environment_test/"
    return path_env_
