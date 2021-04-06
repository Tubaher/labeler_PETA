import PySimpleGUI as sg

# First the window layout in 2 columns
file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
    [sg.Button('Back'),
    sg.Button('Next'),
    sg.Button('Save')]
]

attributes_column1 = [
    
    [sg.Text("Choose the correct attribute:")],
    #[sg.Text(size=(40, 1), key="-TOUT1-")],
    [sg.Text(size=(40, 1), key="-SaveMessage-")],
    #[sg.Text("Age: "), sg.Button("16-30",disabled=False), sg.Button("31-45",disabled=False),sg.Button("46-60",disabled=False),sg.Button("Above 61",disabled=False)],
    [sg.Text("Age: "),sg.Radio('16-30  ', "Age", default=True, size=(10, 1)), sg.Radio('31-45    ', "Age"),sg.Radio('46-60    ', "Age"),sg.Radio('Above 61', "Age")],
    [sg.Text("Shoes: "),sg.Radio('Leather Shoes  ', "Shoes", default=True, size=(10, 1)), sg.Radio('Sandals    ', "Shoes"),sg.Radio('Shoes    ', "Shoes"),sg.Radio('Sneakers', "Shoes")],
    [sg.Text("Upper: "),sg.Radio('Casual  ', "Upper", default=True, size=(10, 1)), sg.Radio('Formal    ', "Upper")],
    [sg.Text("Lower: "),sg.Radio('Casual  ', "Lower", default=True, size=(10, 1)), sg.Radio('Formal    ', "Lower")],
    [sg.Checkbox('Backpack', default=False,key='Backpack')],
    #[sg.Text("Carrying Other: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Carrying Other', default=False,key='Carrying_Othere')],
    #[sg.Text("HAT: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('HAT', default=False,key='HAT')],
   # [sg.Text("Jacket: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Jacket', default=False,key='Jacket')],
    #[sg.Text("Jeans: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Jeans', default=False,key='Jeans')],
    #[sg.Text("Logo: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('LogoLogo', default=False,key='LogoLogo')],
    #[sg.Text("LongHair: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('LongHair', default=False,key='LongHair')],
    #[sg.Text("Male: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Male', default=False,key='Male')],
    #[sg.Text("Messenger Bag: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Messenger Bag', default=False,key='Messenger_Bag')],
    #[sg.Text("Muffler: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Muffler', default=False,key='Muffler')],
    #[sg.Text("No accesory: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    #[sg.Text("Trousers: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    #[sg.Checkbox('1. Python file (start.py)', default=False,key='pyfile')],
    #[sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10, 1))],
    #[sg.Text("V-Neck: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
]

attributes_column2 = [
    
    [sg.Checkbox('No accesory', default=False,key='No_accesory')],
    #[sg.Text("No Carrying: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('No Carrying', default=False,key='No_Carrying')],
    #[sg.Text("Plaid: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Plaid', default=False,key='Plaid')],
    #[sg.Text("Plastic bags: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Plastic bags', default=False,key='Plastic_bags')],
    #[sg.Text("CarryingOther: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('CarryingOther', default=False,key='CarryingOther')],
    #[sg.Text("Shorts: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Shorts', default=False,key='Shorts')],
    #[sg.Text("Short Sleeve: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Short Sleeve', default=False,key='Short_Sleeve')],
    #[sg.Text("Skirt: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Skirt', default=False,key='Skirt')],
    #[sg.Text("Stripes: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Stripes', default=False,key='Stripes')],
    #[sg.Text("Sunglasses: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Sunglasses', default=False,key='Sunglasses')],
    [sg.Checkbox('Trousers', default=False,key='Trousers')],
    #[sg.Text("T-shirt: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('T-shirt', default=False,key='T-shirt')],
    #[sg.Text("Upper Other: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('Upper Other', default=False,key='Upper_Other')],
    #[sg.Checkbox('1. Python file (start.py)', default=False,key='pyfile')],
    #[sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10, 1))],
    #[sg.Text("V-Neck: "), sg.Button("yes",disabled=False), sg.Button("no",disabled=False)],
    [sg.Checkbox('V-Neck', default=False,key='V-Neck')],
    [sg.Button("Save",disabled=True)],
]



# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(attributes_column1),
        sg.VSeperator(),
        sg.Column(attributes_column2),
    ]
]

window = sg.Window("Image Viewer", layout)
