import os
from dotenv import load_dotenv
import openai
import re

# credit: https://gist.github.com/Darkflib/f1c63164397a50aef8ccf7d8c2a142e0

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
# org_id = os.environ.get("OPENAI_ORG_ID")
model_engine = os.getenv("MODEL_ENGINE")

openai.api_key = api_key
# openai.organization = org_id

messages = []
system_msg = input(
    "\n\033[33mWhat type of chatbot would you like to create?\033[0m \n\n> ")
messages.append(
    {"role": "system", "content": f"You are a chatbot who is acting like they really are {system_msg}"})

print("\n")

print(f"Say hello to your new {system_msg} assistant!\n")
user_input = ""
chat_history = "System: " + system_msg

while user_input != "!endchat":
    user_input = input("\033[34mYou: \033[0m")
    if user_input == "!endchat":
        break

    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=messages)

    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    chat_history += f"\nUser: {user_input}\nChatGPT: {reply}\n"
    print("\n\033[32m" + "Bot:\033[0m " + reply + "\n")

chat_log = input(
    "\n\nPlease enter a filename to save the chat log to (without the .log extension): ")
with open(f"{chat_log}.log", "w") as f:
    f.write(re.sub("\033\[\d+m", "", chat_history))
