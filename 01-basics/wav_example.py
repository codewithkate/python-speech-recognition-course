# Audio file formats
# .mp3 - compressed, but can lose info
# .flac - lossless compression
# .wav - largest size, but best quality (standard)

import wave

# Audio signal parameters
# - number of channels: mono(1), stereo(2)
# - smaple width: bytes per sample
# - framreate/sample_rate: samples per second (i.e. 44,100Hz)
# - number of frames
# - values of a frame

wav_file = "output.wav"

obj = wave.open(wav_file, "rb")

print("Number of channels:", obj.getnchannels())
print("Sample Width:", obj.getsampwidth())
print("Frame Rate:", obj.getframerate())
print("Number of Frames:", obj.getnframes())
print("Parameters:", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)  #read all frames
print(type(frames), type(frames[0]))
print(len(frames) / 2)

obj.close()

obj_new = wave.open("output_new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16_000.0)
obj_new.writeframes(frames)  #duplicate the file

obj_new.close()