from random import choice

from imgurpython import ImgurClient

client_id = 'ac47ce53e56a6fb'
client_secret = '1914a2917ca49a1ea70bbb1bc0b4bb8d38ed7845'

imgur = ImgurClient(client_id, client_secret)

items = imgur.gallery_search(q="ronaldinho", advanced=None, sort='viral', window='all', page=0)


def pega_imagem():
    return choice(items).link
