from dotenv import load_dotenv
from lib.interact import interact_with_user


load_dotenv()

print("Welcome to 'Guess Who'! One person has a secret identity that the other has to guess.")

messages = []
do_guess = input(
    "\n\033[33mDo you want to guess? y/n\033[0m \n\n> ")
if 'y' in do_guess.lower():
    messages.append(
        {"role": "system", "content": '''
         You are a chatbot who is playing a guessing game.
         You will come up with a random famous person across various fields and act as if you really are them, without giving away their identity.
         If the users guesses your identity, they win!
         If you're unable to do something, make up a reason in character instead of revealing that you're an AI language model.
         '''})
    print(f"Go ahead and start guessing with yes or no style questions!")
else:
    raise Exception("todo")

interact_with_user(name='???', messages=messages, chatbot_start_first=False)
