import csv
import pandas as pd
from collections import OrderedDict
import numpy as np
import tifffile
from tifffile import imwrite
import os
import openpyxl



def valid_max(parameter):
    Max = 0
    for key in valid_trebic_dataset.keys():
        m=max(valid_trebic_dataset[key][parameter])
        if Max < m:
            Max = m

    return Max

def valid_min(parameter):
    Min = np.inf #valid_trebic_dataset[1][parameter][0]
    for key in valid_trebic_dataset.keys():
        m=min(valid_trebic_dataset[key][parameter])
        if Min > m:
            Min = m

    return Min

def fix_coordinates(Min, parameter):
    for key in valid_trebic_dataset.keys():
        temp = ()
        for coordinate in valid_trebic_dataset[key][parameter]:
            new_coordinate = coordinate - Min + 1
            temp = tuple(list(temp) + [new_coordinate])
        valid_trebic_dataset[key][parameter] = temp

def create_dataset_file():
    with open('Trebic_dataset.csv', mode='w', newline='') as File:
        writer = csv.writer(File)

        for key in valid_trebic_dataset.keys():
            for x, y, lat, lon in zip(valid_trebic_dataset[key][0], valid_trebic_dataset[key][1],
                                      valid_trebic_dataset[key][2], valid_trebic_dataset[key][3]):
                string = key, x, y, lat, lon
                writer.writerow(string)
            writer.writerow(" ")
    File.close()

def load_class_lable():
    matrix = -1 * np.ones((maxX - minX + 1, maxY - minY + 1))
    for key in valid_trebic_dataset.keys():
        i = 0
        while id[i] != key:
            i += 1
        for x, y in zip(valid_trebic_dataset[key][0], valid_trebic_dataset[key][1]):
            matrix[x-1, y-1] = class_lable[i]
            i += 1

    return matrix

def load_pixels():
    matrix = -1 * np.ones((maxX - minX + 1, maxY - minY + 1))
    for key in valid_trebic_dataset.keys():
        i = 0
        while id[i] != key:
            i += 1
        for x, y in zip(valid_trebic_dataset[key][0], valid_trebic_dataset[key][1]):
            matrix[x-1, y-1] = pixels[i] * 10000
            i += 1

    return matrix



# 1. prende dal Tab B2 la colonna degli id e della classe
exFile = pd.read_excel('data_Sentinel2_Barta.xlsx', sheet_name='B2')
id = exFile.loc[:, 'ID in spapefile']     # prende la colonna degli id dei poligoni
class_lable = exFile.iloc[:, 1]      # prende la colonna delle classi

# 2. estrae dal punto precedente una lista con gli id senza ripetizioni
polygons_id = list(OrderedDict.fromkeys(id))   #lista senza id duplicati

# 3. caricare Trebic1_4_8_20.txt all'interno di un dizionario
#    con chive = poligono, valore = array di tuple con X,Y,lon,lat
with open('Trebic1_4_8_20m.txt', mode='r') as File:
    trebic_dataset = {}
    polygon = 0  # valore
    X = ()
    Y = ()
    Lat = ()
    Lon = ()

    File.readline() #salto la prima riga
    for row in File:
        if len(row.strip()) != 0:   #se la riga è vuota aggiungo i valori nelle tuple
            temp = row.strip().split()
            X = tuple(list(X) + [int(temp[1])])
            Y = tuple(list(Y) + [int(temp[2])])
            Lat = tuple(list(Lat) + [float(temp[5])])
            Lon = tuple(list(Lon) + [float(temp[6])])

        else:   #altrimenti inserisco nell'array le tuple ed inserisco nel dizionario l'array ed il poligono attuale
            values = []     # chiave
            values.append(X)
            values.append(Y)
            values.append(Lat)
            values.append(Lon)

            polygon += 1    #valore
            trebic_dataset[polygon] = values

            X = ()
            Y = ()
            Lat = ()
            Lon = ()

File.close()

# 4. crea una copia del dizionario del punto precedente in cui appaiono
#    solo le coppie chiave,valore dei poligoni presenti in 'polygons_id'
valid_trebic_dataset = {}

for key in trebic_dataset:
    if key in polygons_id:
        valid_trebic_dataset[key] = trebic_dataset[key]

# 5-6. calcola il minimo e massimo di X e Y utilizzando tutti i poligoni presenti
#      nel dizionario creato al punto 4
maxX = valid_max(0) #la tupla [0] contiene X
maxY = valid_max(1) #la tupla [1] contiene Y
minX = valid_min(0)
minY = valid_min(1)

# 7-8. trasformare tutte le X e Y al punto 4 in (X-minX+1) ed (Y-minY+1)
fix_coordinates(minX, 0)
fix_coordinates(minY, 1)

# 9. salva il dizionario in un file.csv
create_dataset_file()

# 10. Crea la matrice "class_image" con dimensione (MaxX-minX+1) x (MaxY-minY+1) dove vengono
#     inserite le class label e crea il file tiff
class_image = load_class_lable()
imwrite('class_image.tif', class_image)

# Per ogni time stamp
sheets = ['B2','B3','B4','B5','B6','B7','B8A','B11','B12']
time_stamps = [101, 111, 126, 151, 181, 221, 231, 241, 256, 261, 271, 286, 291, 321]

for time_stamp in time_stamps:
    directory = str(time_stamp)   #crea la cartella del timestep
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Per ogni tab
    for sheet in sheets:
        # 1. carica dall'attuale tab la colonna del time stamp.
        exFile = pd.read_excel('data_Sentinel2_Barta.xlsx', sheet_name=sheet)
        pixels = exFile.loc[:, time_stamp]

        # 2. Crea una matrice "matrix" di dimensione (MaxX-MinX+1) x (MaxY-MinY+1) in cui inserisce i pixels
        #   nelle relative posizioni X e Y dal dizionario dello step 4
        matrix = load_pixels()

        # 3. creara il file tiff della matrice nella cartella "\timestamp\banda_tamestamp.tiff"
        filename = str(sheet) + "_" + str(time_stamp) + '.tif'
        file_path = str(time_stamp) + "/" + filename
        tifffile.imwrite(file_path, matrix)

#Crea una banda vuota
matrix = -1 * np.ones((maxX - minX + 1, maxY - minY + 1))
tifffile.imwrite('empty_band.tif', matrix)

