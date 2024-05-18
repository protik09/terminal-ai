@echo off
:: Sets folder to folder that the batch file is running from
set "FOLDER=%~dp0"
echo Folder set to %FOLDER%
:: Recursively iterate through all folders in the project to find the venv
for /r "%FOLDER%" %%f in (.) do (
    if exist "%%f\Activate.ps1" (
        @REM echo python venv found in %%f
        cd /d "%%f"
        :: Check if running in CMD or Powershell
        if /i "%comspec%" equ "%SystemRoot%\system32\cmd.exe" (
            @REM echo Running batch file from CMD
            call activate
        ) else (
            echo Running batch file from powershell
            echo run activate_venv.ps1 instead.
        )
        exit /b
    )
)
:: If no venv found, create a new one and install requirements
if not exist "%FOLDER%\.venv" (
    echo No Python venv found. Creating a new one...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    echo Installing Python requirements...
    pip install -r requirements.txt
    echo Python venv created and requirements installed.
)