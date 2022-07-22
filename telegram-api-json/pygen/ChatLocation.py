
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chatlocation# ['Represents a location to which a chat is connected.']
class ChatLocation(DefaultType):

    
	# @var location The location to which the supergroup is connected. Can't be a live location.
	@property
	def location(self) -> Location:
		return self._d["location"]
	# @var address Location address; 1-64 characters, as defined by the chat owner
	@property
	def address(self) -> String:
		return self._d["address"]

