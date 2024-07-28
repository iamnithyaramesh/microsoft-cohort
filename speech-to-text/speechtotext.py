from openai import OpenAI
client = OpenAI(api_key="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")

audio_file= open("text-to-speech\speech.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
transcript