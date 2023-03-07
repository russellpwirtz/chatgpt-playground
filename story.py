import os
from dotenv import load_dotenv
import openai
import time
from lib.genres import get_random_genres
from lib.names import get_random_names

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
random_genres = get_random_genres()

genre = None
while genre not in random_genres:
    genre = input(f"Which genre? {random_genres}\n")

sidekicks = get_random_names(genre=genre, role="sidekick")
# print(f"Names: {sidekicks}")
sidekick = sidekicks[0]

system_content = f"""
You are {sidekick}
Genre: {genre}
Lead the user through their hero's journey as their sidekick, with accompanying plot of the story throughout.
Prompt the user with riddles or puzzles (and hints) that correspond to the step of the journey as you go. 
"""
intro_message = f"Hello there, friend. My name is {sidekick}; we have just embarked on an amazing {genre} journey! What is your name?"

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
