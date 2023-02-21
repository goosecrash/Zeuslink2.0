import requests

def get_total_supply():
    try:
        response = requests.get('http://localhost:8080/total_supply')
        response.raise_for_status()  # Raise an exception if the response status code is not 200
        return int(response.text)
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

if __name__ == '__main__':
    total_supply = get_total_supply()
    if total_supply is not None:
        print(f'Total supply: {total_supply}')
