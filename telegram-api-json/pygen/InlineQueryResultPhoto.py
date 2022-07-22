
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultphoto# ['Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.']
class InlineQueryResultPhoto(DefaultType):

    
	# @var type Type of the result, must be photo
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var photo_url A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB
	@property
	def photo_url(self) -> String:
		return self._d["photo_url"]
	# @var thumb_url URL of the thumbnail for the photo
	@property
	def thumb_url(self) -> String:
		return self._d["thumb_url"]
	# @var photo_width Optional. Width of the photo
	@property
	def photo_width(self) -> Integer:
		return self._d["photo_width"]
	# @var photo_height Optional. Height of the photo
	@property
	def photo_height(self) -> Integer:
		return self._d["photo_height"]
	# @var title Optional. Title for the result
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var description Optional. Short description of the result
	@property
	def description(self) -> String:
		return self._d["description"]
	# @var caption Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> String:
		return self._d["caption"]
	# @var parse_mode Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
	@property
	def parse_mode(self) -> String:
		return self._d["parse_mode"]
	# @var caption_entities Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> Array of MessageEntity:
		return self._d["caption_entities"]
	# @var reply_markup Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> InlineKeyboardMarkup:
		return self._d["reply_markup"]
	# @var input_message_content Optional. Content of the message to be sent instead of the photo
	@property
	def input_message_content(self) -> InputMessageContent:
		return self._d["input_message_content"]

