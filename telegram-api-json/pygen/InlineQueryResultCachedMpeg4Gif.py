
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif# ['Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.']
class InlineQueryResultCachedMpeg4Gif(DefaultType):

    
	# @var type Type of the result, must be mpeg4_gif
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var mpeg4_file_id A valid file identifier for the MPEG4 file
	@property
	def mpeg4_file_id(self) -> String:
		return self._d["mpeg4_file_id"]
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

