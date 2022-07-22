
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#pollanswer# ['This object represents an answer of a user in a non-anonymous poll.']
class PollAnswer(DefaultType):

    
	# @var poll_id Unique poll identifier
	@property
	def poll_id(self) -> String:
		return self._d["poll_id"]
	# @var user The user, who changed the answer to the poll
	@property
	def user(self) -> User:
		return self._d["user"]
	# @var option_ids 0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote.
	@property
	def option_ids(self) -> Array of Integer:
		return self._d["option_ids"]

