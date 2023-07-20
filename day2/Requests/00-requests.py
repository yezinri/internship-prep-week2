import requests

def main():
    response = requests.get('http://www.google.com')
    print(response)
    print(response.status_code)
    print(response.headers['Content-Type'])
    print("Content:", response.text)


if __name__ == "__main__":
    main()