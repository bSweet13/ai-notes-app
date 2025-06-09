import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def app():
    app = create_app('testing')
    return app

@pytest.fixture
def test_client(app):
    return app.test_client()

@pytest.fixture
def init_database(app):
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

def test_create_user(init_database):
    user = User(
        email='test@example.com',
        cognito_sub='12345678-1234-1234-1234-123456789012'
    )
    db.session.add(user)
    db.session.commit()

    saved_user = User.query.filter_by(email='test@example.com').first()
    assert saved_user is not None
    assert saved_user.email == 'test@example.com'
    assert saved_user.cognito_sub == '12345678-1234-1234-1234-123456789012'
    assert saved_user.created_at is not None 