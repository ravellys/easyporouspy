import os
from easyporouspy.metaimage.MetaImage import MetaImage


def test_path_exist():
    dir = r"../../environment_test"
    name = "meta_test"
    mim = MetaImage(name=name)
    mim.create_dir(dir=dir)
    assert os.path.isdir(os.path.join(dir, name))


def test_save_im_js():
    dir = r"../../environment_test"
    name = "meta_test"
    mim = MetaImage(name=name)
    mim.create_dir(dir=dir)
    path = r"../../environment_test/file_test"
    name_file = 'im.json'
    mim.save_im_js(name=name_file, path_file=path)
    assert os.path.isfile(os.path.join(mim.mim_dir, name_file))
