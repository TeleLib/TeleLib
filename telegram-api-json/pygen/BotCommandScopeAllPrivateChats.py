
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#botcommandscopeallprivatechats# ['Represents the scope of bot commands, covering all private chats.']
class BotCommandScopeAllPrivateChats(DefaultType):

    
	# @var type Scope type, must be all_private_chats
	@property
	def type(self) -> String:
		return self._d["type"]

