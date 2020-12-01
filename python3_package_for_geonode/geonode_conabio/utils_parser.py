import xml.etree.ElementTree as ET

def parse_sld_madmex_style(style_source_path):
    """
    Function for parsing sld MAD-Mex style.
    Args:
        style_source_path (str): path of sld MAD-Mex style
    Return:
        rf_children (list): list of child elements related to ColorMapEntry Element.
    """
    root = ET.parse(style_source_path).getroot()
    ns = "http://www.opengis.net/sld"
    rf = root.find('ns:UserLayer/ns:UserStyle/ns:FeatureTypeStyle/ns:Rule/ns:RasterSymbolizer/ns:ColorMap',
                   namespaces={'ns': ns})
    return list(rf)