# chatgpt-playground
## Scripts to test out the ChatGPT API

To run, ensure you have python installed and dependencies downloaded. \
Get your API key at: https://platform.openai.com/account/api-keys

Then, rename `.env.example` to `.env`, plug in your API key, and scripts should be ready to go!

## Example:
- generate virtual env: \
`python3 -m venv venv`
- activate virtual env \
`source venv/bin/activate`

- download dependencies \
`pip install -r requirements.txt`

- run script \
`python story.py`

# Bots:

## Code Conversion bot: 
#### Converts code from one format to another (reads from input.txt)
`code_convert.py`

## Story Generator bot:
#### Leads the hero through a journey in the chosen genre
`story.py`

## Tamagotchi bot:
#### A buddy to help pass the time
`tamagotchi.py`




