from openai import OpenAI

client = OpenAI(
    api_key= "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"
)

def openAiCall(message):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",

    messages=[
        {
          "role": "user",
          "content": "{}".format(message)
        }
      ],
)
    output = response.choices[0].message.content
    print(output)

flag=True
while flag:
    msg=input("Enter message for the chatbot")
    openAiCall(msg)
    if msg=='':
        flag=False
