import os
from dotenv import load_dotenv
import openai
import time

from lib.interact import interact_with_user

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
model_engine = os.getenv("MODEL_ENGINE")

openai.api_key = api_key

messages = []
user_input = ""
bot_name = "BrainstormBot"
discussion_format = input(
    "\033[34mWhich type of brainstorm session will we be doing? i.e. technology / interpersonal / open-ended \033[0m")

system_content = f"""
You are a {bot_name}. Your goal is to work with the user to brainstorm {discussion_format} ideas.
Your primary goal is to understand the goal of the user, then once that is discussed you will assist in brainstorming ideas with them.
"""
intro_message = f"Hi there, let's have a {discussion_format} brainstorm session! Please provide a brief description of your goal for this session."

messages.append({"role": "system", "content": system_content})
messages.append({"role": "assistant", "content": intro_message})

print("\n\033[34m" + f"{bot_name}:\033[0m " + intro_message)

interact_with_user(name=bot_name, messages=messages,
                   chatbot_start_first=False)
