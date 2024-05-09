# Discord Bot with Strikes System

This is a Discord bot that allows server administrators to issue strikes to users. When a user accumulates 3 strikes, they are automatically banned from the server.

## Features

- **Strike System**: Administrators can issue strikes to users.
- **Automatic Ban**: Users are banned from the server when they accumulate 3 strikes.
- **Database Integration**: Strikes are stored in a MariaDB database.
- **Configuration File**: Bot token and database settings are read from a configuration file.

## Requirements

- Python 3.x
- [discord.py](https://pypi.org/project/discord.py/)
- [aiomysql](https://pypi.org/project/aiomysql/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/parttimelegend/discord-bot-strikes.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `config.ini` file based on the provided `config.ini.example` template and fill in your bot token and database credentials.

4. Run the bot:

    ```bash
    python main.py
    ```

## Configuration

Edit the `config.ini` file to specify your bot token and database settings.

```ini
[Database]
host = localhost
port = 3306
user = your_database_user
password = your_database_password
db = your_database_name

[Bot]
token = your_bot_token
```

## Usage

- Invite the bot to your Discord server.
- Use `!strike @user` command to issue a strike to a user.
- Use `!shutdown` command to shut down the bot.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug fixes, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
