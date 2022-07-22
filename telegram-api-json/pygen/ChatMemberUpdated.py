
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chatmemberupdated# ['This object represents changes in the status of a chat member.']
class ChatMemberUpdated(DefaultType):

    
	# @var chat Chat the user belongs to
	@property
	def chat(self) -> Chat:
		return self._d["chat"]
	# @var from Performer of the action, which resulted in the change
	@property
	def from(self) -> User:
		return self._d["from"]
	# @var date Date the change was done in Unix time
	@property
	def date(self) -> Integer:
		return self._d["date"]
	# @var old_chat_member Previous information about the chat member
	@property
	def old_chat_member(self) -> ChatMember:
		return self._d["old_chat_member"]
	# @var new_chat_member New information about the chat member
	@property
	def new_chat_member(self) -> ChatMember:
		return self._d["new_chat_member"]
	# @var invite_link Optional. Chat invite link, which was used by the user to join the chat; for joining by invite link events only.
	@property
	def invite_link(self) -> ChatInviteLink:
		return self._d["invite_link"]

