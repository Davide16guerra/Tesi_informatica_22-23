import numpy as np
from tifffile import tifffile


class Label:

    def __init__(self, filePath=None, npArray=None):
        if filePath is not None:
            self.__label = tifffile.imread(filePath)
        if npArray is not None:
            self.__label = npArray

    def get_label(self):
        return self.__label

    def get_flatten(self, mask=None):
        if mask is None:
            return self.__label.reshape(-1)
        else:
            flattenLabel = self.__label.reshape(-1)
            return flattenLabel[mask.get_mask()]
