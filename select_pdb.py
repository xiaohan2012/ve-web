import tornado.web

from db import db

from tornado.escape import json_encode

PDB_STR_COL_NAME = "pdb_str"
class SelectPDBHandler(tornado.web.RequestHandler):
    def get(self, structure_id):
        print "structure id", structure_id
        if db[PDB_STR_COL_NAME].find_one({"structure_id": structure_id}) == None:
            from crawler import download_pdb_file
            pdb_str = download_pdb_file(structure_id)
            if pdb_str is None:
                #pdb id not found, return 500 code
                self.set_status(500)
                
                self.write(json_encode({
                    "pdb_id": structure_id,
                    "status":"not found"
                }))

            else:
                #find one from pdb bank
                db[PDB_STR_COL_NAME].insert({
                    "structure_id": structure_id,
                    "content": pdb_str
                })
                self.write(json_encode({
                    "pdb_id": structure_id,
                    "status":"inserted"
                }))
        else:
            #it just exists in our db
            self.write(json_encode({
                "pdb_id": structure_id,
                "status":"exist"
            }))
