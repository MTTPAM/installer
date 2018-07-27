@ECHO OFF
rem Initialize this as a git repo
git init .
rem Tell Git that the repo this is is for this \/
git remote add origin https://github.com/MTTPAM/PublicRelease.git
rem fetch all updates to the repo
git fetch --all
rem reset the folder
git reset --hard
rem set branch to non-memes
git branch
git checkout Memeless-MTTPAM
rem remove the installer.py
del installer.py /A
rem Finished Remove dontrunme
del dontrunme.bat /A