
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chatmembermember# ['Represents a chat member that has no additional privileges or restrictions.']
class ChatMemberMember(DefaultType):

    
	# @var status The member's status in the chat, always "member"
	@property
	def status(self) -> String:
		return self._d["status"]
	# @var user Information about the user
	@property
	def user(self) -> User:
		return self._d["user"]

