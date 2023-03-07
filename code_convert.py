import os
from dotenv import load_dotenv
import openai
import time

load_dotenv()

# see .env
api_key = os.environ.get("OPENAI_API_KEY")
# org_id = os.environ.get("OPENAI_ORG_ID")
model_engine = os.getenv("MODEL_ENGINE")

openai.api_key = api_key
# openai.organization = org_id

messages = []

with open('input.txt', 'r') as file:
    file_contents = file.read()

source_format = 'React / jsx'
output_format = 'React / next.js'

system_content = f"""
You are a code conversion bot. Your role is to take a file of the format {source_format} and convert it to {output_format}.
"""

messages.append({"role": "system", "content": system_content})
messages.append({"role": "assistant",
                "content": f"Please provide the {source_format} file and I will convert it to {output_format}."})
messages.append({"role": "user", "content": file_contents})

response = openai.ChatCompletion.create(
    model=model_engine,
    messages=messages)

reply = response["choices"][0]["message"]["content"]
print("\n\033[34m" + "Converted:\033[0m\n" + reply + "\n")
