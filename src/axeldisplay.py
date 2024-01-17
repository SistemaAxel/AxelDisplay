from flask import Flask, request
import os
from gtts import gTTS
import tkinter as tk
import socket
DEVICE_NAME = socket.gethostname()
# Change this to your TVHEADEND / DIZQUETV / IP CAM / etc.
CHANNELS = {
    "playa": "http://212.170.100.189/mjpg/video.mjpg",
    "portugalete": "http://212.8.113.121:8081/mjpg/video.mjpg",
    "cocina": "rtsp://hack:hack@192.168.0.41/av_stream/ch0",
}
CURRENT_CHANNEL = ""
app = Flask(__name__)

def alert(msg: str):
    k = len(msg.split(" "))
    f = ((k*750)*2)+2000
    root = tk.Tk() 
    root.title("AXEL") 
    root.geometry('750x250+70+70')
    msg = tk.Label(root, text=msg, font=("Arial", 30)).pack()
    root.after(f,lambda:root.destroy())
    root.mainloop()

@app.route('/api/stream_channel')
def api__stream_channel():
    global CURRENT_CHANNEL
    name=request.args["q"]
    CURRENT_CHANNEL = request.args["q"]
    url = CHANNELS[name]
    os.system("pkill vlc")
    os.system(f"vlc -I qt --qt-minimal-view '{url}' &")
    return "Done"
@app.route('/api/stream_stop')
def api__stream_stop():
    global CURRENT_CHANNEL
    os.system("pkill vlc")
    CURRENT_CHANNEL = ""
    return "Done"
@app.route('/api/cmd')
def api__cmd():
    os.system(request.args["q"])
    return "Done"
@app.route('/api/notify')
def api__notify():
    os.system("pkill vlc")
    e =gTTS(request.args["msg"] + " - " + request.args["msg"], lang="es", slow=True)
    e.save("tts.mp3")
    os.system("mpg123 tts.mp3 &")
    alert(request.args["msg"])
    if CURRENT_CHANNEL != "":
        url = CHANNELS[CURRENT_CHANNEL]
        os.system(f"vlc -I qt --qt-minimal-view '{url}' &")
    return "Done"

@app.route('/api/axeldiscover')
def api__axeldiscover():
    return {"hostname": DEVICE_NAME, "service": "AxelDisplay"}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8314, debug=True) ##
