import requests

# Replace with the actual API endpoint and parameters
API_ENDPOINT = "https://api.example.com/train_status"
API_KEY = "your_api_key"


def get_train_status(19494, 2/july/2024):
    params = {
        'train_number': train_number,
        'date': date,
        'api_key': API_KEY
    }
    response = requests.get(API_ENDPOINT, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


train_number = "12345"  # Example train number
date = "2024-07-01"  # Date in YYYY-MM-DD format

status = get_train_status(train_number, date)

if status:
    if status['is_cancelled']:
        print(f"Train {train_number} is cancelled on {date}.")
    else:
        print(f"Train {train_number} is running on {date}.")
else:
    print("Failed to fetch train status.")