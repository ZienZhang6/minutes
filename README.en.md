# Minutes

<div align="center">
  <img src="media/logo.png" width="300px">
</div>

[中文](README.md) | [English](README.en.md)

Minutes is an intelligent assistant for long audio files. It uses Paraformer, the best open-source Chinese speech recognition model, to transcribe podcasts into text. Then, it leverages large language models to summarize the transcript, extract highlights based on timestamps, and also supports Q&A and continuation features.

## Main Features

- Transcribe podcasts into text
- Summarize transcripts with large language models to generate highlights (currently supports OpenAI, ChatGLM, OpenBuddy, and other open-source Chinese models)
- (TODO) Add chat functionality, allowing users to ask questions based on podcast content
- (TODO) Build a vector database from multiple long audio files to support continuation

## Features

- Highly accurate Chinese speech recognition, surpassing OpenAI's Whisper Large model
- Fully private deployment supported, [Sample recognition result for Random Podcast E114](media/out.txt)

![Demo](media/screenshot.jpg)

## Installation and Usage

```bash
# Download models
bash downloads/download.sh
# Install dependencies
pip3 install -r requirements.txt

# Optional: Install ffmpeg if your audio format is not wav

# Start running
python3 pipeline.py --wav dowloads/test_audios/e114.mp3
```
