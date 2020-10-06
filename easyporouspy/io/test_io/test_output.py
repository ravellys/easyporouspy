import os
from easyporouspy.metaimage.metaimage import MetaImage


def test_path_exist():
    dir = "C:\\Users\\ravellys\\PycharmProjects\\easyporouspy\\easyporouspy\\metaimage\\test_metaimage\\ambiente_test"
    name = "meta_test"
    mim = MetaImage(name=name)
    mim.create_dir(dir=dir)
    assert os.path.isdir(os.path.join(dir, name))


def test_save_imjs():
    dir = "C:\\Users\\ravellys\\PycharmProjects\\easyporouspy\\easyporouspy\\metaimage\\test_metaimage\\ambiente_test"
    name = "meta_test"
    mim = MetaImage(name=name)
    mim.create_dir(dir=dir)
    path = "C:\\Users\\ravellys\\PycharmProjects\\easyporouspy\\easyporouspy\\io\\file_test"
    name_file = 'im.json'
    mim.save_im_js(name=name_file, path_file=path)
    assert os.path.isfile(os.path.join(mim.mim_dir, name_file))
