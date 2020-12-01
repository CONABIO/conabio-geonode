def hex_to_rgba(hex_code):
    """
    Helper function to transform hexadecimal code to rgba values
    Args:
        hex_code (str): hexadecimal code of color, example: #FF0000
    Returns:
        tuple: RGBA value, example: (255, 0, 0, 255)
    """
    return tuple(int(hex_code[i:i+2], 16) for i in (1, 3 ,5)) + (255,)

def get_cmap_from_element_list_madmex_style(l):
    """
    Convert list of child elements related to ColorMapEntry element in sld MAD-Mex style to dictionary.
    Args:
        l (list): list of child elements related to ColorMapEntry Element.
    Return:
        rgb_dict (dict): dictionary with keys related to pixel values of raster and values related to color RGBA values.
    """
    hex_dict = dict([(int(i.attrib["quantity"]), i.attrib["color"]) for i in l])
    rgb_dict = {k:hex_to_rgba(v) for k,v in hex_dict.items()}
    rgb_dict[0] = (0,0,0,0)
    return rgb_dict