import numpy as np
from tifffile import tifffile


class Band:

    def __init__(self, filePath=None, npArray=None):
        if filePath is not None:
            self.__band = tifffile.imread(filePath)
        if npArray is not None:
            self.__band = npArray

        if np.all(self.__band == -1) or self.__band == []:
            self.__exist = False
        else:
            self.__exist = True


    def get_band(self): # solleva eccezione se la banda è inesistente
        if not self.get_existence():
            raise Exception("banda vuota!")

        return self.__band

    def get_flatten(self, mask=None):
        if mask is None:
            return self.__band.reshape(-1, 1)
        else:
            flattenBand = self.__band.reshape(-1, 1)
            return flattenBand[mask.get_mask()]

    def get_existence(self):
        return self.__exist