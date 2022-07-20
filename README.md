# LinuxMemesBot

This is a simple telegram bot that get some memes from r/linuxmemes and post it in a telegram channel.

## Installation

clone the repository
```git
https://github.com/SameerSahu007/LinuxMemesBot.git
```

create a virtual environment by installing virtualenv
```bash
pip install virtualenv
```

create the venv folder
```bash
virtualenv venv
```

After that activate the virtual enviorment by executing 

```bash
venv\Scripts\activate
```

Install the required packages
```bash
pip install -r requirements.txt
```

generate you telegram api key by searching @BotFather on Telegram after that you also need to generate [Reddit Api key](https://www.reddit.com/prefs/apps)

Now create a .env file and put your api keys in it 

```bash
CLIENT_ID=
CLIENT_SECRET = 
USER_AGENT =
TELEGRAM_API =
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
