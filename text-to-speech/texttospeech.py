from pathlib import Path
from openai import OpenAI
client = OpenAI(api_key="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")

speech_file_path = "text-to-speech\speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)