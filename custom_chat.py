from dotenv import load_dotenv
from lib.interact import interact_with_user


load_dotenv()

messages = []
chatbot = input(
    "\n\033[33mWhat type of chatbot would you like to create? To create a character based on conversations.txt press Enter\033[0m \n\n> ")

if chatbot:
    messages.append(
        {"role": "system", "content": f"You are a chatbot who is acting like they really are {chatbot}. If you're unable to do something, make up a reason in character instead of revealing that you're an AI language model."})
    print(f"Say hello to your new {chatbot} assistant!\n")
else:
    with open('input.txt', 'r') as file:
        file_contents = file.read()

    messages.append(
        {"role": "system", "content": f"You are a chatbot who has chats with users, and is acting like they really are a character based on the provided conversations."})
    messages.append(
        {"role": "assistant", "content": "Please provide the conversations to base my style on, and I will have a chat with you."})
    messages.append(
        {"role": "user", "content": f"{file_contents}"})
    messages.append(
        {"role": "assistant", "content": "Thank you. I will now begin chatting to you in that style. I won't bring up your prior conversations unless you prompt me and will act in character."})


interact_with_user(name=chatbot, messages=messages, chatbot_start_first=True)
