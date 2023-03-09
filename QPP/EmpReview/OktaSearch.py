import asyncio, time, get_all_okta_users

from okta.client import Client as OktaClient


config = {
    'domain': 'eso',
    'token': '00wRZl_kpU3eHwWjQgfb1TtuGzec52ddOIE4-p_FHB',
}

"""
async def main(parameters):
    tic = time.perf_counter()
    users, resp, err = await okta_client.list_users(parameters)
    n = len(users)

    toc = time.perf_counter()


    print(f"Total of {n} users.")
    print(f"Finished in {toc - tic:0.4f} seconds")

"""
tic = time.perf_counter()
users = get_all_okta_users.get_all_users(config['domain'],config['token'])
n = len(users)
# print(users[1])
toc = time.perf_counter()
print(f"total of {n} users")
print(f"Finished in {toc - tic:0.4f} seconds")



