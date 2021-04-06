# img_viewer.py

from layout import *
import os.path
import logging

from utils import *

# Level of warnings
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.INFO)

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

        #attributes={fileName:[] for fileName in fnames}

        logging.info('Filename at START: {}'.format(filename))
        update_img(filename, window)

    elif event == 'Next':
        try:
            idx += 1
            filename = os.path.join(
                values["-FOLDER-"], fnames[idx]
            )
            logging.info('Filename after NEXT: {}'.format(filename))
            logging.info('Values of values_array: {}'.format(values))
            logging.info("Type of values is: {}".format(type(values)))
            attributes=pre_process_dict(values)
            logging.info("Attributes after process: {}".format(attributes))
            logging.info("Values after process: {}".format(values))
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