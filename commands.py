class StrikeCommand:
    """ Handles the strike command functionality. """
    def __init__(self, db_manager):
        self.db_manager = db_manager

    async def execute(self, ctx, member):
        strikes = await self.db_manager.get_strike_count(member.id) + 1
        await self.db_manager.update_strikes(member.id, strikes)
        if strikes >= 3:
            await member.ban(reason="3 strikes")
            message = f"{member.display_name} has been banned due to accumulating 3 strikes."
        else:
            message = f"{member.display_name} has {strikes} {'strike' if strikes == 1 else 'strikes'}."
        await ctx.send(message)
        return message
