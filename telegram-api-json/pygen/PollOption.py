
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#polloption# ['This object contains information about one answer option in a poll.']
class PollOption(DefaultType):

    
	# @var text Option text, 1-100 characters
	@property
	def text(self) -> String:
		return self._d["text"]
	# @var voter_count Number of users that voted for this option
	@property
	def voter_count(self) -> Integer:
		return self._d["voter_count"]

