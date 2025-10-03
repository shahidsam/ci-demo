from app import app

def test_home():
    client =app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello! Your CI/CD pipeline deployed this Flask App" in response.data

def test_add():
    client = app.test_client()
    response = client.get("/add/3/4")
    assert response.status_code == 200
    assert b"The sum of 3 and 4 is 7" in response.data

    