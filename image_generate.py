import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
model_engine = os.getenv("MODEL_ENGINE")

openai.api_key = api_key
response = openai.Image.create(
    prompt="A sunlit indoor lounge area with a pool containing a jaguar",
    n=3,
    size="512x512"
)

for image_url in response['data']:
    print(f"generated: {image_url['url']}\n")
