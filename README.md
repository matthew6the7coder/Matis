# Matis

My personal AI helper for my projects. It runs on my own computer using Ollama, so it's free and has no credits.

## What you need

- A computer that can run Python
- [Ollama](https://ollama.com) installed
- Python installed

## How to run Matis

1. Install Ollama from ollama.com
2. Download the model by running this in a terminal:
   ```
   ollama pull llama3.2:1b
   ```
3. Install the Ollama Python library:
   ```
   pip install ollama
   ```
4. Start Matis:
   ```
   python chatbot.py
   ```
5. Chat away! Type `quit` to stop.

## Change Matis's personality

Open `chatbot.py` and edit the text in the `"content"` line near the top. You could make Matis funny, super encouraging, or an art teacher.

## Notes

- Matis runs on your own computer, so nothing is sent to the internet.
- Small models are not as clever as big ones, so Matis may get things wrong sometimes.
