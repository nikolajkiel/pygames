from words import words

from functools import lru_cache
import requests, io, bs4, os
from flask import Flask, Response, render_template
from gtts import gTTS


app = Flask(__name__)


# @lru_cache()
# @timer
def get_sound(search_term, folder='audio', ext='.mp3'):
    search_term = search_term.strip()
    print(search_term)

    current = os.listdir(folder)
    if search_term + ext in current:
        with open(os.path.join(folder, search_term + ext), 'rb') as f:
            return [search_term, io.BytesIO(f.read())]


    url = f'https://sproget.dk/lookup?SearchableText={search_term}'
    response = requests.get(url)
#    pattern = re.compile(r'\.mp3')
#    matches = pattern.finditer(str(response.content))
#    for match in matches:
#        print(match)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    sounds = soup.find_all('audio')
    print(sounds)
    name, mp3 = None, None
    names = []
    while mp3 is None:
        for i,sound in enumerate(sounds):
            elements = list(sound.previous_elements)[:6]
            for elem in elements:
                if elem.__str__().startswith('<span class="k">'):
                    name = elem.contents[0]
                    if name == search_term:
                        mp3 = sound['src']
                        break;break;break#;continue
#                    else:
#                        names.append(name)
        break

    name = name if name is not None else search_term
    if mp3 is None:
        # Fall-back
        try:
            mp3 = sounds[0]['src']
#        mp3 = str(response.content)[str(response.content).find('.mp3')-100+55:str(response.content).find('.mp3')+4]

        except IndexError:
            print('No sounds found!')
            return name, b''

    bts = io.BytesIO(requests.get(mp3).content)
    with open(os.path.join(folder, search_term + ext), 'wb') as f:
        f.write(bts.read())
    return [name, bts]


def get_word(word, folder='audio', ext='.mp3', lang='da'):
    word = word.strip()

    current = os.listdir(folder)
    if not word + ext in current:
        g = gTTS(word, lang=lang)
        g.save(os.path.join(folder, word + ext))

    with open(os.path.join(folder, word + ext), 'rb') as f:
        return io.BytesIO(f.read())




def generate(bts):
    bts.seek(0)
    yield bts.read()

@app.route('/')
def index():
    app.logger.info(f'\n\n{os.getcwd()}   logged in successfully\n\n')
    a, b = get_sound('af')
    return Response(generate(b), mimetype="audio/x-wav")

@app.route('/<string:word>')
def sproget(word):
    b = get_word(word)
    return Response(generate(b), mimetype="audio/x-wav")


if __name__ == '__main__':
    app.run(debug=True, port=5333)
else:
    ss = get_sound('år')