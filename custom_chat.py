from dotenv import load_dotenv
from lib.interact import interact_with_user


load_dotenv()

messages = []
chat_assistant = input(
    "\n\033[33mWhat type of chatbot would you like to create?\033[0m \n\n> ")
messages.append(
    {"role": "system", "content": f"You are a chatbot who is acting like they really are {chat_assistant}"})

print(f"Say hello to your new {chat_assistant} assistant!\n")

interact_with_user(name=chat_assistant, messages=messages)
