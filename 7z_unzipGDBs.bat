:: download 7zip to use this batch file
:: make sure 7z zip is added to the environment variables as specified below
:: or set path accordingly

set PATH=%PATH%;C:\Program Files\7-Zip\
echo %PATH%

:: Set working PathDirectory accordingly
set PathDir=C:\Users\stevenconnorg\Documents\knight-federal-solutions\AF_Installation_Feedback\

:: Set name of folder/zip with complete gdbs
set gdbsZipsFolder=%CD%/gdbs-complete

:: Unzip the folder
mk dir %gdbsZipsFolder%
7z e %gdbsZipsFolder%.zip -o%gdbsZipsFolder%

:: then unzip each zipped gdb inside directory
cd %gdbsZipsFolder%
7z x *.zip 

:: remove zipped gdbs afterward 
del *.zip /a /s

cmd /k