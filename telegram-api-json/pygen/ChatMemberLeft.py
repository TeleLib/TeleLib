
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chatmemberleft# ["Represents a chat member that isn't currently a member of the chat, but may join it themselves."]
class ChatMemberLeft(DefaultType):

    
	# @var status The member's status in the chat, always "left"
	@property
	def status(self) -> String:
		return self._d["status"]
	# @var user Information about the user
	@property
	def user(self) -> User:
		return self._d["user"]

