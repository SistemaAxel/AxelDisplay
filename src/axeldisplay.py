# sudo apt install python3-flask python3-gtts mpg123 -y && pip3 install --upgrade gtts gtts-token
from flask import Flask, request
import os
import subprocess
from gtts import gTTS
import tkinter as tk

# Change this to your TVHEADEND / DIZQUETV / IP CAM / etc.
CHANNELS = {
    "la1": "http://192.168.0.71:9981/play/ticket/stream/channel/b460d7390c8a42a45b3806914c1cf57d?title=1%20%3A%20La%201",
    "la2": "http://192.168.0.71:9981/play/ticket/stream/channel/f14b070ce7fb468b87c13ef62ee42323?title=2%20%3A%20La%202",
    "antena3": "http://192.168.0.71:9981/play/ticket/stream/channel/8193702dd4f8ed9ea81eb4f5f4759a7f?title=3%20%3A%20antena3",
    "cuatro": "http://192.168.0.71:9981/play/ticket/stream/channel/083ecf9202d9a8937cc838708bbc7d3b?title=4%20%3A%20Cuatro",
    "telecinco": "http://192.168.0.71:9981/play/ticket/stream/channel/239aefbccec67a090adb925d7b85a497?title=5%20%3A%20Telecinco",
    "la6": "http://192.168.0.71:9981/play/ticket/stream/channel/b4af082e52c4112000fd71065e14eb27?title=6%20%3A%20laSexta",
    "energy": "http://192.168.0.71:9981/play/ticket/stream/channel/36acb5e05b575fd30db8339dcf8a8178?title=11%20%3A%20Energy",
    "atreseries": "http://192.168.0.71:9981/play/ticket/stream/channel/86729669b7a6ce4702469223862972dc?title=13%20%3A%20atreseries",
    "24h": "http://192.168.0.71:9981/play/ticket/stream/channel/219134041bcd796116e0b397cbc73d54?title=9%20%3A%2024h",
    "kasa-1": "http://192.168.0.21:10071/video?channel=1",
    "kasa-2": "http://192.168.0.21:10071/video?channel=2",
    "kasa-3": "http://192.168.0.21:10071/video?channel=3",
    "kasa-4": "http://192.168.0.21:10071/video?channel=4",
    "kasa-5": "http://192.168.0.21:10071/video?channel=5",
    "kasa-6": "http://192.168.0.21:10071/video?channel=6",
    "kasa-7": "http://192.168.0.21:10071/video?channel=7",
    "kasa-8": "http://192.168.0.21:10071/video?channel=8",
    "kasa-9": "http://192.168.0.21:10071/video?channel=9",
    "kasa-10": "http://192.168.0.21:10071/video?channel=10",
}
CURRENT_CHANNEL = ""
app = Flask(__name__)

def alert(msg: str):
    k = len(msg.split(" "))
    f = k*1250
    root = tk.Tk() 
    root.title("AXEL") 
    root.geometry('750x250+70+70')
    msg = tk.Label(root, text=msg, font=("Arial", 30)).pack()
    root.after(f,lambda:root.destroy())
    root.mainloop()

@app.route('/api/stream_channel/<name>')
def api__stream_channel(name):
    CURRENT_CHANNEL = name
    url = CHANNELS[name]
    os.system("pkill vlc")
    os.system(f"vlc -I qt --qt-minimal-view '{url}' &")
    return "Done"
@app.route('/api/stream_stop')
def api__stream_stop():
    os.system("pkill vlc")
    return CURRENT_CHANNEL
@app.route('/api/cmd')
def api__cmd():
    os.system(request.args["q"])
    return "Done"
@app.route('/api/notify')
def api__notify():
    e =gTTS(request.args["msg"] + " - " + request.args["msg"], lang="es", slow=True)
    e.save("tts.mp3")
    os.system("mpg123 tts.mp3 &")
    alert(request.args["msg"])
    return "Done"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8314, debug=True) ##
