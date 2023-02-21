import requests

url = 'http://localhost:5000/total_supply'

try:
    response = requests.get(url, timeout=1)
    if response.status_code == 200:
        print('Total supply:', response.text)
    else:
        print('Error: Could not get total supply')
except requests.exceptions.RequestException as e:
    print('Error:', e)
