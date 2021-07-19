import pandas as pd
import shutil
import re
import urllib
from os import listdir
from PIL import Image
import os
import PIL
import glob

persons = []

def listar_arquivos(caminho=None):
    lista_arqs = [arq for arq in listdir(caminho)]
    return lista_arqs

def readXlsx():
  read_file = pd.read_excel('Plan1.xlsx')
  read_file.to_csv('alunos.csv', index = None, header = True)

def readCsv():
  read_file = open('alunos.csv', 'r')
  
  for row in read_file:
    row = row.replace('\n', '')
    row = row.split(',')
    persons.append(row)

  read_file.close()

readXlsx()
readCsv()

caminhos = open('file_list.txt', 'r')

for caminho in caminhos:
  caminho = caminho.replace('\n', '')
  arquivos = listar_arquivos(caminho)

  for arquivo in arquivos:
    arq = arquivo.split('.')[0]

    for person in persons:
      if arq == person[1]:
        os.rename(caminho + '/' + arq +'.jpg', caminho + '/' + person[0] +'.jpg')
        fixed_height = 120
        image = Image.open(caminho + '/' + person[0] +'.jpg')
        height_percent = (fixed_height / float(image.size[1]))
        width_size = int((float(image.size[0]) * float(height_percent)))
        image = image.resize((width_size, fixed_height), PIL.Image.NEAREST)
        image.save(caminho + '/' + person[0] +'.jpg')

