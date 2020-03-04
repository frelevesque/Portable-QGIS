# -*- coding: utf-8 -*-
__author__ = 'Frédéric Lévesque'
__version__ = '0.1'

import os, re
import shutil

def start_qgis():
    # Get the main portable QGIS folder
    base_path = os.path.dirname(os.getcwd())

    # Assign the QGIS files path
    qgis_path = os.path.join(base_path, "qgis")

    # Assign the path to qgis-bin.env file where path are written
    env_path = '{0}/qgis/bin/qgis-ltr-bin.env'.format(base_path)
    # Assign the path of the backup of the qgis-bin.env file
    env_path_bck = env_path + '.bak'



    """Fait le back up de l'orginal si non disponible
    """
    if not os.path.isfile(env_path_bck):
        shutil.copy2(env_path, env_path_bck)

    """Remplace l'orignal par le back up
    utile si le dossier est déplacé
    """    
    if os.path.isfile(env_path_bck):
        shutil.copy2(env_path_bck, env_path)    

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
        
        # uniformiser les /
        if '/' in line:
            line = line.replace('\\', '/')
            
        lines[inx] = line

    # enregistre le nouveau fichier '.env' avec les bon chemin
    with open(env_path, 'w') as f:
        f.writelines(lines)

    # Démarre QGIS
    os.system(qgis_path + '/bin/qgis-ltr.bat --profiles-path ' + base_path)
    
if __name__ == "__main__":
    start_qgis()
