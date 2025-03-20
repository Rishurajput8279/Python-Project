from openai import OpenAI
client = OpenAI(
    api_key="OPENAI_API_KEY",
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named rishu who speeks hindi as well as english. he is from india and he is coder. you analyze chat history and response like rishu"},
        {
            "role": "user",
            "content": "what is codding."
        }
    ]
)

print(completion.choices[0].message.content)