from django.test import TestCase


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
        response = self.client.get('/horoscope/7/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/horoscope/libra/')
