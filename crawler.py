from urllib2 import Request, urlopen

def download_pdb_file(structure_id):
    """(strucure_id: str) => file_content: str

    """
    url = "http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId=%s" %structure_id
    res = urlopen(Request(url))
    return res.read()