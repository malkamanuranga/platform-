from fastapi.testclient import TestClient

from app import main

client = TestClient(main.app)


def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_readyz_ready():
    r = client.get("/readyz")
    assert r.status_code == 200


def test_readyz_not_ready(monkeypatch):
    monkeypatch.setattr(main, "_ready", False)
    r = client.get("/readyz")
    assert r.status_code == 503


def test_metrics_exposed():
    client.get("/healthz")
    r = client.get("/metrics")
    assert r.status_code == 200
    assert "http_requests_total" in r.text
