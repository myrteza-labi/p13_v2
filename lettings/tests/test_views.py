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
