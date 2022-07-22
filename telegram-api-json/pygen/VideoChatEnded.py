
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#videochatended# ['This object represents a service message about a video chat ended in the chat.']
class VideoChatEnded(DefaultType):

    
	# @var duration Video chat duration in seconds
	@property
	def duration(self) -> Integer:
		return self._d["duration"]

