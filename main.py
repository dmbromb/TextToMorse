import pandas as pd
import lxml

def text_to_morse(word, translation_dictionary):
    morse = ''
    for letter in word:
        morse += f'{translation_dictionary[letter.title()]} '
    return morse

url = 'https://en.wikipedia.org/wiki/Morse_code'
data = pd.read_html(url)
df = (data[0])
df = df[['Character', 'Code']].loc[0:25]
df['Character'] = (df['Character'].str.split(',', expand=True)).iloc[:, 0]
df['Code'] = (df['Code'].str.replace('ⓘ', '')).str.replace('\xa0', ' ')
df = (df.set_index('Character'))

keep_going = True

while keep_going:
    dict = df.to_dict()['Code']
    word = input('\nWhat word would you like to translate? \n')
    try:
        print(text_to_morse(word, dict))
    except:
        print('Invalid string. Please enter letters only')
    y_n = input('\nWould you like to translate another word? (y/n)\n')
    if y_n.upper() != 'Y':
        keep_going = False