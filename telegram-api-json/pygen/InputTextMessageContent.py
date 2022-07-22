
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inputtextmessagecontent# ['Represents the content of a text message to be sent as the result of an inline query.']
class InputTextMessageContent(DefaultType):

    
	# @var message_text Text of the message to be sent, 1-4096 characters
	@property
	def message_text(self) -> String:
		return self._d["message_text"]
	# @var parse_mode Optional. Mode for parsing entities in the message text. See formatting options for more details.
	@property
	def parse_mode(self) -> String:
		return self._d["parse_mode"]
	# @var entities Optional. List of special entities that appear in message text, which can be specified instead of parse_mode
	@property
	def entities(self) -> Array of MessageEntity:
		return self._d["entities"]
	# @var disable_web_page_preview Optional. Disables link previews for links in the sent message
	@property
	def disable_web_page_preview(self) -> Boolean:
		return self._d["disable_web_page_preview"]

