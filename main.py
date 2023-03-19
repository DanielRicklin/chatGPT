#!/usr/bin/python

import os
from dotenv import load_dotenv
import openai
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()
console = Console()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

while True :
    question = input("\033[95mQuestion : \033[0m")

    messages.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    print("\n\033[95mChatGPT : \033[0m")
    console.print(Markdown(response.choices[0].message.content))
    print("\n")
    messages.append(response.choices[0].message)
