import pytest
from django.urls import reverse
from lettings.models import Address, Letting

@pytest.mark.django_db
def test_lettings_index_view(client):
    # Setup : on crée une entrée pour vérifier l’affichage
    address = Address.objects.create(
        number=99,
        street="Test Street",
        city="Testville",
        state="TS",
        zip_code=12345,
        country_iso_code="TST"
    )
    Letting.objects.create(title="Test Letting", address=address)

    # Appel de la vue
    url = reverse("lettings:index")
    response = client.get(url)

    # Vérifications
    assert response.status_code == 200
    assert "Test Letting" in response.content.decode()
    assert "lettings/index.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_letting_detail_view(client):
    address = Address.objects.create(
        number=5,
        street="Rue des Tests",
        city="TestCity",
        state="TC",
        zip_code=54321,
        country_iso_code="TST"
    )
    letting = Letting.objects.create(title="Letting Detail Test", address=address)

    url = reverse("lettings:letting", args=[letting.id])
    response = client.get(url)

    assert response.status_code == 200
    assert "Letting Detail Test" in response.content.decode()
    assert "lettings/letting.html" in [t.name for t in response.templates]
