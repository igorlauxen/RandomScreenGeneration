import unittest

from src.Field import Field
from src.TypeEnum import TypeEnum

class FieldTest(unittest.TestCase):

    def setUp(self):
        self.field1 = Field(1)

    def test_generatedType(self):
        self.assertTrue(TypeEnum.has_value(self.field1.type), 'Type was not found, please verify creation of Type')

if __name__ == "__main__":
    unittest.main()
