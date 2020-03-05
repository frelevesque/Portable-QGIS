1) Create a folder for your portable QGIS, i.e "QGIS_3.10.3_LTR";

2) In this folder add the batch files (qgis-ltr.bat qgis-ltr-grass7.bat) and create a folder "qgis";

3) Still in "QGIS_3.10.3" folder create a folder name "portable" and add to phyton file (qgis-ltr.pyw qgis-ltr-grass7.pyw) to this folder;

4) Place the content of C:/Program Files (x86 or x64)/QGIS 3.10/ in the ".../QGIS_3.10.3_LTR/qgis/" directory;

5) Now you should have something like this:

+-- /QGIS_3.10.3_LTR/
    +-- qgis-ltr.bat
    +-- qgis-ltr-grass7.bat
    +-- portable/
        +-- qgis-ltr.pyw
        +-- qgis-ltr-grass7.pyw
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

6) Start qgis-ltr.bat or qgis-ltr-grass7.bat by clicking on it. QGIS will start.
