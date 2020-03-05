@echo off

SET BATCH_PATH=%~dp0

SET QGIS_ROOT=%BATCH_PATH%qgis

echo.
echo Quel module pip voulez-vous installer? Which module do you want to install?
set /P pip_package=

"%QGIS_ROOT%\apps\Python37\python.exe" -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org %pip_package%

echo.

timeout /t 15
