import PIL
from PIL import Image, ImageTk
import io
import pandas as pd
from attributes import attributes_list, df_attributes

def get_img_data(f, maxsize=[128, 256], first=False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img = img.resize(maxsize,PIL.Image.ANTIALIAS)
    
    # img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)


def pre_process_dict(windows_dict, image_name):
    """
    A function to change key values of False by 0 and True by 1. 
    """
    attributes_dict=windows_dict.copy()
    attributes_dict.pop('-FOLDER-') #Delete -FOLDER- key
    attributes_dict.pop('Browse')   #Delete -BROWSE- key
    attributes_dict['image_name'] = image_name 

    for key in attributes_dict:
        if attributes_dict[key]==False:
                attributes_dict[key]=0
        elif attributes_dict[key]==True:
                attributes_dict[key]=1
    return attributes_dict
    

def append_row(attribute_dict, idx):
    df_attributes.loc[idx] = attribute_dict
