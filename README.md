# GohAnalyst - OpenBB AI Slack Agent

This repository leverages [OpenBB's agents repo](https://github.com/OpenBB-finance/openbb-agents) to build a Slack bot that has access to 100+ financial datasets. This was done as part of my OpenBB Creaton 2023.

The blogpost associated with this can be found here: TBD.

![image](https://github.com/DidierRLopes/openbb-slack-agent/assets/25267873/cdb72cc4-4bf1-4078-a800-b398b6a6c7e6)

## Getting Started

### Get OpenBB PAT

Sign up for the [OpenBB Hub](https://my.openbb.co).

This will allow you to [set any API keys for different data vendors](https://my.openbb.co/app/platform/api-keys), which will allow your agent to be able to tap into more diversified financial datasets. Once that is done you can retrieve your Personal Access Token (PAT) [here](https://my.openbb.co/app/platform/pat).

Replace your OpenBB_PAT credentials in the [slack_bot.py file](slack_bot.py).

### Get OpenAI API key

Retrieve your OpenAI Key from [here](https://platform.openai.com/api-keys).

Replace your OpenAI API key in the [slack_bot.py file](slack_bot.py).

### Create Slack Bot

1. Go into [Slack API page](https://api.slack.com/).
2. Click on "Your Apps"
3. Click on "Create new App"
4. Select "From an App Manifest"
5. This [file](/slack_bot_manifest.json) will provide your app manifest to get started quickly so you can set up all the Bot scopes correctly.

### Get your Slack Bot credentials

You will need: 

* Go to **Install App** tab:  
  * `SLACK_BOT_TOKEN` can be found int **OAuth Tokens for Your Workspace**

* Go to **General** tab:
  * `SLACK_APP_TOKEN` can be found in **App Credentials**
  * `SIGNING_SECRET` can be found in **App-Level Tokens**

Replace those credentials in the [slack_bot.py file](slack_bot.py).

### Run Slack Bot

Install the 3 python libraries needed to run this:

```
pip install openbb
pip install openai
pip install slack_bolt
```

Then run it with `python slack_bot.py`.

At this stage the App is running on localhost:3000 and waiting for an event in order to trigger a reply.

However your Slack Bot isn't yet subscribed to be notified of events in Slack.

### Slack Bot to be subscribed to Slack events

Now you want to go into **Event Subscriptions** tab and enable events.

We want the HTTP POST requests to be sent to localhost:3000 where our Slack Bot python script is ready to reply.

Hence we can use ngrok to forward traffic to our local port.

After [installing ngrok](https://ngrok.com/docs/guides/getting-started/), this can be done with:

```
ngrok http 3000
```

The output looks like this:

![image](https://github.com/DidierRLopes/openbb-slack-agent/assets/25267873/cbce258d-c495-4835-9799-905ab501ed5f)

Once that is done you want to copy the Forwarding link as shown below

![image](https://github.com/DidierRLopes/openbb-slack-agent/assets/25267873/fb99a229-05c2-4c32-bd9f-7cc95866ece4)

Then that link is added to the **Request URL** input on your Slack API page, with the addition of `/slack/events` at the end.

This is what it should look like:

<img width="982" alt="Screenshot 2024-02-24 at 10 57 51 AM" src="https://github.com/DidierRLopes/openbb-slack-agent/assets/25267873/85e46a90-a537-499a-a984-1de1d43fa295">

If everything works as expected, you should get a green tick to validate that the URL is working and on the ngrok window it should display a new line with:

```
POST /slack/events                       200 OK
```

### Have fun

![image](https://github.com/DidierRLopes/openbb-slack-agent/assets/25267873/754fa920-2b17-47b8-99f2-3e6352daf8bc)


## Disclaimer

This project was done only for the context of the OpenBB Creaton 2023 to explore what one could build on top of the OpenBB agent and will **NOT** be maintained or even improved.

