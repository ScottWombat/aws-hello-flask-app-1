import requests
from app.utils.NumberValidationException import NumberValidationException
def test_index_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/login')
    assert response.status_code == 200


def check_existence(number):
    try:
        response = requests.get('http://127.0.0.1:5000/', params={'number': number}) # 1
        response.raise_for_status() # 2
        return response.json()['exists'] # 3
    except (requests.exceptions.HTTPError, KeyError) as e: # 4
        raise NumberValidationException('something went wrong when calling api') from e