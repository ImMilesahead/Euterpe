# Euterpe
Streaming audio over UDP
run py typing 

required packages are 
```
sys (default)
socket (default)
threading (default)
pyaudio
```

```
python Audio\ Streamer.py INPUT
```
will record audio from default microphone and send it over udp to connections

```
python Audio\ Streamer.py OUTPUT
```
will recieve audio via udp and output to default output source