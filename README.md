# Membot — as simple as it is

Membot is a simple Telegram bot, which I created to practise with such things as Docker, Telegram API and Redis.

A lot of work to be done here, so stay tuned :)

## Installation

### Docker image

You can use docker image to run bot:

```bash
docker pull fiza1160/membot:0.0.1
docker run -d --rm fiza1160/membot:0.0.1
```

Requirements:

1. You must run `Redis` to work with bot. It stores data in Redis.
2. Set environment variables:
  - `MEM_BOT_TELEGRAM_TOKEN`
  - `MEM_BOT_REDIS_PORT`
  - `MEM_BOT_REDIS_HOST`

## TODO:

1. Decrease Docker image size.
2. Make a docker-compose file to simplify installation.
3. Make bot smarter :)
4. Integrate with CI/CD and deploy it to Heroku.
