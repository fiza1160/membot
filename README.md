# Membot — as simple as it is

Membot is a simple Telegram bot, which I created to practise with such things as Docker, Telegram API and Redis.

A lot of work to be done here, so stay tuned :)

## Installation

### Docker compose

```bash
git clone https://github.com/fiza1160/membot
cd membot
# You need to add Telegram Token to .env file
# Please, read this article to know how to create telegram bot:
# https://core.telegram.org/bots#3-how-do-i-create-a-bot
# echo "MEM_BOT_TELEGRAM_TOKEN=<YOUR_TELEGRAM_TOKEN>" > .env
docker-compose up
```

## TODO:

1. Decrease Docker image size.
2. Make a docker-compose file to simplify installation.
3. Make bot smarter :)
4. Integrate with CI/CD and deploy it to Heroku.
