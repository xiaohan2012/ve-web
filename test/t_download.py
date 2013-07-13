import urllib2

from common import *

from crawler import download_pdb_file

class PdbFileDownloaderTest(unittest.TestCase):
    def test_download_file_length(self):
        file_content = download_pdb_file("1LSG")
        actual = len(file_content)
        expected = 122472
        self.assertEqual(actual, expected)

    def test_not_downloadable_exception(self):
        actual = download_pdb_file("~~")
        expected = None
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()