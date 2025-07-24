import pytest
from project import add_income, add_expense, display_summary, filter_by_category

def test_add_income():
    transactions = []
    add_income(transactions, 100, "salary")
    assert len(transactions) == 1
    assert transactions[0]["type"] == "income"
    assert transactions[0]["amount"] == 100
    assert transactions[0]["category"] == "salary"

def test_add_expense():
    transactions = []
    add_expense(transactions, 50, "food")
    assert len(transactions) == 1
    assert transactions[0]["type"] == "expense"
    assert transactions[0]["amount"] == 50
    assert transactions[0]["category"] == "food"

def test_display_summary():
    transactions = [
        {"type": "income", "amount": 100, "category": "salary"},
        {"type": "expense", "amount": 50, "category": "food"}
    ]
    display_summary(transactions)

def test_filter_by_category():
    transactions = [
        {"type": "income", "amount": 100, "category": "salary"},
        {"type": "expense", "amount": 50, "category": "food"},
        {"type": "expense", "amount": 30, "category": "food"}
    ]
    filtered = filter_by_category(transactions, "food")
    assert len(filtered) == 2
    assert filtered[0]["category"] == "food"
    assert filtered[1]["category"] == "food"
