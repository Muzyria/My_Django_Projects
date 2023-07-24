from django.test import TestCase
from . import views

# Create your tests here.


class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEquals(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEquals(response.status_code, 200)
        self.assertIn("Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
                      response.content.decode())

    def test_libra_redirect(self):
        for key, value in enumerate(list(views.signs), 1):
            response = self.client.get(f'/horoscope/{key}/')
            self.assertEquals(response.status_code, 302)
            self.assertEquals(response.url, f'/horoscope/{value}/')

    def test_signs(self):

        for key, value in views.signs.items():
            response = self.client.get(f'/horoscope/{key}/')
            self.assertEquals(response.status_code, 200)
            self.assertIn(value[1], response.content.decode())
