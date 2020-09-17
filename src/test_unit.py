#!/usr/bin/env python

import pytest
import database

@pytest.fixture
def db_mock():
    return database.Database("src/data/db.json")

def test_balance(db_mock):
    assert db_mock.balance("ACCT100") == "40.00 USD"
    assert db_mock.balance("ACCT200") == "-10.00 USD"
    assert db_mock.balance("ACCT300") == "0.00 USD"
    assert db_mock.balance("nick123") is None

def test_owes_money(db_mock):
    assert db_mock.owes_money("ACCT100")
    assert not db_mock.owes_money("ACCT200")
    assert not db_mock.owes_money("ACCT300")
    assert db_mock.owes_money("nick123") is None
