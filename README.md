# Template Bot v1.0
By [William Gardner](https://github.com/wg4568/), written for _@user_ on Fiverr

## Order Details

**$X** with **X day delivery** ordered on X/X/X

## Installation

To set up your system, you will need to do the following

- Install Python3.7 from their [website](https://www.python.org/)
- Install requirements by running `python -m pip install -r requirements.txt`

You will also need to create an application, through the [discord dev website](https://discordapp.com/developers/) then give it a bot. You will need the bot token in the `config.json` file for the bot to work!

See [this](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) step by step guide for more help creating a bot!

## Files

### Most important

You will need to use these files!

- `README.md` this file, for help and info
- `config.json` options and configuration
- `requirements.txt` required packages
- `main.py` run this to start the bot

### Other files

Don't touch these unless you know what you're doing!

- `database.json` where list data is stored
- `embeds.py` discord embed classes
- `venv/` [virtualenv](https://virtualenv.pypa.io/en/latest/) folder

## Configuration

See `config.json` to configure the bot.

The config file is formatted with the parameter name on the left, and it's value on the right. Do NOT touch the name on the left! This will break the bot. Instead change the value on the right to tweak your bot.

    "name": "value (change this!)"

Values that are text (as opposed to a number) should be surrounded by double quotes, as shown above.

 Configuration parameters are described below.

- `prefix` bot command prefix
- `embed_colors` side-color of the bot messages (in rgb)
- `commands` command names, and the actual command itself-- use this if you want to rename a command
- `token` bot token from the [discord api](https://discordapp.com/developers/)