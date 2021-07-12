import pandas as pd
import os
import shutil
import re
import urllib
import os
from os import listdir

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

