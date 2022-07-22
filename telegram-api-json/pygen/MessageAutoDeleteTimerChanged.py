
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#messageautodeletetimerchanged# ['This object represents a service message about a change in auto-delete timer settings.']
class MessageAutoDeleteTimerChanged(DefaultType):

    
	# @var message_auto_delete_time New auto-delete time for messages in the chat; in seconds
	@property
	def message_auto_delete_time(self) -> Integer:
		return self._d["message_auto_delete_time"]

