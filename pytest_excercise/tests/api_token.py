import requests
from faker import Faker

def get_api_token():
    # Endpoint do uzyskania tokenu
    url = "https://simple-books-api.click/api-clients"
    fake = Faker()
    fake_client_name  = fake.first_name() + " " + fake.last_name()
    fake_email = fake.email()

    print(fake_client_name)
    print(fake_email)

    # Dane wymagane do rejestracji i uzyskania tokenu
    payload = {
        "clientName": fake_client_name,
        "clientEmail": fake_email
    }

    # Wysłanie żądania POST
    response = requests.post(url, json=payload)

    # Sprawdzenie odpowiedzi
    if response.status_code == 201:
        token = response.json().get("accessToken")
        return token
    else:
        print("Błąd:", response.status_code, response.text)

if __name__ == "__main__":
    api_token = get_api_token()
    print(api_token)
