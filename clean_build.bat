@echo off
REM Clean up build artifacts and Python cache files for terminal-ai

REM Remove __pycache__ folders
for /d /r %%i in (__pycache__) do rmdir /s /q "%%i" 2>nul

REM Remove .pyc files
for /r %%i in (*.pyc) do del /q "%%i" 2>nul

REM Remove protai.egg-info folder
if exist protai.egg-info rmdir /s /q protai.egg-info 2>nul

REM Remove dist and build folders
if exist dist rmdir /s /q dist 2>nul
if exist build rmdir /s /q build 2>nul

REM Remove .pytest_cache folder
if exist .pytest_cache rmdir /s /q .pytest_cache 2>nul

REM Remove .mypy_cache folder
if exist .mypy_cache rmdir /s /q .mypy_cache 2>nul

REM Done
@echo Cleanup complete.