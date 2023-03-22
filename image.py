#!/usr/bin/python3

import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

question = input("\033[95mQuelle image tu veux fréro ? \033[0m")

response = openai.Image.create(
    prompt=question,
    n=1,
    size="1024x1024"
)

print(response['data'][0]['url'])