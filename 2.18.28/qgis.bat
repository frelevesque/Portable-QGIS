REM This batch file make QGIS 2.x.x LTR portable on windows
REM config will be stored in QGIS 2.x.x/qgis/qgisconfig
REM options will be stored in QGIS 2.x.x/qgis/qgisoptions

@ECHO OFF

SET BATCH_PATH=%~d0

SET QGIS_ROOT=%BATCH_PATH%qgis

path %PATH%;%QGIS_ROOT%\apps\qgis\bin;%QGIS_ROOT%\apps;%QGIS_ROOT%\bin >nul
start "QGIS" /B %QGIS_ROOT%\bin\qgis-ltr-grass7.bat --configpath %QGIS_ROOT%\qgisconfig --optionspath %QGIS_ROOT%\qgisoptions >nul
@ECHO OFF
timeout /t 2

taskkill /f /im cmd.exe >nul
:exit
