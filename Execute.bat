start cmd /c python -m http.server
start cmd /c "timeout /t 2 & start "" "chrome.exe" "C:\real-time-video-translator\runscript.html""
python stream.py