import pandas as pd


attributes_list =[  'image_name',
                    'Age16-30',
                    'Age31-45',
                    'Age46-60',
                    'AgeAbove61',
                    'Backpack',
                    'CarryingOther',
                    'Casual lower',
                    'Casual upper',
                    'Formal lower',
                    'Formal upper',
                    'Hat',
                    'Jacket',
                    'Jeans',
                    'Leather Shoes',
                    'Logo',
                    'Long hair',
                    'Male',
                    'Messenger Bag',
                    'Muffler',
                    'No accessory',
                    'No carrying',
                    'Plaid',
                    'PlasticBags',
                    'Sandals',
                    'Shoes',
                    'Shorts',
                    'Short Sleeve',
                    'Skirt',
                    'Sneaker',
                    'Stripes',
                    'Sunglasses',
                    'Trousers',
                    'Tshirt',
                    'UpperOther',
                    'V-Neck']

# Create the data frame which contains the info of every image and its attributes
df_attributes = pd.DataFrame(columns = attributes_list)

