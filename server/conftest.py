from unittest.mock import patch

import pytest

with patch.dict("os.environ", {"FLASK_SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"}):
    from app import app, db


@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    with app.app_context():
        db.create_all()
        try:
            yield app.test_client()
        finally:
            db.session.remove()
            db.drop_all()
