import os

from easyporouspy.io.input import import_file_path
from easyporouspy.metaimage.MetaImage import MetaImage


def test_import_file_path():
    path = r"../../environment_test/file_test"
    im = import_file_path(path)
    assert im.shape == (11, 840, 840)


def test_import_file_with_metaimage():
    dir = r"../../environment_test"
    name = "meta_test"
    mim = MetaImage(name=name)
    mim.create_dir(dir=dir)
    path = r"../../environment_test/file_test"
    im = mim.import_file_path(path)
    assert mim.mim_dir == os.path.join(dir, name)
    assert im.shape == (11, 840, 840)


def test_input_imjs_asarray():
    dir = r"../../environment_test"
    name = "meta_test"
    mim = MetaImage(name=name)
    mim.create_dir(dir=dir)
    path = r"../../environment_test/file_test"
    name_file = 'im.json'
    mim.save_im_js(name=name_file, path_file=path)
    im = mim.open_im_js()
    assert im.shape == (11, 840, 840)
