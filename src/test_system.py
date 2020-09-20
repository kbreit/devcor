#!/usr/bin/env python

import requests
import pytest

@pytest.fixture()
def kwargs():
    requests.packages.urllib3.disable_warnings()
    return {
        "url": "https://localhost:5000",
        "verify": False,
        "headers": {"Accept": "text/html"},
    }

def test_get_good_page(kwargs):
    resp = requests.get(**kwargs)
    assert resp.status_code == 200
    assert "Enter account ID" in resp.text

def test_get_bad_page(kwargs):
    kwargs["url"] = "https://localhost:5000/bad.html"
    resp = requests.get(**kwargs)
    assert resp.status_code == 404
    assert "Not Found" in resp.text

def test_post_good_acct(kwargs):
    _post_acct(kwargs, {"acctid": "ACCT100", "acctbal": "40.00 USD"})
    _post_acct(kwargs, {"acctid": "ACCT200", "acctbal": "-10.00 USD"})
    _post_acct(kwargs, {"acctid": "ACCT300", "acctbal": "0.00 USD"})

def test_post_bad_acct(kwargs):
    _post_acct(kwargs, {"acctid": "nick123"})

def _post_acct(kwargs, acct):
    kwargs["headers"].update(
        {"Content-Type": "applicatin/x-www-form-urlencoded"})
    resp = requests.post(**kwargs, data=f"accid={acct['acctid']}")
    assert resp.status_code == 200
    balance = acct.get("acctbal")
    if balance:
        assert f"Account balance: {balance}" in resp.text
    else:
        assert "Unknown account number" in resp.text

