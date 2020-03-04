1) Create a folder for your portable QGIS, i.e "QGIS_2.18.28"

2) In this folder add the batch file (qgis.bat) and create a folder "qgis"

3) Place the content of C:/Program Files (x86 or x64)/QGIS 2.18/ in the ".../QGIS_2.18.28/qgis/" directory

4) Now you should have something like this

+-- /QGIS_2.18.28/
    +-- qgis.bat
    +-- qgis/
        +-- apps/
            +-- (bunch of files and folders)
        +-- bin/
            +-- (bunch of files and folders)
        +-- etc/
            +-- (bunch of files and folders)
        +-- icons/
            +-- (bunch of files and folders)
        +-- include/
            +-- (bunch of files and folders)
        +-- qgisconfig/ (after first run)
            +-- (bunch of files and folders)
        +-- qgisoptions/ (after first run)
            +-- (folder with ini file)
        +-- share/
            +-- (bunch of files and folders)
        +-- msvcp110.dll
        +-- ~8 other files

5) start qgis.bat by clicking on it. QGIS will start.
