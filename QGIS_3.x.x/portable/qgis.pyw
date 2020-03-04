# -*- coding: utf-8 -*-
__author__ = 'Frédéric Lévesque'
__version__ = '0.1'

import os, re
import shutil

base_path = os.getcwd().replace('\\portable','').replace('/portable','')
qgis_path = base_path + "\\qgis"

env_path = '{0}/qgis/bin/qgis-bin.env'.format(base_path)
env_path_bck = env_path + '.backup'

"""Fait le back up de l'orginal si non disponible
"""
if not os.path.isfile(env_path_bck):
    shutil.copy2(env_path, env_path_bck)

"""Remplace l'orignal par le back up
utile si le dossier est déplacé
"""    
if os.path.isfile(env_path_bck):
    shutil.copy2(env_path_bck, env_path)    

with open(env_path, 'r') as f:
    lines = f.readlines()

texte = ''.join(lines)
pattern_qgis = re.search("(?=[A-Z]:\\\)(.*?QGIS.*?\d\.\d*?)(?=\W)", texte)

try:
    pattern_qgis = pattern_qgis.group()
    pattern_qgis_forward = pattern_qgis.replace('\\', '/')
except AttributeError:
    print(texte)
    exit()

print(base_path)
print(pattern_qgis)
print(pattern_qgis_forward)

env_nouveau = []

for line in lines:
    line = line.replace(pattern_qgis, qgis_path)
    line = line.replace(pattern_qgis_forward, qgis_path)
    if '/' in line:
        line = line.replace('\\', '/')
        
    env_nouveau.append(line)

print(env_nouveau)

with open(env_path, 'w') as f:
    f.writelines(env_nouveau)

os.system(qgis_path + '/bin/qgis.bat --profiles-path ' + base_path)
