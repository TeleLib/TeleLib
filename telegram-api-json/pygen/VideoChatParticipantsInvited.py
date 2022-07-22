
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#videochatparticipantsinvited# ['This object represents a service message about new members invited to a video chat.']
class VideoChatParticipantsInvited(DefaultType):

    
	# @var users New members that were invited to the video chat
	@property
	def users(self) -> Array of User:
		return self._d["users"]

