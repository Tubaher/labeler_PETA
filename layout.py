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
    [sg.Button('Back',disabled=True),
    sg.Button('Next'),
    sg.Button('Save')]
]

attributes_column1 = [
    
    [sg.Text("Choose the correct attribute:")],
    [sg.Text(size=(40, 1), key="-SaveMessage-")],
    [sg.Text("Age: "),sg.Radio('16-30  ', "Age", key='Age16-30', default=True, size=(10, 1)), sg.Radio('Age31-45    ', "Age",key='Age31-45'),sg.Radio('46-60    ', "Age",key='Age46-60'),sg.Radio('Above 61', "Age",key='AgeAbove61')],
    [sg.Checkbox('Backpack', default=False,key='Backpack')], 
    [sg.Checkbox('Carrying Other', default=False,key='CarryingOther')],
    [sg.Text("Lower: "),sg.Radio('Casual  ', "Casual_lower" , key='Casual lower', default=True, size=(10, 1)), sg.Radio('Formal    ', "Formal_lower", key='Formal lower')],
    [sg.Text("Shoes: "),sg.Radio('Leather Shoes  ', "Shoes",key='Leather Shoes', default=True, size=(10, 1)), sg.Radio('Sandals    ', "Shoes",key='Sandals'),sg.Radio('Shoes    ', "Shoes",key='Shoes'),sg.Radio('Sneakers', "Shoes",key='Sneaker')],
    [sg.Text("Upper: "),sg.Radio('Casual  ', "Casual_upper", key='Casual upper', default=True, size=(10, 1)), sg.Radio('Formal    ', "Formal_upper", key='Formal upper')],       
    [sg.Checkbox('HAT', default=False,key='HAT')],
    [sg.Checkbox('Jacket', default=False,key='Jacket')],
    [sg.Checkbox('Jeans', default=False,key='Jeans')],
    [sg.Checkbox('LogoLogo', default=False,key='Logo')],
    [sg.Checkbox('LongHair', default=False,key='Long hair')],
    [sg.Checkbox('Male', default=False,key='Male')],
    [sg.Checkbox('Messenger Bag', default=False,key='Messenger Bag')],
    [sg.Checkbox('Muffler', default=False,key='Muffler')],

]

attributes_column2 = [
    
    [sg.Checkbox('No accesory', default=False,key='No accesory')],
    [sg.Checkbox('No Carrying', default=False,key='No Carrying')],
    [sg.Checkbox('Plaid', default=False,key='Plaid')],
    [sg.Checkbox('Plastic bags', default=False,key='PlasticBags')],
    [sg.Checkbox('Shorts', default=False,key='Shorts')],
    [sg.Checkbox('Short Sleeve', default=False,key='Short Sleeve')],
    [sg.Checkbox('Skirt', default=False,key='Skirt')],
    [sg.Checkbox('Stripes', default=False,key='Stripes')],
    [sg.Checkbox('Sunglasses', default=False,key='Sunglasses')],
    [sg.Checkbox('Trousers', default=False,key='Trousers')],
    [sg.Checkbox('T-shirt', default=False,key='Tshirt')],
    [sg.Checkbox('Upper Other', default=False,key='UpperOther')],
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

window = sg.Window("Labeler for PETA", layout)
