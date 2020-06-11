import subprocess

from geonode_conabio.settings import HOST_NAME, PASSWORD_DB_GEONODE_DATA

def create_table_via_shp2pgsql(filename,
                               name_table):
    """
    Create table to postgresql geonode_data database using shp2pgsql.
    Will use ~/.geonode_conabio file to retrieve DB credentials.
    Args:
        filename (str): path of filename that will be used to create table in geonode_data DB.
        name_table (str): name of table that will be created in geonode_data DB.
    Returns:
        list: (int): first position number 0 means executed cmd ok.
              (out, err): second and third positions as described in https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate
    """
    print(name_table)
    cmd1 = ["shp2pgsql",
            filename,
            name_table,
            "public." + name_table + ".shp"]
    cmd2 = ["psql",
            "-q",
            "-h",
            HOST_NAME,
            "-d",
            "geonode_data",
            "-U", 
            "geonode",
           ]
    p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stderr=subprocess.PIPE,
                          env={"PGPASSWORD": PASSWORD_DB_GEONODE_DATA})
    out, err = p2.communicate()
    result = p2.poll()
    p1.terminate()
    p2.terminate()
    
    return [result, out, err]
