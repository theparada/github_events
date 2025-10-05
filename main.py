import requests
import sys

def get_events(username, lines = 5):
    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url)
    events = response.json()
    for event in events[:lines]:
        event_type = event.get('type')
        repo_name = event['repo']['name']
        date = event["created_at"]
        print(f'[{date}] -> type: {event_type}, at: {repo_name}')

if __name__ == "__main__":
    if len(sys.argv) == 3:
        get_events(sys.argv[1], int(sys.argv[2]))
    else:
        print('inserts arguments: username, # of lines')
