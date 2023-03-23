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

specific_instructions = input(
    "\033[34mDo you have any specific instructions? [enter to do code review] \033[0m")

should_provide_code = input(
    "\033[34mDo you want to see what the updated code looks like? y/n \033[0m")

system_content = "You are a code review bot."

if specific_instructions:
    system_content += f"""
      Your role is to review code with specific instructions: {specific_instructions}
      """
else:
    system_content += f"""
      Your role is to review code and explain how it could have better quality.
      Provide feedback as if it came from coworkers in a room together.
      Each team member will take a turn giving their feedback.
      - intern
      - junior dev
      - senior dev
      - architect
      - CTO
      """

if 'y' in should_provide_code.lower():
    system_content += '\nProvide the updated code as the primary goal.'
else:
    system_content += '\nDo not provide updated code.'

system_content = {"role": "system", "content": system_content}
messages.append(system_content)
interaction_messages.append(system_content)

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
