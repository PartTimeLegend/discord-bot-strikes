from discord.ext import commands
import discord
from command_factory import CommandFactory
from database_manager import DatabaseManager

class Bot(commands.Bot):
    """ Custom bot class with setup and command handling. """
    def __init__(self, config_file):
        super().__init__(command_prefix='!')
        self.config_file = config_file
        self.db_manager = DatabaseManager(self.config_file)
        self.command_factory = CommandFactory(self.db_manager)

    async def on_ready(self):
        await self.db_manager.create_pool()
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.process_commands(message)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Invalid command. Use `!strike @user` to issue a strike.")

    async def close(self):
        await self.db_manager.close()
        await super().close()

    def setup_commands(self):
        self.add_command(self.strike_command)

    @property
    def strike_command(self):
        return commands.Command(name='strike', 
                                callback=self.strike_callback,
                                help="Issue a strike to a user",
                                usage="!strike @user",
                                permissions=discord.Permissions(administrator=True))

    async def strike_callback(self, ctx, member: discord.Member):
        command = self.command_factory.get_command("strike")
        await command.execute(ctx, member)
