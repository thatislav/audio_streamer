"""
Client part.
Run it after server part is running.
"""

import pyaudio
import socket


port = 9090
ip = "127.0.0.1"

chunk = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True,
                frames_per_buffer=chunk)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((ip, port))

while True:
    try:
        client_sock.sendall(stream.read(chunk))
    except Exception as e:
        print(e)
        break

stream.stop_stream()
stream.close()
client_sock.close()
p.terminate()
