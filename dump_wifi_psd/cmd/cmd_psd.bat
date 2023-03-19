@ECHO OFF

TITLE My System Info

ECHO Please wait... Gathering system information.

ECHO =========================

for /f "skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profiles') do @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear

:: or you can type this- > Netsh wlan show profile name=”Wi-F name” key=clear