import re

def parser(text):

    text_split = re.split(r'0+', text)

    dict_sample = {'first_name': text_split[0],
                   'last_name': text_split[1],
                   'id': text_split[2]
                   }
    
    print('\n\nEncoded Text is: ', text)
    print('Dictionary is ')
    print(dict_sample)

text_string = 'Robert000Smith0000123'
parser(text_string)
