'''
'''

import json
import os
import string
import sys

def clean_text(the_text):
    lower = the_text.lower().split()
    cleaned = ' '.join(lower)
    no_emojis = cleaned
    trans_dict = {}
    for key in string.punctuation:
        if key == "'":
            trans_dict[key] = ''
        else:
            trans_dict[key] = ' '

    text_punct = str.maketrans(trans_dict)

    text_low = no_emojis.lower()
    text_toks = text_low.translate(text_punct).split()

    return text_toks

if __name__ == '__main__':
    dirname = sys.argv[1]
    dest = sys.argv[2]
    count = 0
    reply_count = 0
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(filename)
            full_path = os.path.join(root, filename)
            dest_path = os.path.join(dest, filename)

            cmts = []
            with open(full_path) as handle:
                for new_line in handle:
                    the_payload = json.loads(new_line)
                    the_text = ''
                    if the_payload['kind'] == 'youtube#commentThread':
                        the_text = the_payload['snippet']['topLevelComment']['snippet']['textOriginal']

                    elif the_payload['kind'] == 'youtube#comment':
                        the_text = the_payload['snippet']['textOriginal']

                    cleaned_toks = clean_text(the_text)
                    the_payload['cleaned_tokens'] = cleaned_toks
                    cmts.append(the_payload)

            with open(dest_path, 'a') as handle:
                for cmt in cmts:
                    handle.write(json.dumps(cmt))
                    handle.write('\n')
                    