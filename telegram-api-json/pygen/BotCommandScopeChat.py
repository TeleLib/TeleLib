
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#botcommandscopechat# ['Represents the scope of bot commands, covering a specific chat.']
class BotCommandScopeChat(DefaultType):

    
	# @var type Scope type, must be chat
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var chat_id Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
	@property
	def chat_id(self) -> Integer|String:
		return self._d["chat_id"]

