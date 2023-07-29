import numpy as np

import Band
import IndexBuilder
import MutualInfo


class Image:

    def __init__(self):
        self.__tensor = []

    def set_band(self, Band, index=None):
        if index is None:
            self.__tensor.append(Band)
        else:
            self.__tensor.insert(index, Band)

    def get_band(self, index=None):
        return self.__tensor[index]

    def get_tensor(self):
        return self.__tensor

    def MI(self, label):
        flattenLable = label.get_flatten()
        mi = MutualInfo.MutualInfo(flattenLable)
        results = []  # lista contenente tutte le bande di cui calcoliamo i valori MI
        for band in self.get_tensor():
            if band.get_existence():     # verifica se la banda è tra quelle utilizzate
                flattenBand = band.get_flatten()  # crea la banda appiattita e senza pixels con valore = -1
                result = mi.compute(flattenBand)
            else:
                result = [0]
            results.append(result[0])

        return results

    def createIndexImage(self, indexes):
        # calcolo degli indici
        image = Image()  # immagine che conterrà tutti gli indici calcolati
        ib = IndexBuilder.IndexBuilder()
        i = 0
        for index in indexes:
            result = ib.compute(self, index)  # calcola indice passato in input
            tempBand = Band.Band(npArray=result)  # crea la banda con l'indice calcolato

            image.set_band(tempBand, i)  # la inserisce nell'immagine
            i += 1

        return image

    def get_dataset(self, mask):
        X_dataset = Image()
        emptyBand = Band.Band(npArray=-1 * np.ones(len(mask)).reshape(-1, 1))
        for band in self.get_tensor():
            if band.get_existence():
                band = Band.Band(npArray=band.get_band().flatten()[mask].reshape(-1, 1))
                X_dataset.set_band(band)    # aggiungo una matrice che contiene solo i valori della banda nelle posizioni indicate da mask
            else:
                X_dataset.set_band(emptyBand)
        return X_dataset
