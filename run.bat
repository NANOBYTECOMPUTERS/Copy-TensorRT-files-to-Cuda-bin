@echo off
echo Running Python script as administrator...
powershell -Command "& {Start-Process -FilePath 'python.exe' -ArgumentList '%~dp0copy_tenso_2_cuda.py' -Verb RunAs; $LastExitCode}"

if %errorlevel% equ 0 (
    echo Python script completed successfully.
) else (
    echo Error occurred while running the Python script.
)
echo.  & rem Echo a blank line for readability
echo Press any key to close...
pause >nul & rem Pause but hide the "Press any key to continue..." message
