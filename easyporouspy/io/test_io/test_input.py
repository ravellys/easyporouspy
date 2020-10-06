from easyporouspy.io.input import import_file_path


def test_import_file_path():

    path = "C:\Users\ravellys\PycharmProjects\easyporouspy\easyporouspy\file_test"
    im = import_file_path(path)
    print(im.shape)
