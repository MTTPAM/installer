set git=git/bin/git
%git% init .
%git% remote add origin https://github.com/MTTPAM/PublicRelease.git
%git% fetch --all
%git% reset --hard origin/master
del FirstTimeSetup.bat