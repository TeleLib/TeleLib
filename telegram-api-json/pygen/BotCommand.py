
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#botcommand# ['This object represents a bot command.']
class BotCommand(DefaultType):

    
	# @var command Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores.
	@property
	def command(self) -> String:
		return self._d["command"]
	# @var description Description of the command; 1-256 characters.
	@property
	def description(self) -> String:
		return self._d["description"]

