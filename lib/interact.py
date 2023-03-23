import os
from dotenv import load_dotenv
import openai
import time
import re

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
model_engine = os.getenv("MODEL_ENGINE")

openai.api_key = api_key
debug_logging = True


def interact_with_user(name: str, messages: list, chat_history: str = "", chatbot_start_first: bool = False):
    user_input = ""

    if chatbot_start_first:
        process_messages(name, messages, chat_history, user_input)

    while user_input != "!endchat":
        user_input = input("\033[34mYou: \033[0m")
        if user_input == "!endchat":
            break

        messages.append({"role": "user", "content": user_input})
        process_messages(name, messages, chat_history, user_input)

    chat_log = input(
        "\n\nPlease enter a filename to save the chat log to (without the .log extension): ")
    with open(f"{chat_log}.log", "w") as f:
        f.write(re.sub("\033\[\d+m", "", chat_history))


def process_messages(name, messages, chat_history, user_input):
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=messages)

    reply = response["choices"][0]["message"]["content"]
    stop_reason = response["choices"][0]["finish_reason"]
    model = response["model"]
    tokens_used = response["usage"]["total_tokens"]

    messages.append({"role": "assistant", "content": reply})
    chat_history += f"\nUser: {user_input}\n{name}: {reply}\n"
    print("\n\033[32m" + f"{name}:\033[0m " + reply + "\n")

    if debug_logging:
        print(
            "\n\033[33m" + f"DEBUG:\033[0m Stop reason: {stop_reason}\tTokens_used: {tokens_used}\tModel: {model}\n")
