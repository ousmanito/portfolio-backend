from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class TestPostEndpoint(APITestCase):
    def setUp(self):
        # Créez un utilisateur pour tester l'authentification.
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_get_experience(self):
        # Authentifiez l'utilisateur.
        self.client.login(username="testuser", password="testpassword")

        # Faites votre requête.
        response = self.client.get("/api/Experience/")

        # Assurez-vous que la requête a réussi.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_experience(self):
        self.client.login(username="testuser", password="testpassword")
        data = {
            "title": "Chapitre 3",
            "position": "Developpeur Django",
            "start_date": "2022-07-29",
            "end_date": "2023-12-07",
        }
        response = self.client.post("/api/Experience/", data)
        print(response.status_code)

    def test_get_experience_unauthenticated(self):
        # Faites votre requête sans authentifier l'utilisateur.
        response = self.client.get("/api/Experience/")

        # Assurez-vous que la requête a échoué à cause de l'absence d'authentification.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
