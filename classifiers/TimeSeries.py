import numpy as np
import pandas as pd

import Label
import MutualInfo


class TimeSeries:

    def __init__(self):
        self.__timeSeries = []
        self.label = 0
        self.mask = 0

    def add_image(self, image):
        self.__timeSeries.append(image)

    def set_label(self, label):
        self.label = label

    def set_mask(self, mask):
        self.mask = mask

    def concatenate(self, index):
        concatenation = []  # lista contenente le bande appiattite da concatenare
        for tensor in self.get_images():    # per ogni immagine
            if not tensor.get_band(index).get_existence():
                return [0]  # in tal caso interrompe il ciclo e restituisce 0
            band = tensor.get_band(index).get_flatten()  # prende la banda nel relativo index e la appiattisce
            concatenation.append(band)  # altrimenti la aggiunge tra le bande da concatenare

        concatenateBands = np.concatenate(concatenation, axis=0)    # effettua la concatenazione
        return concatenateBands

    def MI(self, index=None):
        if index is None:
            miResults = []  # lista contenente tutti i risultati di ogni concatenazione tra le bande
            i = 0
            while i < len(self.get_image(0).get_tensor()):  # esegue per ogni banda
                result = self.MI(i)
                miResults.append(result)
                i += 1

            return miResults
        else:
            concatenateBands = self.concatenate(index)  #concatena la banda nel relativo index
                                                        # con la stessa banda in time stamp differenti
            if len(concatenateBands) > 1:   # verifica che non sia una banda inutilizzata
                concatenateLabel = self.replicateLabel()    #concatena la stessa label con se stessa
                                                            # per tante volte quanti sono i time stamp
                mi = MutualInfo.MutualInfo(concatenateLabel)
                result = mi.compute(concatenateBands)   # calcola il valore di MI sulla concatenazione
                return result[0]
            else:
                return 0    # altrimenti restituisce solo 0

    def get_label(self):
        return self.label

    def get_image(self, index):
        return self.__timeSeries[index]

    def get_images(self):
        return self.__timeSeries

    def replicateLabel(self):
        flattenLabel = self.label.get_flatten()
        concatenation = []  # lista contenente le label da concatenare
        i = 0
        while i < len(self.__timeSeries):
            concatenation.append(flattenLabel)  # aggiunge alla lista la label appiattita con la mask applicata
            i += 1

        concatenateLabel = np.concatenate(concatenation, axis=0)
        return concatenateLabel

    def createIndexTimeSeries(self, indexes):
        images = TimeSeries()
        for image in self.get_images():
            images.add_image(image.createIndexImage(indexes))

        return images

    def get_dataset(self, mask):
        X_dataset = TimeSeries()
        for image in self.get_images():     # per ogni immagine, ricavo i pixel di train o test set da ciascuna delle sue bande o indici
            X_result = image.get_dataset(mask)
            X_dataset.add_image(X_result)

        # divido il target in train o test set
        y_dataset = Label.Label(npArray=self.get_label().get_label().reshape(-1, 1).ravel()[mask])

        return X_dataset, y_dataset




