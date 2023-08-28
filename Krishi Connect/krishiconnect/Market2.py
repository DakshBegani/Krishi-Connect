import requests

api_key = '579b464db66ec23bdd000001420beab8b9a546d268d7c574c638dbe3'

api_url = 'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070'

def fetch_data(state):
    params = {
        'api-key': api_key,
        'format': 'json',
        'filters[state]': state,
    }

    try:
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            data = response.json()  
            return data
        else:
            print(f"Request failed with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return None

def display_district_data(data):
    if data:
        for record in data['records']:
            print("\nRecord:")
            print("State:", record['state'])
            print("District:", record['district'])
            print("Market:", record['market'])
            print("Commodity:", record['commodity'])
            print("Variety:", record['variety'])
            print("Grade:", record['grade'])
            print("Arrival Date:", record['arrival_date'])
            print("Min Price:", record['min_price'])
            print("Max Price:", record['max_price'])
            print("Modal Price:", record['modal_price'])

state = input("Enter the name of the state: ")

data = fetch_data(state)

if data:
    display_district_data(data)
else:
    print("No data found for the specified state and district.")
