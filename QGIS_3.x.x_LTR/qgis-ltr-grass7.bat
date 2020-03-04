@ECHO OFF
REM This batch file make QGIS 3.x.x portable on windows
REM Config will be stored in QGIS 3.x.x/profiles/
REM The batch file calls a Python script that correct the path each time QGIS is started via the batch file

SET BATCH_PATH=%~dp0

SET QGIS_ROOT=%BATCH_PATH%qgis

"%QGIS_ROOT%\apps\Python37\pythonw.exe" %BATCH_PATH%portable\qgis-ltr-grass7.pyw

timeout /t 3

taskkill /f /im cmd.exe >nul
