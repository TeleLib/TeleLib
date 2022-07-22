
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif# ['Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.']
class InlineQueryResultMpeg4Gif(DefaultType):

    
	# @var type Type of the result, must be mpeg4_gif
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var mpeg4_url A valid URL for the MPEG4 file. File size must not exceed 1MB
	@property
	def mpeg4_url(self) -> String:
		return self._d["mpeg4_url"]
	# @var mpeg4_width Optional. Video width
	@property
	def mpeg4_width(self) -> Integer:
		return self._d["mpeg4_width"]
	# @var mpeg4_height Optional. Video height
	@property
	def mpeg4_height(self) -> Integer:
		return self._d["mpeg4_height"]
	# @var mpeg4_duration Optional. Video duration in seconds
	@property
	def mpeg4_duration(self) -> Integer:
		return self._d["mpeg4_duration"]
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
	# @var caption Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
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
	# @var input_message_content Optional. Content of the message to be sent instead of the video animation
	@property
	def input_message_content(self) -> InputMessageContent:
		return self._d["input_message_content"]

