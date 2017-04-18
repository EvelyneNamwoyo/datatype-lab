from datatypeslab import data_type
import unittest
class DataTypeTestCase(unittest.TestCase):

  def test_none_type(self):
    self.assertEqual('no value', data_type(None))

  def test_array_type(self):
    self.assertEqual(3, data_type([1, 2, 3]))

  def test_small_array_type(self):
    self.assertEqual(None, data_type([1, 2]))

  def test_small_booleans_type(self):
    self.assertEqual(True, data_type(True))

  def test_small_integer_type(self):
    self.assertEqual('less than 100', data_type(3))

  def test_large_integer_type(self):
    self.assertEqual('more than 100', data_type(200))
  
  def test_str_type(self):
    self.assertEqual(6, data_type('andela'))
  def test_empty_string(self):
    self.assertEqual( data_type(' '), 'Cannot allow empty strings')
  def test_empty_string(self):
    self.assertEqual( data_type(''), 'Cannot allow empty strings')
  def test_for_invalid_input_dict(self):
    with self.assertRaises(ValueError):
      result=data_type({})
  def test_for_invalid_input_set(self):
    with self.assertRaises(ValueError):
      result=data_type(set())

if __name__ == "__main__":
    unittest.main()