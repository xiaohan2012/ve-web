from UserList import UserList
from simplejson import dumps

class Structure(object):
    def __init__(self, structure_id, chains = [], residues = [], atoms = []):
        """(str, list of Residue)"""
        self._id = structure_id
        self.residues = residues
        self.chains = chains
        self.atoms = atoms
                
    def prepare_json(self):
        return {
            "atoms": [a.prepare_json() for a in self.atoms],
            "residues":[r.prepare_json() for r in self.residues],
            "chains": [c.prepare_json() for c in self.chains],
        }
        
class Chain(UserList):
    def __init__(self, chain_id, residues):
        self.residues = residues
        self.id = chain_id
        super(Chain,self).__init__(residues)

    def prepare_json(self):
        return {
            "id": self.id,
            "residues": [r.id for r in self.residues]
        }
        
        
class Residue(UserList):
    def __init__(self, residue_id,  chain_id, atoms = []):
        self.id = residue_id
        
        self.chain = None
        self.chain_id = chain_id
        self.atoms = atoms

        super(Residue,self).__init__(atoms)
        
    def prepare_json(self):
        return {"id": self.id, "atoms": [a.id for a in self.atoms]}
        
class Atom(object):
    def __init__(self, id,  element, xyz, residue_name, residue_id, chain_id, ins_res, ail):
        self.id = id
        self.element = element
        self.xyz = xyz
        self.x, self.y, self.z = self.xyz
        
        self.residue = None
        self.residue_id = residue_id
        self.residue_name = residue_name
        
        self.chain = None
        self.chain_id = chain_id
        
        self.ins_res = ins_res
        self.ail = ail

    def prepare_json(self):
        return {"id": self.id, "element": self.element, "position": self.xyz}
        
    def __str__(self):
        return "%s at %f %f %f of residue %d(%s) of chain %s" %(self.element, self.x, self.y, self.z,
                                                                self.residue_id, self.residue_name, self.chain_id)
    def __repr__(self):
        return str(self)

def group_by(lst, key = lambda v:v, val_mapping = lambda v:v ):
    """take a list a group the items by give `key` function"""
    vals = set(map(key, lst))
    return dict([(v, [val_mapping(l)
                      for l in lst if key(l) == v])
                 for v in vals])
    
def parse(structure_id, string):
    lines = string.split("\n")
    atom_lines = [l for l in lines if l[:4] == "ATOM"]

    atoms = [Atom(id = int(l[6:11].strip()),
                  element = l[12:16].strip(),
                  xyz = (
                      float(l[30:38].strip()),
                      float(l[38:46].strip()),
                      float(l[46:54].strip())
                  ),
                  residue_name = l[17:20].strip(),
                  residue_id = int(l[22:26].strip()),
                  chain_id = l[21:22].strip(),
                  ins_res = l[26:27],
                  ail = l[16:17]
              ) for l in atom_lines]
    
    atoms_by_residue = group_by(atoms, key = lambda a: a.residue_id)
    atoms_by_chain = group_by(atoms, key = lambda a: a.chain_id)

    chains = [Chain(chain_id, ats) for chain_id, ats in atoms_by_chain.items()]

    residues = [Residue(res_id, ats[0].chain_id, ats) for res_id, ats in atoms_by_residue.items()]

    #rebind phase, chicken-egg problem
    resid_to_res = dict([(res.id, res) for res in residues])
    chainid_to_chain = dict([(chain.id, chain) for chain in chains])

    for atom in atoms:
        atom.residue = resid_to_res[atom.residue_id]
        atom.chain = chainid_to_chain[atom.chain_id]
        
    for res in residues:
        res.chain = chainid_to_chain[res.chain_id]
        
    return Structure(structure_id, chains, residues, atoms)