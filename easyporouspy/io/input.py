import os

import imageio
import numpy as np
from tqdm import tqdm


def import_file_path(path):
    """
    Importa conjunto de arquivos de uma pasta e cria um array 3D
    :param path:
    :return: numpy array
    """

    list_files = os.listdir(path)  # lista de arquivos dentro da pasta das amostras
    list_files = np.sort(np.array(list_files))  # organizar os arquivos
    im = []  # inicialização do vetor de armazenamento

    for file in tqdm(list_files) :
        fetch_file = os.path.join(path, file)
        image = np.array(imageio.imread(fetch_file))  # importa imagem e converte em numpy

        im.append(image.T)  # Adiciona matriz numpy ao vetor de armazenameto

    im = np.array(im)
    return im


if __name__ == '__main__':
    print(os.getcwd())
