# tests/test_validation.py
# TODO: once ExpenseIn / Money exist, port the three attacks from class
# into parametrized tests here:
#   - negative amount returns 422
#   - amount > 10000 returns 422
#   - Cyrillic homoglyph payer is rejected
#   - currency outside the allowlist is rejected
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

URL = "/api/groups/1/expenses"
VALID = {"amount": 12.5, "payer": "alice", "payer_email": "alice@x.com"}


# Attack 1: "free money" — a negative amount was accepted with HTTP 200
def test_negative_amount_rejected():
    r = client.post(URL, json={**VALID, "amount": -500})
    assert r.status_code == 422
    assert r.json()["detail"][0]["loc"] == ["body", "amount"]


# Attack 1 variants (slide 8 + slide 23): zero, too big, overflow, NaN, too many decimals
@pytest.mark.parametrize("amount", [-1, 0, 10000.01, 100001, 1e308, "NaN", 12.345])
def test_invalid_amounts_rejected(amount):
    r = client.post(URL, json={**VALID, "amount": amount})
    assert r.status_code == 422
    assert r.json()["detail"][0]["loc"] == ["body", "amount"]
