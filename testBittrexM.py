import unittest
from BittrexM import Bittrex

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.bittrex = Bittrex()
    def get_order_book(self):
        url = 'https://bittrex.com/api/v1.1/public/getorderbook'
        params = {'market': pair, 'type': type}
        self.assertTrue(requests.get(url, params)==200)


suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner().run(suite)
