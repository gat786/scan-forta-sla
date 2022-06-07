import sys
import os
import logging
from requests import get
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def get_status(address: str):
    """ Function which calls the API's and gets response from Forta SLA API """
    url = f"https://api.forta.network/stats/sla/scanner/{address}"
    response = get(url)
    return response.json()


def handler(event, context):
    """ Lambda Handler Function """
    load_dotenv()

    bot_address = os.environ["FORTA_BOT_ADDRESS"]
    slack_bot_token = os.environ["SLACK_BOT_TOKEN"]

    slack_client = WebClient(token=slack_bot_token)

    status = get_status(bot_address)

    if "statistics" in status:
        if "avg" in status["statistics"]:
            avg_sla = status["statistics"]["avg"]
            if status["statistics"]["avg"] <= 0.75:
                try:
                    slack_client.chat_postMessage(
                        channel="CSBJY2Z47",
                        text=f"Forta Bot with id: {bot_address} has a low sla of {avg_sla}"
                    )
                except SlackApiError as error:
                    assert error.response["error"]
            else:
                log_message = f"Bot has a average sla of {avg_sla}"
                logging.info(log_message)
    return 'Executed Lambda function successfully!'
