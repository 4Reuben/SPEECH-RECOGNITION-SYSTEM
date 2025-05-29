# File: main.py
# Description: This script transcribes audio files using the Wav2Vec2 model from Hugging Face Transformers.

import os
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torchaudio

# Load pretrained model and processor
processor = Wav2Vec2Processor.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-english")
model = Wav2Vec2ForCTC.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-english")

def transcribe_audio(file_path):
    print("🎤 Loading audio...")

    if not os.path.isfile(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        waveform, sample_rate = torchaudio.load(file_path)
    except Exception as e:
        print(f"❌ Error loading audio: {e}")
        return

    if sample_rate != 16000:
        print("🔁 Resampling audio to 16kHz...")
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resampler(waveform)

    print("🧠 Transcribing with Wav2Vec2...")
    input_values = processor(waveform.squeeze(), return_tensors="pt", sampling_rate=16000).input_values

    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])

    print("\n✅ Transcription:")
    print(transcription)

    # Save transcription to a text file in the same folder
    output_file = os.path.splitext(file_path)[0] + "_transcription.txt"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcription)
        print(f"💾 Transcription saved to: {output_file}")
    except Exception as e:
        print(f"❌ Failed to save transcription: {e}")

if __name__ == "__main__":
    # 👉 Replace this with the actual full path to your file
    audio_path = r"C:\Users\ASUS\Downloads\Internship\Codtech IT Solutions\Task-2\sample.wav"
    transcribe_audio(audio_path)
    print("🎧 Transcription over!")