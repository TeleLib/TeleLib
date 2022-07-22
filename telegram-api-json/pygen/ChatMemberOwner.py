
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chatmemberowner# ['Represents a chat member that owns the chat and has all administrator privileges.']
class ChatMemberOwner(DefaultType):

    
	# @var status The member's status in the chat, always "creator"
	@property
	def status(self) -> String:
		return self._d["status"]
	# @var user Information about the user
	@property
	def user(self) -> User:
		return self._d["user"]
	# @var is_anonymous True, if the user's presence in the chat is hidden
	@property
	def is_anonymous(self) -> Boolean:
		return self._d["is_anonymous"]
	# @var custom_title Optional. Custom title for this user
	@property
	def custom_title(self) -> String:
		return self._d["custom_title"]

