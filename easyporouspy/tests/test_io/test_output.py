import os
from easyporouspy.metaimage.MetaImage import MetaImage


def test_path_exist(path_env):
    dir_ = path_env
    name = "meta_test"
    mim = MetaImage(name=name)
    mim.create_dir(dir_=dir_)
    assert os.path.isdir(os.path.join(dir_, name))


def test_save_im_js(path_env):
    dir_ = path_env
    name = "meta_test"
    mim = MetaImage(name=name)
    mim.create_dir(dir_=dir_)
    path = dir_ + 'file_test'
    name_file = 'im.json'
    mim.save_im_js(name=name_file, path_file=path)
    assert os.path.isfile(os.path.join(mim.mim_dir, name_file))
