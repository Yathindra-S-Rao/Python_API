import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    """Fetches a list of posts"""
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        posts = response.json()
        print(f"Retrieved {len(posts)} posts.")
        for post in posts[:5]:  # Print first 5 posts
            print(f"{post['id']}: {post['title']}")
    else:
        print("Failed to retrieve posts", response.status_code)

def get_users():
    response = requests.get(f"{BASE_URL}/users")
    if response.status_code == 200:
        users = response.json()
        for user in users:
            print(f"{user['name']}")


print(get_posts())
print(get_users())



