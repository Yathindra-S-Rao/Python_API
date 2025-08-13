import requests

BASE_URL = 'https://gorest.co.in/public/v2/users/1009'


def get_users():
    return requests.get(BASE_URL)


if __name__=='__main__':
    print('Request:', get_users().request)
    print(get_users())
    print('Status Code:', get_users().status_code)
    print('Response Object:', get_users().json())
    print(type(get_users().json()))     # Returns List
    print(type(get_users().text))       # Returns String

    for i in get_users().json():
        if i['email'] == 'raju@testmail.com':
            print(i['id'])
