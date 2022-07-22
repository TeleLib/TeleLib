
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#botcommandscopechatmember# ['Represents the scope of bot commands, covering a specific member of a group or supergroup chat.']
class BotCommandScopeChatMember(DefaultType):

    
	# @var type Scope type, must be chat_member
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var chat_id Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
	@property
	def chat_id(self) -> Integer|String:
		return self._d["chat_id"]
	# @var user_id Unique identifier of the target user
	@property
	def user_id(self) -> Integer:
		return self._d["user_id"]

