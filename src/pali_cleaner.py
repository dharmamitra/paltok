import re

def clean_pali(string):
        string = string.lower()

        if type(string) != str:
                print(f'Pali cleaner: non-str input: {string}')
                return ''
        html_tags = re.compile('<.*?>')
        string = re.sub(html_tags, "", string)
        string = re.sub(r'[0-9!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\']',"", string) # ascii digits and punctuation
        string = re.sub(r'[\t\n\r\x0b\x0c]'," ", string) # whitespaces apart from " "
        string = re.sub(r'[ṅṁ]',"ṃ", string) # whitespaces apart from " "
        string = re.sub(r'[”ऐạै–…‘“’\\ौऋ—औ]',"", string)
        string = string.strip()
        return string

def normalize_orig(string):
        string = re.sub(r'[ṅṁ]',"ṃ", string)
        return string
