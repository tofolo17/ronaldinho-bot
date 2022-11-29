<div align="center">
    <img src="Images/00.gif" width="400"/>
</div>
<br/>

# ronaldinho-bot

> 🇧🇷 [Português](#o-que-você-encontrará-neste-repositório) · 🇺🇸 [English](#what-will-you-find-in-this-repository)

## O que você encontrará neste repositório?

Um pequeno bot de Discord tão aleatório quanto o Ronaldinho. Com o prefixo "ronaldo", extraia imagens aleatórias do
craque da base de dados do Imgur. Feito em **junho de 2021** e revisado em novembro de 2022.

### Comandos

| Comando        | O que faz                                                    |
|----------------|--------------------------------------------------------------|
| `ronaldo gol`  | responde com um bordão aleatório                             |
| `ronaldo lindo`| envia uma imagem aleatória do Ronaldinho, buscada no Imgur   |

O status do bot também muda a cada 5 segundos ("Jogando FutCadeia", "Assistindo Harry Potter"...).

### Ferramentas

Python 3, [discord.py](https://discordpy.readthedocs.io/) 1.7 e [imgurpython](https://github.com/Imgur/imgurpython).

### Como usar

```bash
git clone https://github.com/tofolo17/ronaldinho-bot.git
cd ronaldinho-bot
pip install -r requirements.txt
```

Crie um bot no [Discord Developer Portal](https://discord.com/developers/applications) e uma aplicação na
[API do Imgur](https://api.imgur.com/oauth2/addclient). Defina as variáveis de ambiente (veja `.env.example`):

```bash
export DISCORD_TOKEN="token do bot"
export IMG_ID="client id do Imgur"
export IMG_SECRET="client secret do Imgur"
python main.py
```

> ⚠️ O código usa a API do discord.py 1.x (sem *intents*), por isso a versão fica fixada no `requirements.txt`. O
> imgurpython não é mais mantido, então a busca de imagens pode deixar de funcionar.

### Licença

[MIT](LICENSE)

---

## What will you find in this repository?

A little Discord bot as random as Ronaldinho. With the prefix "ronaldo", extract random images of the star from Imgur's
database. Built in **June 2021** and revised in November 2022.

### Commands

| Command        | What it does                                           |
|----------------|--------------------------------------------------------|
| `ronaldo gol`  | replies with a random catchphrase                      |
| `ronaldo lindo`| sends a random Ronaldinho image fetched from Imgur     |

The bot's status also changes every 5 seconds ("Playing FutCadeia", "Watching Harry Potter"...).

### Tools

Python 3, [discord.py](https://discordpy.readthedocs.io/) 1.7 and [imgurpython](https://github.com/Imgur/imgurpython).

### How to use

```bash
git clone https://github.com/tofolo17/ronaldinho-bot.git
cd ronaldinho-bot
pip install -r requirements.txt
```

Create a bot in the [Discord Developer Portal](https://discord.com/developers/applications) and an app on the
[Imgur API](https://api.imgur.com/oauth2/addclient). Set the environment variables (see `.env.example`):

```bash
export DISCORD_TOKEN="bot token"
export IMG_ID="Imgur client id"
export IMG_SECRET="Imgur client secret"
python main.py
```

> ⚠️ The code uses the discord.py 1.x API (no intents), so the version is pinned in `requirements.txt`. imgurpython is
> no longer maintained, so the image search may stop working.

### License

[MIT](LICENSE)
