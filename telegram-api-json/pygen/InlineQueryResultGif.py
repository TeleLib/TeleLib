
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultgif# ['Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.']
class InlineQueryResultGif(DefaultType):

    
	# @var type Type of the result, must be gif
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var gif_url A valid URL for the GIF file. File size must not exceed 1MB
	@property
	def gif_url(self) -> String:
		return self._d["gif_url"]
	# @var gif_width Optional. Width of the GIF
	@property
	def gif_width(self) -> Integer:
		return self._d["gif_width"]
	# @var gif_height Optional. Height of the GIF
	@property
	def gif_height(self) -> Integer:
		return self._d["gif_height"]
	# @var gif_duration Optional. Duration of the GIF in seconds
	@property
	def gif_duration(self) -> Integer:
		return self._d["gif_duration"]
	# @var thumb_url URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
	@property
	def thumb_url(self) -> String:
		return self._d["thumb_url"]
	# @var thumb_mime_type Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg"
	@property
	def thumb_mime_type(self) -> String:
		return self._d["thumb_mime_type"]
	# @var title Optional. Title for the result
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var caption Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> String:
		return self._d["caption"]
	# @var parse_mode Optional. Mode for parsing entities in the caption. See formatting options for more details.
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
	# @var input_message_content Optional. Content of the message to be sent instead of the GIF animation
	@property
	def input_message_content(self) -> InputMessageContent:
		return self._d["input_message_content"]

