from os.path import join
from os import remove
import pandas as pd

images_path = '/home/tubaher/Documents/Labeled_data/DK/diego'
annotations_path = 'test.txt'

df = pd.read_csv('test.txt', header=None,  sep=' ')

for image in df[0]:
    remove(join(images_path, image))


# print(df)
