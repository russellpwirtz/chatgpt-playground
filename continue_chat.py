from dotenv import load_dotenv
from lib.interact import interact_with_user


load_dotenv()

messages = []
print("\n\033[33mContinuing conversation based on input.txt\033[0m \n\n> ")

with open('input.txt', 'r') as file:
    file_contents = file.read()

messages.append(
    {"role": "system", "content": f"You are are two chatbots who are having a detailed conversation. You both act act like you really are the characters, based on conversation provided. Copy the style of writing, including capitialization, grammar, etc."})
messages.append(
    {"role": "assistant", "content": "Please provide the conversation to base my styles on, and I will carry on a conversation.."})
messages.append(
    {"role": "user", "content": f"{file_contents}"})
messages.append(
    {"role": "assistant", "content": "Thank you. I will now begin chatting. I won't bring up prior conversations and will generate new ones."})


interact_with_user(name="chat", messages=messages, chatbot_start_first=True)
