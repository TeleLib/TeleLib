
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chatmemberbanned# ["Represents a chat member that was banned in the chat and can't return to the chat or view chat messages."]
class ChatMemberBanned(DefaultType):

    
	# @var status The member's status in the chat, always "kicked"
	@property
	def status(self) -> String:
		return self._d["status"]
	# @var user Information about the user
	@property
	def user(self) -> User:
		return self._d["user"]
	# @var until_date Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned forever
	@property
	def until_date(self) -> Integer:
		return self._d["until_date"]

