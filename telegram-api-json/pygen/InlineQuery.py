
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequery# ['This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.']
class InlineQuery(DefaultType):

    
	# @var id Unique identifier for this query
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var from Sender
	@property
	def from(self) -> User:
		return self._d["from"]
	# @var query Text of the query (up to 256 characters)
	@property
	def query(self) -> String:
		return self._d["query"]
	# @var offset Offset of the results to be returned, can be controlled by the bot
	@property
	def offset(self) -> String:
		return self._d["offset"]
	# @var chat_type Optional. Type of the chat from which the inline query was sent. Can be either "sender" for a private chat with the inline query sender, "private", "group", "supergroup", or "channel". The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat
	@property
	def chat_type(self) -> String:
		return self._d["chat_type"]
	# @var location Optional. Sender location, only for bots that request user location
	@property
	def location(self) -> Location:
		return self._d["location"]

