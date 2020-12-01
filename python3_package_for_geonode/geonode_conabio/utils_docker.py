from docker import APIClient

from geonode_conabio.settings import HOST_NAME, USER_GEOSERVER, PASSWORD_GEOSERVER

def publish_featuretype_via_docker(native_name, epsg_code="EPSG:4326"):
    """
    Function that publishes already registered vector file in postgresql database called geonode_data
    in geoserver. This will stablish SRS as EPSG 4326 and compute from data and native bounds (bounding box).
    Uses gsconfig package to programatically publish vector file.
    See: https://docs.geoserver.org/latest/en/user/gettingstarted/shapefile-quickstart/index.html
    See: https://github.com/GeoNode/geoserver-restconfig
    Args:
        native_name (str): name of table in geonode_data database.
    Return:
        ex_start (str): output of geonode spcgeonode_django_1 docker container. If success string is empty.
    """
    
    c = APIClient(base_url='unix://var/run/docker.sock')
    
    string = "from geoserver.catalog import Catalog;"
    string2 = "cat = Catalog("
    HOST_GEOSERVER = 'http://' + HOST_NAME + '/geoserver/rest'
    string3 = "store = cat.get_stores(names=['geonode_data'], workspaces=['geonode']);"
    string4 = "cat.publish_featuretype(native_name, store[0], epsg_code, native_name=native_name)"

    string = "".join([string, string2, "\'",
                      HOST_GEOSERVER, "\',\'",
                      USER_GEOSERVER, "\', ", "\'", PASSWORD_GEOSERVER, "\');",
                      string3,
                      "native_name = \'", native_name, "\';", 
                      "epsg_code = \'", epsg_code, "\';", 
                      string4])
    cmd = "".join(["python -c ", "\"", string, "\""])
    ex = c.exec_create(container = 'spcgeonode_django_1', 
                       cmd = cmd)
    ex_start = c.exec_start(exec_id=ex) #if arg stream=True in exec_start method, then returns generator
    return ex_start
def update_layers_via_docker(layer_name):
    """
    Wrapper for updatelayers command of geonode using docker-py functionality.
    Args:
        layer_name (str): name of layer registered in geoserver
    Returns:
        ex_start (str): result of exec_start method of docker-py
    """
    
    c = APIClient(base_url='unix://var/run/docker.sock')
    cmd = "".join(["python manage.py updatelayers -s geonode_data -w geonode -f ",
                   layer_name, " ",
                   "--settings=geonode.local_settings"])
    ex = c.exec_create(container = 'spcgeonode_django_1', 
                       cmd = cmd)
    ex_start = c.exec_start(exec_id=ex) #if arg stream=True in exec_start method, then returns generator
    return ex_start
def import_layers_via_docker(region, name, title,
                             abstract, keywords, 
                             filename):
    """
    Wrapper for importlayers command of geonode using docker-py functionality.
    Args:
        region (str): name of region registered in geonode
        name (str): name of layer that will be registered in geonode
        title (str): title of layer that will be registered in geonode
        abstract (str): abstract of layer that will be displayed in geonode
        keywords (str): keywords of layer that will be displayed in geonode
        filename (str): path of layer that will be registered in geonode
    Returns:
        ex_start (str): result of exec_start method of docker-py    
    """
    c = APIClient(base_url='unix://var/run/docker.sock')
    cmd = "".join(["python manage.py importlayers -v 3 -i -o ",
                   "-n ", name, " ",
                   "-t ", title, " ",
                   "-a ", abstract, " ",
                   "-k ", keywords, " ",
                   "-r ", region, " ",
                   filename, " ",
                   "--settings=geonode.local_settings"])
    ex = c.exec_create(container = 'spcgeonode_django_1', 
                       cmd = cmd)
    ex_start = c.exec_start(exec_id=ex) #if arg stream=True in exec_start method, then returns generator
    
    return ex_start
def retrieve_layer_and_style_registered_in_geonode(title_layer):
    """
    Wrapper to retrieve layer and style names already registered in geonode.
    Args:
        title_layer (str): name of title of layer registered in geonode
    Returns:
        ex_start (str): result of exec_start method of docker-py
    """
    c = APIClient(base_url='tcp://172.17.0.1:1111')
    #c = APIClient(base_url='unix://var/run/docker.sock')
    string1 = """import os;\
    import django;\
    os.chdir('/spcgeonode');\
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geonode.local_settings');\
    django.setup();\
    from geonode.base.models import Link;\
    from geonode.layers.models import Layer;\
    """
    string2 = "layer = Layer.objects.filter(title="                                       
    string3 = ").first();"
    string4 = "style_name = layer.default_style.name;"
    string5 = "layer_name = layer.name;"
    string = "".join([string1, 
                      "title_layer = \'", title_layer, "\';",
                      string2, "\'",
                      title_layer, "\'", 
                      string3,
                      string4,
                      string5,
                      "print(layer_name);",
                      "print(style_name)"])
    cmd = "".join(["python -c ", "\"", string, "\""])
    ex = c.exec_create(container = 'spcgeonode_django_1', 
                   cmd = cmd)
    ex_start = c.exec_start(exec_id=ex) #if arg stream=True in exec_start method, then returns generator
    return ex_start