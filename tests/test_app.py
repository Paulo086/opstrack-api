from app import app


def test_home_route_returns_success_and_message():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Olá! A API Opstrack está funcionando!"
