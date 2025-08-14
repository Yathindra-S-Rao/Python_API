import requests

base_url = "https://gorest.co.in/public/v2/users"
response = requests.get(base_url)


def search_by_name(name):
    url = f"{base_url}?name={name}"
    return requests.get(url)


print(response.json())
print(search_by_name("Raj").json())
