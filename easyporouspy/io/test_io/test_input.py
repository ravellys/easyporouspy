from easyporouspy.io.input import import_file_path
from easyporouspy.metaimage.metaimage import MetaImage


def test_import_file_path():
    path = "C:\\Users\\ravellys\\PycharmProjects\\easyporouspy\\easyporouspy\\io\\file_test"
    im = import_file_path(path)
    assert im.shape == (11, 840, 840)


def test_import_file_with_metaimage():
    dir = "C:\\Users\\ravellys\\PycharmProjects\\easyporouspy\\easyporouspy\\metaimage\\test_metaimage\\ambiente_test"
    name = "meta_test"
    mim = MetaImage(name=name)
    mim.create_dir(dir=dir)
    path = "C:\\Users\\ravellys\\PycharmProjects\\easyporouspy\\easyporouspy\\io\\file_test"
    im = mim.import_file_path(path)
    assert im.shape == (11, 840, 840)

