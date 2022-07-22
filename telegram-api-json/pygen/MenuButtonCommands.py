
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#menubuttoncommands# ["Represents a menu button, which opens the bot's list of commands."]
class MenuButtonCommands(DefaultType):

    
	# @var type Type of the button, must be commands
	@property
	def type(self) -> String:
		return self._d["type"]

