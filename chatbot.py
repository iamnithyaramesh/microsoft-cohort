from openai import OpenAI
client=OpenAI(api_key="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")

assistant = client.beta.assistants.create(
    name="Macha!",
    instructions="You are my friend.Dont behave like a nerd.Just give me friendly suggestions.",
    model="gpt-4-1106-preview"
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Hey Macha!"
)