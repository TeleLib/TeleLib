
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#videochatscheduled# ['This object represents a service message about a video chat scheduled in the chat.']
class VideoChatScheduled(DefaultType):

    
	# @var start_date Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator
	@property
	def start_date(self) -> Integer:
		return self._d["start_date"]

