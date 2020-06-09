"""
Server part.
Run it first of all.
"""

import pyaudio
import socket
import wave


port = 9090
chunk = 256
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
WAVE_OUTPUT_FILENAME = "output_1.wav"

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True,
                frames_per_buffer=chunk)

server_sock = socket.socket()
server_sock.bind(('', port))
server_sock.listen(1)
conn, address = server_sock.accept()

print("Connected: ", address)
print("Your IP address is: ", socket.gethostbyname(socket.gethostname()))
print("Server Waiting for client on port ", port)

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)

while True:
    # Recieve data from the client:
    data = conn.recv(1024)
    if not data:
        break
    wf.writeframes(data)

wf.close()
stream.stop_stream()
stream.close()
server_sock.close()
conn.close()
p.terminate()
