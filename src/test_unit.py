#!/usr/bin/env python

import pytest
import database

@pytest.fixture(scope="module")
def db_mock():
    return database.Database("sqlite:///:memory:", "src/data/initial.json")

def test_balance(db_mock):
    db_mock.connect()
    assert db_mock.balance("ACCT100") == "40.00 USD"
    assert db_mock.balance("ACCT200") == "-10.00 USD"
    assert db_mock.balance("ACCT300") == "0.00 USD"
    assert db_mock.balance("nick123") is None
    db_mock.disconnect()

