import pytest
import requests
from pytest_excercise.tests.api_token import get_api_token

BASE_URL = "https://simple-books-api.click"
TOKEN = get_api_token()


@pytest.fixture(scope="module")
def order_id():
    """Tworzy zamówienie na potrzeby testów i zwraca jego ID."""
    url = f"{BASE_URL}/orders"
    headers = {"Authorization": TOKEN}
    payload = {"bookId": 1, "customerName": "Jan Kowalski"}

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201

    json_data = response.json()
    assert json_data.get("created") is True
    order_id = json_data.get("orderId")
    assert isinstance(order_id, str)

    yield order_id

    # Cleanup po testach - usunięcie zamówienia
    del_response = requests.delete(f"{BASE_URL}/orders/{order_id}", headers=headers)
    assert del_response.status_code == 204


def test_get_status():
    """Testuje status API."""
    response = requests.get(f"{BASE_URL}/status")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"


def test_get_books():
    """Testuje pobranie listy książek."""
    response = requests.get(f"{BASE_URL}/books")
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)
    assert len(books) > 0


def test_update_order(order_id):
    """Testuje aktualizację zamówienia."""
    url = f"{BASE_URL}/orders/{order_id}"
    headers = {"Authorization": TOKEN}
    payload = {"customerName": "John Nowak"}

    response = requests.patch(url, json=payload, headers=headers)
    assert response.status_code == 204


def test_delete_order_manual():
    """Testuje ręczne usunięcie zamówienia."""
    # Najpierw tworzymy zamówienie, żeby mieć co usunąć
    url = f"{BASE_URL}/orders"
    headers = {"Authorization": TOKEN}
    payload = {"bookId": 1, "customerName": "Delete Me"}

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201

    order_id = response.json().get("orderId")

    # Teraz usuwamy to zamówienie
    del_response = requests.delete(f"{BASE_URL}/orders/{order_id}", headers=headers)
    assert del_response.status_code == 204
