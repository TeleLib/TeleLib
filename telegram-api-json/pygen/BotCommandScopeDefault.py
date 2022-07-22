
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#botcommandscopedefault# ['Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.']
class BotCommandScopeDefault(DefaultType):

    
	# @var type Scope type, must be default
	@property
	def type(self) -> String:
		return self._d["type"]

