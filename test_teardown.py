import pytest

@pytest.fixture
def account():
    print("[setup]")
    yield "account"
    print("[teardown]")

def test_first(account):
    assert account == "account"

def test_second(account):
    assert account == "account"
