# install whisper using pip install whisper-speech
import importlib
# pip install -U openai-whisper
# import whisper
try:
    importlib.util.find_spec('whisper')
    print("whisper is installed")
except ImportError:
    print("whisper is not installed")
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'whisper'])
# import whisper


model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("audio.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)