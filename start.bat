CALL ../env/Scripts/activate.bat
START "new window" cmd /k "pelican --listen"
pelican content --autoreload