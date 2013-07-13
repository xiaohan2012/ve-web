from urllib2 import Request, urlopen, HTTPError

def download_pdb_file(structure_id):
    """(strucure_id: str) => file_content: str

    """
    url = "http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId=%s" %structure_id
    try:
        res = urlopen(Request(url))
        return res.read()
    except HTTPError:
        return None


if __name__ == '__main__':
    download_pdb_file("2")