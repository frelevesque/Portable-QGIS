# -*- coding: utf-8 -*-
__author__ = 'Frédéric Lévesque'
__version__ = '0.1'

import os, re
import shutil

def start_qgis():
    base_path = os.getcwd().replace('\\portable','').replace('/portable','')
    qgis_path = os.path.join(base_path, "qgis")

    """Check if LTR"""
    env_path = os.path.normpath('{0}/bin/qgis-ltr-bin-g7.env'.format(qgis_path))
    env_path_bak = env_path + '.bak'
    batch_path = os.path.normpath('{0}/bin/qgis-ltr-grass7.bat'.format(qgis_path))

    if not os.path.isfile(env_path):
        env_path = os.path.normpath('{0}/bin/qgis-bin-g7.env'.format(qgis_path))
        env_path_bak = env_path + '.bak'
        batch_path = os.path.normpath('{0}/bin/qgis-grass7.bat'.format(qgis_path))

    """Fait le back up de l'orginal si non disponible
    """
    if not os.path.isfile(env_path_bak):
        shutil.copy2(env_path, env_path_bak)

    """Remplace l'orignal par le back up
    utile si le dossier est déplacé
    """    
    if os.path.isfile(env_path_bak):
        shutil.copy2(env_path_bak, env_path)    

    """Lit le fichier environnement
    """
    with open(env_path, 'r') as f:
        lines = f.readlines()

    texte = ''.join(lines)

    """Pattern de recherche dans le ficher '.env' pour trouver la version et
    le chemin a remplacer
    """
    pattern_qgis = re.search("(?=[A-Z]:\\\)(.*?QGIS.*?\d\.\d*?)(?=\W)", texte)

    try:
        pattern_qgis = pattern_qgis.group()
        pattern_qgis_forward = pattern_qgis.replace('\\', '/')
        
    # Si pas de pattern correspondant
    except AttributeError:
        print(texte)
        exit()

    # Corrige les chemins ligne par ligne
    for inx, line in enumerate(lines):

        line = line.replace(pattern_qgis, qgis_path)
        line = line.replace(pattern_qgis_forward, qgis_path)
        
        # Uniformiser les /
        if '/' in line:
            line = line.replace('\\', '/')
            
        lines[inx] = line

    # Enregistre le nouveau fichier '.env' avec les bon chemin
    with open(env_path, 'w') as f:
        f.writelines(lines)

    # Démarre QGIS
    os.system(batch_path + ' --profiles-path ' + base_path)
    
if __name__ == "__main__":
    start_qgis()
