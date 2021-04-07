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
            logging.info('Filename before NEXT: {}'.format(filename))
            logging.info('Values of values_array: {}'.format(values))
            attributes=pre_process_dict(values, fnames[idx])
            logging.info("Attributes after process: {}".format(attributes))
            append_row(attributes, idx)
            logging.info("Dataframe df attributes: \n {}".format(df_attributes))
            
            idx += 1
            
            filename = os.path.join(values["-FOLDER-"], fnames[idx])
            update_img(filename, window)

                
        except:
            pass
    elif event == 'Back':
        # try:
        logging.info('Filename before BACK: {}'.format(filename))
        logging.info('Values of values_array: {}'.format(values))
        attributes=pre_process_dict(values, fnames[idx])
        logging.info("Attributes after process: {}".format(attributes))
        append_row(attributes, idx)
        logging.info("Dataframe df attributes: \n {}".format(df_attributes))

        idx -= 1

        filename = os.path.join(values["-FOLDER-"], fnames[idx])
        update_img(filename, window)

        #TODO Extract the data from the dataframe and update values_array
                
        # except:
        #         pass
    
    
    try:
        logging.critical('Index value: {}'.format(idx))
        if (idx+1) > (len(fnames)-1):
            window['Next'].update(disabled=True)
        elif (idx-1) < 0:
            window['Back'].update(disabled=True)
        else:
            window['Next'].update(disabled=False)
            window['Back'].update(disabled=False)
    except:
        pass


    
window.close()