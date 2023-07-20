import requests
import secrets

def main():
    payload = {
        "access_key": secrets.API_KEY,
        # "base": "KRW",
        "symbols": "GBP,JPY,EUR"
    }
    response = requests.get("http://api.exchangeratesapi.io/v1/latest", params=payload)

    print(response.status_code)
    print(response.headers['Content-Type'])
    # print(response.text)
    response_json = response.json()
    print(response_json['success'])
    print(response_json['timestamp'])



if __name__ == "__main__":
    main()