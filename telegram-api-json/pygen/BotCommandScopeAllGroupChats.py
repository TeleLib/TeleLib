
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#botcommandscopeallgroupchats# ['Represents the scope of bot commands, covering all group and supergroup chats.']
class BotCommandScopeAllGroupChats(DefaultType):

    
	# @var type Scope type, must be all_group_chats
	@property
	def type(self) -> String:
		return self._d["type"]

