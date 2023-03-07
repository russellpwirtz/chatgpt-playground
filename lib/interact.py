import os
from dotenv import load_dotenv
import openai
import time
import re

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
model_engine = os.getenv("MODEL_ENGINE")

openai.api_key = api_key


def interact_with_user(name: str, messages: list, chat_history: str = ""):
    user_input = ""

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
        chat_history += f"\nUser: {user_input}\n{name}: {reply}\n"
        print("\n\033[32m" + f"{name}:\033[0m " + reply + "\n")

    chat_log = input(
        "\n\nPlease enter a filename to save the chat log to (without the .log extension): ")
    with open(f"{chat_log}.log", "w") as f:
        f.write(re.sub("\033\[\d+m", "", chat_history))
