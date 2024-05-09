from bot import Bot

def main():
    config_file = 'config.ini'
    bot = Bot(config_file)
    bot.setup_commands()
    bot.run(bot.config.get('Bot', 'token'))

if __name__ == "__main__":
    main()
