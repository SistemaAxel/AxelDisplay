echo NOT FOR PRODUCTION
echo PLEASE USE PI USER

echo Installing Flask, gTTS and mpg123 via APT
sudo apt install python3-flask python3-gtts mpg123 -y

echo Updating gTTS via pip
pip3 install --upgrade gtts gtts-token


echo Downloading Code
wget -O /home/pi/axeldisplay.py https://raw.githubusercontent.com/SistemaAxel/AxelDisplay/main/src/axeldisplay.py 
sudo wget -O /etc/systemd/system/axeldisplay.service https://raw.githubusercontent.com/SistemaAxel/AxelDisplay/main/src/axeldisplay.service

echo Starting AxelDisplay
sudo systemctl enable --now axeldisplay

echo ¡Done!
echo The HTTP Port is 8314
