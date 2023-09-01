from django.test import TestCase
from .models import Game
from django.urls import reverse
# Create your tests here.
# Run the command "coverage run manage.py test blog -v 2"
# Run the command "coverage html"

class GameTest(TestCase):
    def setUp(self):
        self.game = Game.objects.create(
                title="Gaia Project",
                players=4,
                duration=90,
                designer="Jude Smiley",
                description="It is beautiful!"
            )
    
    def test_creation(self):
        self.assertEqual(self.game.title, "Gaia Project")
        self.assertEqual(self.game.players, 4)
        
    def test_str_method_returns_title(self):
        self.assertEqual(str(self.game), "Gaia Project")
    
    def test_game_list(self):
        url = reverse('game_list')
        response = self.client.get(url)
        print(response)
        self.assertEqual(200, response.status_code)
        self.assertIn("Number of games uploaded", str(response.content))