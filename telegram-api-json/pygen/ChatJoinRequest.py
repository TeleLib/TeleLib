
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chatjoinrequest# ['Represents a join request sent to a chat.']
class ChatJoinRequest(DefaultType):

    
	# @var chat Chat to which the request was sent
	@property
	def chat(self) -> Chat:
		return self._d["chat"]
	# @var from User that sent the join request
	@property
	def from(self) -> User:
		return self._d["from"]
	# @var date Date the request was sent in Unix time
	@property
	def date(self) -> Integer:
		return self._d["date"]
	# @var bio Optional. Bio of the user.
	@property
	def bio(self) -> String:
		return self._d["bio"]
	# @var invite_link Optional. Chat invite link that was used by the user to send the join request
	@property
	def invite_link(self) -> ChatInviteLink:
		return self._d["invite_link"]

