import json
import os

import numpy as np

from easyporouspy.metaimage.metaimage import _create_dict


class SegmentationGeneric:
    def __init__(self, mim):
        self.mim = mim
        self.dir = os.path.join(mim.mim_dir, 'segmentation')
        self.create_dir()
        self.seg_im_lim = os.path.join(self.dir, 'im_lim_seg.json')

    def threshold(self, lim):
        self.thrs = lim
        return lim

    def limiar_segmentation(self):
        im = self.mim.open_im_js()
        im = im <= self.thrs
        im_js = _create_dict(im.astype(int))
        with open(self.seg_im_lim, 'w') as outfile:
            json.dump(im_js, outfile)

    def create_dir(self):
        path = self.dir
        if os.path.isdir(path):  # vemos de este diretorio ja existe
            print('Ja existe uma pasta com esse nome!')
        else:
            os.mkdir(path)  # aqui criamos a pasta caso nao exista
            print('Pasta criada com sucesso!')

    def open_im_js(self, im_file):
        with open(im_file, 'r') as json_file:
            data = json.load(json_file)
            im = np.array(data['im'].split()).astype(int)
            return im.reshape(tuple(data['shape']))