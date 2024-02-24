import os
import openai
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "REPLACE_ME"
openai.api_key = "REPLACE_ME"

client = OpenAI()

from openbb_agents import agent

SLACK_BOT_TOKEN="REPLACE_ME"
SLACK_APP_TOKEN="REPLACE_ME"
SIGNING_SECRET="REPLACE_ME"

import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SIGNING_SECRET
)

@app.event("app_mention")
def event_test(body, say):
    message = body['event']['text']

    # If the incoming message contains "hi", then respond with a "Hello" message
    if "openbb" in message.lower():
        # React to the message with an emoji
        result_openbb = agent.openbb_agent(
            message,
            OPENBB_PAT="REPLACE_ME"
        )

        completion = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are an expert financial analyst with 30 years of experience. Summarize the following answer to be as concise as possible and slightly sarcastic."},
                {"role": "user", "content": f"The question was {message} and the output is {result_openbb}"}
            ]
        )
        result = completion.choices[0].message.content

    else:
        completion = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are an expert financial analyst with 30 years of experience. You write answers that are extremely concise and short, but slightly sarcastic."},
                {"role": "user", "content": message}
            ]
        )
        result = completion.choices[0].message.content

    say(result)


# Start your app
if __name__ == "__main__":
    app.start(port=3000)