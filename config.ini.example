import configparser
import aiomysql

class DatabaseManager:
    """ Manages all database operations for the Discord bot. """
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.db_config = {
            'host': self.config.get('Database', 'host'),
            'port': self.config.getint('Database', 'port'),
            'user': self.config.get('Database', 'user'),
            'password': self.config.get('Database', 'password'),
            'db': self.config.get('Database', 'db'),
        }
        self.pool = None

    async def create_pool(self):
        self.pool = await aiomysql.create_pool(**self.db_config)

    async def close(self):
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()

    async def execute_query(self, query, *args):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query, args)
                if query.strip().lower().startswith("select"):
                    return await cursor.fetchall()
                await conn.commit()

    async def get_strike_count(self, user_id):
        result = await self.execute_query("SELECT strike_count FROM strikes WHERE user_id = %s", user_id)
        return result[0][0] if result else 0

    async def update_strikes(self, user_id, strikes):
        await self.execute_query("REPLACE INTO strikes (user_id, strike_count) VALUES (%s, %s)", user_id, strikes)
