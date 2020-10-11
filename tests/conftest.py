import os
import pytest
from urllib.parse import quote
from normalize import NumberValidationException 
from app import create_app 
from app.models import User

@pytest.fixture(scope='module')
def new_user():
    user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
    return user


@pytest.fixture(scope='module')
def test_client():
    #flask_app = create_app('flask_test.cfg')
    flask_app = create_app()
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

@pytest.fixture
def api_response(): # 1
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        rsps.add(responses.GET, 'http://127.0.0.1:8080/?number='+quote('+31'), # 2
                 json={'exists': False}, status=200)
        rsps.add(responses.GET, 'http://127.0.0.1:8080/?number=' + quote('+3155512345'),
                 json={'exists': True}, status=200)
        rsps.add(responses.GET, 'http://127.0.0.1:8080/?number=' + quote('+311234555'),
                 json={'exists': True}, status=200)
        yield rsps # 3