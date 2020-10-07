import json
import os

import numpy as np

from easyporouspy.io.input import import_file_path


def _create_dict(im):
    return {'shape': im.shape, 'im': " ".join(im.ravel().astype(str))}


class MetaImage:
    def __init__(self, name='im.json'):
        self.name = name

    def create_dir(self, dir_):
        path = os.path.join(dir_, self.name)
        self.mim_dir = path
        if os.path.isdir(path):  # vemos de este diretorio ja existe
            print('Ja existe uma pasta com esse nome!')
        else:
            os.mkdir(path)  # aqui criamos a pasta caso nao exista
            print('Pasta criada com sucesso!')

    def import_file_path(self, path):
        self.origin_im_path = path
        return import_file_path(path)

    def save_im_js(self, name, path_file):
        im = self.import_file_path(path_file)
        im_js = _create_dict(im)
        self.im_js = os.path.join(self.mim_dir, name)
        with open(self.im_js, 'w') as outfile:
            json.dump(im_js, outfile)

    def open_im_js(self):
        with open(self.im_js, 'r') as json_file:
            data = json.load(json_file)
            im = np.array(data['im'].split()).astype(int)
            return im.reshape(tuple(data['shape']))
