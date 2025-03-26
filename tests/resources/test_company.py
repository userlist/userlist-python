import pytest

from userlist.resources.company import Company
from userlist.resources.relationship import Relationship


def test_company_creation_with_basic_fields():
    company = Company({"identifier": "company-123"})
    assert company.data["identifier"] == "company-123"


def test_company_creation_with_all_fields():
    data = {
        "identifier": "company-123",
        "name": "Test Company",
        "signed_up_at": "2025-03-25T12:00:00Z",
        "properties": {"industry": "tech"},
        "relationships": [],
    }
    company = Company(data)
    assert company.data == data


def test_company_creation_with_none_data():
    with pytest.raises(ValueError, match="data parameter is required"):
        Company(None)


def test_company_creation_with_string():
    company = Company("company-123")
    assert company.data["identifier"] == "company-123"


def test_company_missing_attr():
    company = Company({"identifier": "company-123"})
    with pytest.raises(AttributeError):
        _ = company.non_existent_attribute
