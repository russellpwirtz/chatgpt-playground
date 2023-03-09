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


## Brainstorm bot: 
#### Collaborate with chatGPT to brainstorm on any idea
`brainstorm.py`

## Chat Assistant bot:
#### Have a conversation with anyone you want
`custom_chat.py`

## Code Conversion bot: 
#### Convert code from one format to another (reads from input.txt)
`code_convert.py`

## Code Review bot: 
#### Review code from various fictitious coworkers (reads from input.txt)
`code_review.py`

## Guess Who bot: 
#### Play a game of Guess Who
`guess_who.py`

## NetHack DM bot:
#### Play NetHack with a Dungeon Master
`nethack_dm.py` 

## Story Generator bot:
#### Lead the hero through a journey in the chosen genre
`story.py`

## Tamagotchi bot:
#### A buddy to help pass the time
`tamagotchi.py` 

## TODO: 
- interview bot


# Acknowledgments
#### Code inspired by: https://gist.github.com/Darkflib/f1c63164397a50aef8ccf7d8c2a142e0
