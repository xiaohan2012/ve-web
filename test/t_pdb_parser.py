import os

from common import *
from pdb_parser import parse, group_by

class PdbParserTest(unittest.TestCase):
    def setUp(self):
        self.pdb_path = os.path.join(os.path.dirname(__file__), "1LSG.pdb")
        st = parse("1LSG.pdb",
              open(self.pdb_path).read())
        self.a,self.r,self.c = st.atoms, st.residues, st.chains

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
        self.assertEqual(len(self.r), 144)

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