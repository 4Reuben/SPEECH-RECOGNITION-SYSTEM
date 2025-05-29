# SPEECH-RECOGNITION-SYSTEM

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: REUBEN THOMAS JOHN

*INTERN ID*:CTO4DN1267

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEEKS

*MENTOR*: NEELA SANTOSH

## PROJECT DESCRIPTION

This project is a voice-to-text transcription tool that uses the powerful Wav2Vec2 model from Hugging Face’s Transformers library to convert spoken audio into written text. The model has been fine-tuned for English and works best with .wav files sampled at 16kHz.

This transcription script is accurate, fast, and completely offline—perfect for use cases like note-taking, interview transcriptions, or voice logging. It automatically resamples the audio if needed and saves the output as a .txt file.

The script was developed as part of an internship at CodTech IT Solutions, and it serves as Task 2 in the internship’s deliverables.

## Technologies & Tools Used

- Python 3.x

- PyTorch – for running the deep learning model

- Hugging Face Transformers – for loading the pretrained Wav2Vec2 model and processor

- torchaudio – for loading and resampling .wav audio files

- VS Code / CLI

- Wav2Vec2 Large XLSR-53 English Model – by jonatasgrosman on Hugging Face

## File Structure

Codtech IT Solutions/

│

├── Task-2/

│ ├── main.py # Main Python script for transcription

│ ├── sample.wav # Sample audio input file

│ ├── sample_transcription.txt # Auto-generated transcription output

│ └── README.md # Project documentation (this file)

## How It Works

- Input: The script reads a .wav audio file from a hardcoded path.

- Loading Audio: It uses torchaudio to load and optionally resample the audio to 16kHz.

- Processing: The waveform is passed to the Wav2Vec2 processor, which tokenizes it for the model.

- Prediction: The model predicts token logits, which are decoded into a text transcription.

- Output: The transcribed text is printed in the terminal and also saved as a .txt file in the same directory as the audio.

## What I Did

- Installed and configured transformers, torchaudio, and torch.

- Loaded the pretrained Wav2Vec2 model from Hugging Face (by jonatasgrosman).

- Handled audio loading, error catching, and auto-resampling to 16kHz.

- Used PyTorch's argmax on model logits to get predicted tokens.

- Converted predictions into readable text using the processor’s decode method.

- Saved the transcription to a new .txt file beside the original audio.

## What I Didn't Do (Yet)

- Didn't use models from Meta/Facebook—used a community fine-tuned version instead.

- No GUI or web interface—this is strictly CLI-based.

- Didn’t include support for multiple files or other audio formats like MP3.

- Didn’t add support for real-time or streaming audio transcription.

## What I Learned

- How to use Hugging Face models for audio-based NLP tasks.

- How to handle and preprocess raw audio files using torchaudio.

- How to transcribe audio using Wav2Vec2 and PyTorch.

- Efficient file handling and writing outputs with UTF-8 encoding.

- Debugging tricky model input shape errors and resampling issues.

## Acknowledgments

Huge thanks to CodTech IT Solutions for giving me a hands-on opportunity to explore speech recognition with cutting-edge AI tools. This task pushed me to work with deep learning models outside of traditional NLP and introduced me to the power of audio processing using PyTorch and Hugging Face.

## OUTPUT

![Image](https://github.com/user-attachments/assets/d53ed2a0-228c-4968-8b0a-ef255d2b9984)
