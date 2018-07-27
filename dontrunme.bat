@ECHO OFF
rem Initialize this as a git repo
git init .
rem Tell Git that the repo this is is for this \/
git remote add Memeless-MTTPAM https://github.com/MTTPAM/PublicRelease.git
rem fetch all updates to the repo
git fetch --all
rem reset the folder
git reset --hard origin/master
rem remove the installer.py
del installer.py /A
rem Finished Remove dontrunme
del dontrunme.bat /A