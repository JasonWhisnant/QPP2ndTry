import asyncio, csv

from okta.client import Client as OktaClient

config = {
    'orgUrl': 'https://eso.okta.com',
    'token': '00UTYR_j4ExWv1rI-EcVd7qdjkJs9oQXbHysOArg0P',
}

okta_client = OktaClient(config)
paras = {}

async def main(groupid,userid):
    resp, err = await okta_client.add_user_to_group(groupid,userid)

with open("ProjectPlan3Users.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line["OktaID"])
        """
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main("00g3ni8b6rfakqvxO697",line["OktaID"]))
        """