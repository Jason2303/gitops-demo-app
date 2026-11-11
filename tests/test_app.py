from app.main import app


def client():
    app.config.update(TESTING=True)
    return app.test_client()


def test_index_returns_metadata():
    resp = client().get("/")
    assert resp.status_code == 200
    body = resp.get_json()
    assert "version" in body
    assert "environment" in body


def test_healthz():
    resp = client().get("/healthz")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_readyz():
    resp = client().get("/readyz")
    assert resp.status_code == 200


def test_version():
    resp = client().get("/version")
    assert resp.status_code == 200
    assert "version" in resp.get_json()
