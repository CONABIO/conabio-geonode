import subprocess

def create_table_via_shp2pgsql(filename,
                               name_table):
    """
    Create table to postgresql geonode_data database using ~/.pgpass and shp2pgsql
    The file ~/.pgpass has 0600 permissions and line like:
        hostname:port:database:username:password
    Args:
        filename (str): path of filename that will be used to create table in geonode_data DB.
        name_table (str): name of table that will be created in geonode_data DB.
    """
    name_table = name_table.lower()
    print(name_table)
    cmd1 = ["shp2pgsql",
            filename,
            name_table,
            "public." + name_table + ".shp"]
    cmd2 = ["psql",
            "-q",
            "-h",
            "geonode.conabio.gob.mx",
            "-d",
            "geonode_data",
            "-U", 
            "geonode"]
    p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stderr=subprocess.PIPE)
    out, err = p2.communicate()
    result = p2.poll()
    p1.terminate()
    p2.terminate()
    
    return [result, name_table, out, err]