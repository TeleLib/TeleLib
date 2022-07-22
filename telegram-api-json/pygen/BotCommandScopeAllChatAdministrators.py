
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#botcommandscopeallchatadministrators# ['Represents the scope of bot commands, covering all group and supergroup chat administrators.']
class BotCommandScopeAllChatAdministrators(DefaultType):

    
	# @var type Scope type, must be all_chat_administrators
	@property
	def type(self) -> String:
		return self._d["type"]

