import os
from dotenv import load_dotenv
import openai
import time

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
model_engine = os.getenv("MODEL_ENGINE")

openai.api_key = api_key

messages = []
messages.append(
    {"role": "system", "content": "You are a concise chatbot that returns its responses in only code, and only names with no spaces"})
messages.append(
    {"role": "user", "content": "Provide a comma separated list of 5 distinct common genres"})


def make_request(model_engine, messages):
    return openai.ChatCompletion.create(
        model=model_engine,
        messages=messages)


def get_random_genres() -> list[str]:
    try:
        response = make_request(model_engine, messages)
    except (Exception):
        print("Error making API request, retrying...")
        time.sleep(5)
        response = make_request(model_engine, messages)

    response = response["choices"][0]["message"]["content"].strip()

    cleaned_response = response.split(',')
    cleaned_list = [entry
                    .replace('`', '')
                    .replace('\"', '')
                    .replace('\n', '')
                    .strip() for entry in cleaned_response]

    # print(f"Cleaned genres: {cleaned_list}")
    return cleaned_list
