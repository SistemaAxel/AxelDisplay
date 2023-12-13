echo Deleting Old Code
rm /home/pi/axeldisplay.py

echo Downloading Code
wget -O /home/pi/axeldisplay.py https://raw.githubusercontent.com/SistemaAxel/AxelDisplay/main/src/axeldisplay.py 

echo ¡Done!
echo The HTTP Port is 8314
