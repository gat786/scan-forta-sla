import sys
from requests import get


def get_status(address: str):
    """ Function which calls the API's and gets response from Forta SLA API """
    url = f"https://api.forta.network/stats/sla/scanner/{address}"
    response = get(url)
    return 0


def handler(event, context):
    """ Lambda Handler Function """
    get_status("0xBc9f286125e7DAD9402A05c555028750FdDA85Bb")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'
