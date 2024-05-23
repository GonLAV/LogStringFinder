import unittest
from script import count_string_occurrences_in_file

class TestCountStringOccurrencesInFile(unittest.TestCase):
    def test_count_string_occurrences_in_file(self):
        test_file_path = 'test.txt'
        with open(test_file_path, 'w') as f:
            f.write('error\nwarning\nerror\n')
        
        search_strings = ['error', 'warning']
        expected = {'error': 2, 'warning': 1}
        result = count_string_occurrences_in_file(test_file_path, search_strings)
        self.assertEqual(result, expected)
        os.remove(test_file_path)

if __name__ == '__main__':
    unittest.main()

