import numpy as np
from sklearn.model_selection import train_test_split


class Mask:

    def __init__(self, label):
        self.__mask = np.where(label != -1)
        self.__label = label[self.__mask]

    def get_mask(self):
        return self.__mask[0]

    def split(self, percentualSplit):
        X_train, X_test, y_train, y_test = train_test_split(self.get_mask(), self.get_mask(),
                                                            train_size=percentualSplit, random_state=42, stratify=self.__label)
        mask = [X_train, X_test]
        return mask
