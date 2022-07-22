
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultdocument# ['Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.', 'Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.']
class InlineQueryResultDocument(DefaultType):

    
	# @var type Type of the result, must be document
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var title Title for the result
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var caption Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> String:
		return self._d["caption"]
	# @var parse_mode Optional. Mode for parsing entities in the document caption. See formatting options for more details.
	@property
	def parse_mode(self) -> String:
		return self._d["parse_mode"]
	# @var caption_entities Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> Array of MessageEntity:
		return self._d["caption_entities"]
	# @var document_url A valid URL for the file
	@property
	def document_url(self) -> String:
		return self._d["document_url"]
	# @var mime_type MIME type of the content of the file, either "application/pdf" or "application/zip"
	@property
	def mime_type(self) -> String:
		return self._d["mime_type"]
	# @var description Optional. Short description of the result
	@property
	def description(self) -> String:
		return self._d["description"]
	# @var reply_markup Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> InlineKeyboardMarkup:
		return self._d["reply_markup"]
	# @var input_message_content Optional. Content of the message to be sent instead of the file
	@property
	def input_message_content(self) -> InputMessageContent:
		return self._d["input_message_content"]
	# @var thumb_url Optional. URL of the thumbnail (JPEG only) for the file
	@property
	def thumb_url(self) -> String:
		return self._d["thumb_url"]
	# @var thumb_width Optional. Thumbnail width
	@property
	def thumb_width(self) -> Integer:
		return self._d["thumb_width"]
	# @var thumb_height Optional. Thumbnail height
	@property
	def thumb_height(self) -> Integer:
		return self._d["thumb_height"]

