import os

from common import *
from pdb_parser import parse, group_by

class PdbParserTest(unittest.TestCase):
    def setUp(self):
        self.pdb_path = os.path.join(os.path.dirname(__file__), "1LSG.pdb")
        st = parse("1LSG.pdb",
              open(self.pdb_path).read())
        self.a,self.r,self.c = st.atoms, st.residues, st.chains

        self.st = st
        
    def test_atom_content(self):
        a = self.a[0]
        
        self.assertEqual(a.id, 1)
        self.assertEqual(a.element, "N")

        self.assertEqual(a.x, 18.165)
        self.assertEqual(a.y, 12.653)
        self.assertEqual(a.z, 2.904)
                         
        self.assertEqual(a.residue_id, 1)
        self.assertEqual(a.residue_name, "MET")
        self.assertEqual(a.chain_id, "A")
        self.assertEqual(a.ins_res, " ")
        self.assertEqual(a.ail, " ")
        
    def test_atom_count(self):
        self.assertEqual(len(self.a), 1110)
        
    def test_residue_count(self):
        """if total residue count is correct"""
        self.assertEqual(len(self.r), 144)

    def test_residue_atom_count(self):
        """by sampling the 51th residue if residue's atom count is correct"""
        self.assertEqual(len(self.r[50]), 6)
        
    def test_atom_residue(self):
        """if atom's residue is paired correctly"""
        self.assertEqual(self.a[0].residue.id, 1)
        self.assertEqual(self.a[45].residue.id, 6)

    def test_atom_chain(self):
        """if atom's chain is paired correctly"""
        self.assertEqual(self.a[11].chain.id, "A")
        self.assertEqual(self.a[1100].chain.id, "A")

    def test_residue_chain(self):
        """if residue's chain is paired correctly"""
        self.assertEqual(self.r[11].chain.id, "A")
        self.assertEqual(self.r[100].chain.id, "A")

    def test_json_atom_content(self):
        """test atom json content"""
        actual = self.a[0].prepare_json()
        expected = {'position': (18.165, 12.653, 2.904), 'id': 1, 'element': 'N'}
        self.assertEqual(actual, expected)
        
    def test_json_residue_content(self):
        """after to json, check the first residue's content"""
        actual = self.r[0].prepare_json()
        expected = {'id': 1, 'atoms': [1, 2, 3, 4, 5, 6, 7, 8]} 
        self.assertEqual(actual, expected)

    def test_json_chain_content(self):
        """chain json content"""
        actual = len(self.c[0].prepare_json()["residues"])
        expected = 1110
        self.assertEqual(actual, expected)

            
class GroupByTest(unittest.TestCase):
    """test for the group by function"""
    
    def test_general_case(self):
        lst = [("540","feng"), ("540", "xiao"), ("541", "deng"), ("541", "guo"), ("542", "yu")]
        actual = group_by(lst, key = lambda tpl: tpl[0], val_mapping = lambda tpl: tpl[1])
        expected = {"542": ["yu"],
                    "540":["feng","xiao"],
                    "541":["deng", "guo"]}
        
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()        