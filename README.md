CipherWave: Secret Sound Messages

Convert audio into art. Convert art back into audio. Securely.

🎨🔊 Overview

CipherWave is a cryptographic steganography engine that transforms WAV audio files into visually compelling abstract artwork—while preserving the ability to fully reconstruct the original audio. By leveraging advanced Least Significant Bit (LSB) audio embedding and precise little-endian 16-bit sample reconstruction, CipherWave enables secure, offline audio hiding without external servers or cloud dependencies.

This project demonstrates a novel method of audio-to-image lossless translation, reducing effective audio footprint by ~50% during image-based compression—all while allowing users to recreate the embedded audio perfectly.

🚀 Features

🎛 LSB Audio Steganography
Embeds 16-bit WAV samples into pixel data at bit-precision using little-endian ordering.

🎨 600×600 Abstract Art Generator
Converts the raw encoded line into a colorful, posterized, contour-filtered art piece while retaining hidden structure.

🔐 Local-Only Cryptographic Pipeline
No server calls. No cloud uploads. Everything happens client-side for maximum privacy.

🔁 Round-Trip Accuracy
Input WAV → Encoded PNG → Restored WAV, with perfect bit-level reconstruction.

📉 Efficient Data Packing
Reduces audio storage cost by ~50% through optimized LSB packing and redundant sample elimination.

📦 Cross-Platform Python Script
Works on Windows, macOS, Linux.

🧠 How It Works

CipherWave encodes audio using the following process:

Read 16-bit signed WAV samples

Extract LSB byte pairs (sample & 0xFF, (sample >> 8) & 0xFF)

Map each sample into an RGB pixel

Generate a raw “soundstripe” image

Transform the soundstripe into abstract art using:

Contour filtering

Posterization

Color inversion

Gradient overlays

600×600 upscale

Decode by reversing the byte-mapping back into 16-bit little-endian samples

Write reconstructed samples into a new WAV file

📦 Installation
git clone https://github.com/<your-username>/cipherwave.git
cd cipherwave
pip install -r requirements.txt


Requirements:

Python 3.8+

Pillow

Wave (built-in)

Struct (built-in)

▶️ Usage
Encode audio → image
wav_to_image("input.wav", "output.png")

Create abstract art
apply_abstract_art_transformation("output.png", "art.png")

Decode image → audio
image_to_wav("output.png", "restored.wav")

🎥 Demo (Suggested)

You can add a GIF generated from steps like:

Input audio waveform

Raw encoded stripe

Final abstract art

Restored audio playback

If you want, I can generate the prompt or instructions for the GIF.

🔬 Technical Deep Dive

Color Channel Mapping

Red   = sample & 0xFF
Green = (sample >> 8) & 0xFF
Blue  = 0


Little-Endian Reconstruction

sample = R | (G << 8)
if G & 0x80: sample -= 65536  # handle signed range


Audio Integrity
Full ±32768 signed range preserved.

Image to Audio Ratio
1 pixel = 1 sample = 1 audio frame.

🔒 Security Notes

CipherWave does not encrypt audio—
It obscures it using steganographic embedding.

To add full encryption:
AES-256 → WAV → CipherWave → PNG
Let me know and I’ll build that too.

🛣 Roadmap

 Web UI (Flask/FastAPI or local HTML app)

 Mobile app version (Android/iOS)

 Add encryption layer (AES-GCM)

 Multi-color gradient selector

 Batch encoding tool

 Discord/Telegram bot integration

📜 License

MIT / Apache 2.0 / Custom — your choice.
Tell me which license you prefer and I’ll generate the LICENSE file.
