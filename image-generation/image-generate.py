from openai import OpenAI
client = OpenAI(api_key="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")

response = client.images.generate(
  model="dall-e-3",
  prompt="Newton eating pasta",
  size="1024x1024",
  quality="hd",
  n=3,
)

image_url = response.data[0].url
print(image_url)