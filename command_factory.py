from commands import StrikeCommand

class CommandFactory:
    """ Factory to create command handler instances. """
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_command(self, command_name):
        if command_name == "strike":
            return StrikeCommand(self.db_manager)
        raise ValueError("Unknown command")
