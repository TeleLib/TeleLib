
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#messageid# ['This object represents a unique message identifier.']
class MessageId(DefaultType):

    
	# @var message_id Unique message identifier
	@property
	def message_id(self) -> Integer:
		return self._d["message_id"]

