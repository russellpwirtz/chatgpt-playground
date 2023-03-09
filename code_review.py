import os
from dotenv import load_dotenv
import openai
from lib.interact import interact_with_user

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
model_engine = os.getenv("MODEL_ENGINE")

openai.api_key = api_key

# original prompt to review code
messages = []
#  continuation prompt so we don't re-review the code with each user interaction
interaction_messages = []

with open('input.txt', 'r') as file:
    file_contents = file.read()

should_provide_code = input(
    "\033[34mDo you want to see what the updated code looks like? y/n \033[0m")


system_content = f"""
You are a code debug bot. 
Your role is to take in code and explain how it could have better quality.
Provide feedback as if it came from coworkers in a room together.
They are:
 - junior dev
 - senior dev
 - architect
"""
if 'y' in should_provide_code.lower():
    system_content += '\nProvide the updated code as the primary goal.'
else:
    system_content += '\nDo not provide updated code.'

system_content = {"role": "system", "content": system_content}
messages.append(system_content)
interaction_messages.append(system_content)

assistant_messages = [
    "We're also going to include the intern and a peer from a different company to the list of coworkers providing feedback to give them some extra experience",
    "Please provide the code and I will debug it.",
]

for message in assistant_messages:
    messages.append({"role": "assistant", "content": message})
    interaction_messages.append({"role": "assistant", "content": message})

# for the first pass
messages.append({"role": "user", "content": file_contents})
# for user interection (so we don't reprocess the file each prompt)
interaction_messages.append({"role": "assistant", "content": file_contents})

response = openai.ChatCompletion.create(
    model=model_engine,
    messages=messages)

reply = response["choices"][0]["message"]["content"]

chat_history = "\n\033[34m" + "ReviewBot:\033[0m\n" + reply + "\n"
print(chat_history)

interaction_messages.append({"role": "assistant", "content": reply})

interact_with_user(
    name="ReviewBot", messages=interaction_messages, chat_history=chat_history)
