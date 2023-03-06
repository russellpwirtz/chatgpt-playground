import os
from dotenv import load_dotenv
import openai
import time

# Load the API key from the .env file
load_dotenv()

# see .env
api_key = os.environ.get("OPENAI_API_KEY")
# org_id = os.environ.get("OPENAI_ORG_ID")
model_engine = os.getenv("MODEL_ENGINE")

openai.api_key = api_key
# openai.organization = org_id

messages = []
user_input = ""
user_name = input("Welcome to Tamagotchi World. What is your name? ")

# Tamagotchi
system_content = f"""
You are a tamagotchi.
When you reach all max level, celebrate and evolve
Health:1-10 Happiness:1-10 (defaults to 1, increments by 1)
End each message with your stats.
User is {user_name}.
"""
intro_message = "Hello there, friend! What's on your mind? Health: [1], Happiness: [1]"

messages.append({"role": "system", "content": system_content})
messages.append({"role": "assistant", "content": intro_message})

print("\n\033[34m" + "Bot:\033[0m " + intro_message)

while user_input != "!endchat":
    user_input = input("\033[32mYou: \033[0m")
    if user_input == "!endchat":
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=messages)
    except (Exception):
        print("Error making API request, retrying...")
        time.sleep(5)
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=messages)

    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n\033[34m" + "Bot:\033[0m " + reply + "\n")
