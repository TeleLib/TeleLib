
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#callbackquery# ['This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.']
class CallbackQuery(DefaultType):

    
	# @var id Unique identifier for this query
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var from Sender
	@property
	def from(self) -> User:
		return self._d["from"]
	# @var message Optional. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
	@property
	def message(self) -> Message:
		return self._d["message"]
	# @var inline_message_id Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
	@property
	def inline_message_id(self) -> String:
		return self._d["inline_message_id"]
	# @var chat_instance Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
	@property
	def chat_instance(self) -> String:
		return self._d["chat_instance"]
	# @var data Optional. Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data.
	@property
	def data(self) -> String:
		return self._d["data"]
	# @var game_short_name Optional. Short name of a Game to be returned, serves as the unique identifier for the game
	@property
	def game_short_name(self) -> String:
		return self._d["game_short_name"]

