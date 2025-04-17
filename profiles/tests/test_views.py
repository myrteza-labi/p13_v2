import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

@pytest.mark.django_db
def test_profiles_index_view(client):
    user = User.objects.create(username="testuser")
    Profile.objects.create(user=user, favorite_city="Paris")

    url = reverse("profiles:index")
    response = client.get(url)

    assert response.status_code == 200
    assert "testuser" in response.content.decode()
    assert "profiles/index.html" in [t.name for t in response.templates]
