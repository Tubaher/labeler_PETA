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



# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column)
    ]
]

window = sg.Window("Image Viewer", layout)