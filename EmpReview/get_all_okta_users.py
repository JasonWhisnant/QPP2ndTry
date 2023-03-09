
import requests

def get_all_users(domain, okta_api_token, param):
    error = None
    headers = {'Authorization': 'SSWS {}'.format(okta_api_token),
               'Accept': 'application/json',
               'Content-Type': 'application/json'}

    okta_url = "https://{}.okta.com".format(domain)
    params = param
    url = '{0}/api/v1/users?{1}'.format(okta_url,params)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        users = response.json()
        links = response.links
        while 'next' in links:
            url = links['next']['url']
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            next_users = response.json()
            users += next_users
            links = response.links
    except Exception as e:
        error = "get_all_users failed with exception {}".format(e)
        print(error)
    # return (users, error)
    return users


users = get_all_users('eso','00wRZl_kpU3eHwWjQgfb1TtuGzec52ddOIE4-p_FHB','filter=status eq "ACTIVE"')

for u in users:
    pass
    # print(u['profile']['firstName']+" "+u['profile']['lastName'])