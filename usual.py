"""
A collection of basic python functions useful to ease life.
"""

import os
import xml.etree.ElementTree as ET


def get_subdirectories(directory):
    """
    List only the direct subdirectories of a given directory.
    Files are not included (difference with os.listdir)
    :param directory: path of the directory string
    :return: subdirectories
    :rtype: list
    """
    subdirectories = os.walk(directory).next()[1]
    return subdirectories


def merge_dicts(x, y):
    """
    Merge two dictionaries in Python
    :param x: a dictionary
    :param y: a dictionary
    :return: a dictionary
    """
    z = x.copy()  # start with x's keys and values
    z.update(y)  # modifies z with y's keys and values & returns None
    return z


def modify_bvproc(bvproc, old, new, modified_bvproc):
    """
    Replace all occurences of "old" pattern by "new" pattern in a bvproc (BrainVISA process, XML format) file and save the modified process in a new bvproc file
    :param bvproc: path of the bvproc file
    :param old: pattern to be replaced (usually subject identifier) (str)
    :param new: new pattern (usually other subject identifier) (str)
    :param modified_bvproc: path of the modified bvproc file
    :return: None
    """

    template_bvproc = ET.parse(bvproc)
    template_root = template_bvproc.getroot()
    for tag in template_root.iter("*"):
        init_value = tag.text
        # sometimes tag.text is empty (None) or different type
        if type(init_value) is str:
            new_value = init_value.replace(old, new)
            tag.text = new_value
    template_bvproc.write(modified_bvproc, encoding="utf-8", xml_declaration=True)