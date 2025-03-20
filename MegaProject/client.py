from openai import OpenAI
client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like in alexa and google cloud."},
        {
            "role": "user",
            "content": "what is codding."
        }
    ]
)

print(completion.choices[0].message.content)