import os
from random import choice

from imgurpython import ImgurClient

client_id = os.environ.get('IMG_ID')
client_secret = os.environ.get('IMG_SECRET')

imgur = ImgurClient(client_id, client_secret)

# Fetched once at startup; each command picks a random link from this list.

items = imgur.gallery_search(
    q="ronaldinho", advanced=None, sort='viral', window='all', page=0
)


def pega_imagem():
    return choice(items).link
