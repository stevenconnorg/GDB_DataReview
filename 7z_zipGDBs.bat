:: download 7zip to use this batch file
:: make sure 7z zip is added to the environment variables as specified below
:: or set path accordingly

set PATH=%PATH%;C:\Program Files\7-Zip\
echo %PATH%

:: Set working PathDirectory accordingly
set PathDir=C:\Users\stevenconnorg\Documents\knight-federal-solutions\AF_Installation_Feedback\gdbs-complete\

:: cd into directory with completed geodatabases
:: zip each geodatabase in directory into a new directory called zips
mkdir zips
for /D %%G IN (*.gdb) do 7z a "zips/%%G.zip" "%%G" -mx=9

:: then zip the whole zips directory
cd .. 
7z a gdbs-complete.zip %PathDir%/zips -mx=9

:: then remove the old zips directory
rmdir %PathDir%\gdbs-complete\zips

:: keep batch file commands open just in case
cmd /k