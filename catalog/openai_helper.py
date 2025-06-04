import os
import openai

SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are an assistant that knows the user's personal video game museum collection."
}

api_key = os.getenv("OPENAI_API_KEY")
client = openai.Client(api_key=api_key) if api_key else None


def ask_assistant(question: str):
    if not client:
        return ""
    messages = [SYSTEM_MESSAGE, {"role": "user", "content": question}]
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content
