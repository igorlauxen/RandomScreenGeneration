import unittest

from src.Screen import Screen


minFields = 10
maxFields = 20

class FieldTest(unittest.TestCase):

    def setUp(self):
        self.screen1 = Screen(1, minFields, maxFields)

    def test_generatedType(self):
        self.assertTrue(self.screen1.getFieldsLength() > 0, 'We dont have fields :(')
        self.assertTrue(self.screen1.getFieldsLength() < maxFields, 'We have more than expected')
        self.assertTrue(self.screen1.getFieldsLength() > minFields, 'We have less than expected')

if __name__ == "__main__":
    unittest.main()
