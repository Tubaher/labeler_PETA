import PIL
from PIL import Image, ImageTk
import io
import pandas as pd


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


def pre_process_dict(original_dict):
    """
    A function to change key values of False by 0 and True by 1. 
    """
    output1=original_dict.copy()
    output1.pop('-FOLDER-') #Delete -FOLDER- key
    output1.pop('Browse')   #Delete -BROWSE- key

    for key in output1:
        if output1[key]==False:
                output1[key]=0
        else:
                output1[key]=1
    return output1
    

