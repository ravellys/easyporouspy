import json
import os
from easyporouspy.io.input import import_file_path


def _create_dict(im):
    return {'shape': im.shape, 'im': " ".join(im.ravel().astype(str))}


class MetaImage:
    def __init__(self, name):
        self.origin_im_path = None
        self.im_dir = None
        self.name = name

    def create_dir(self, dir):
        path = os.path.join(dir, self.name)
        self.im_dir = path
        if os.path.isdir(path):  # vemos de este diretorio ja existe
            print('Ja existe uma pasta com esse nome!')
        else:
            os.mkdir(path)  # aqui criamos a pasta caso nao exista
            print('Pasta criada com sucesso!')

    def import_file_path(self, path):
        self.origin_im_path = path
        return import_file_path(path)

    def save_imjs(self, name, path_file):
        im = self.import_file_path(path_file)
        im_js = _create_dict(im)
        with open(os.path.join(self.im_dir, name), 'w') as outfile:
            json.dump(im_js, outfile)
        pass


