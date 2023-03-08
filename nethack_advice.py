import os
from dotenv import load_dotenv
import openai
from lib.interact import interact_with_user

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
model_engine = os.getenv("MODEL_ENGINE")

openai.api_key = api_key

# original prompt to review code
messages = []
#  continuation prompt so we don't re-review the code with each user interaction
interaction_messages = []

with open('input.txt', 'r') as file:
    file_contents = file.read()

system_content = f"""
You are a nethack 3.7.0 advice bot. 
Your role is to take in the current state of the board and explain it like you are the DM.
You will then give the most advantageous next move, including which key(s) to press.
"""

system_content = {"role": "system", "content": system_content}
messages.append(system_content)
interaction_messages.append(system_content)

assistant_messages = [
    "Please provide the nethack board and I will give helpful advice.",
]

for message in assistant_messages:
    messages.append({"role": "assistant", "content": message})
    interaction_messages.append({"role": "assistant", "content": message})

# for the first pass
messages.append({"role": "user", "content": file_contents})
# for user interection (so we don't reprocess the file each prompt)
interaction_messages.append({"role": "assistant", "content": file_contents})

response = openai.ChatCompletion.create(
    model=model_engine,
    messages=messages)

reply = response["choices"][0]["message"]["content"]

chat_history = "\n\033[34m" + "DM:\033[0m\n" + reply + "\n"
print(chat_history)

interaction_messages.append({"role": "assistant", "content": reply})

interact_with_user(
    name="DM", messages=interaction_messages, chat_history=chat_history)
