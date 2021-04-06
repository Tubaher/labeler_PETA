# img_viewer.py

from layout import *
import os.path
import logging
import PIL
from PIL import Image, ImageTk
import io


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

# Level of warnings
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.NOTSET)

# Dictionary of labels
labels = {}

# idx to an element in the folder
idx = 0
# Run the Event Loop

def update_img(filename, window):
    ''' 
    Update the frame where the image is shown
    input: name of the updated file
            window where the update is done
    output: image window updated 
    '''
    window["-TOUT-"].update(filename)
    window["-IMAGE-"].update(data=get_img_data(filename))

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".jpg"))
        ]
        filename = os.path.join(
                values["-FOLDER-"], fnames[idx]
            )
        logging.info('Filename at START: {}'.format(filename))
        update_img(filename, window)
        #window["-TOUT-"].update(filename)
        #window["-IMAGE-"].update(data=get_img_data(filename))

    elif event == 'Next':
        try:
            idx += 1
            filename = os.path.join(
                values["-FOLDER-"], fnames[idx]
            )
            logging.info('Filename after NEXT: {}'.format(filename))
            update_img(filename, window)
        except:
                pass
    elif event == 'Back':
        try:
            if idx !=0:
                idx -= 1
                filename = os.path.join(
                    values["-FOLDER-"], fnames[idx]
                )
                logging.info('Filename after NEXT: {}'.format(filename))
                update_img(filename, window)
        except:
                pass


    
window.close()