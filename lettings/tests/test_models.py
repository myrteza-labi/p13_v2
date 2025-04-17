import pytest
from lettings.models import Address, Letting

@pytest.mark.django_db
def test_address_str():
    address = Address.objects.create(
        number=42,
        street="Wallaby Way",
        city="Sydney",
        state="NS",
        zip_code=2000,
        country_iso_code="AUS"
    )
    assert str(address) == "42 Wallaby Way"

@pytest.mark.django_db
def test_letting_str():
    address = Address.objects.create(
        number=221,
        street="B Baker Street",
        city="London",
        state="LD",
        zip_code=12345,
        country_iso_code="GBR"
    )
    letting = Letting.objects.create(
        title="Sherlock's Flat",
        address=address
    )
    assert str(letting) == "Sherlock's Flat"
