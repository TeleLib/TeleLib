
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultcachedaudio# ['Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.', 'Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.']
class InlineQueryResultCachedAudio(DefaultType):

    
	# @var type Type of the result, must be audio
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var audio_file_id A valid file identifier for the audio file
	@property
	def audio_file_id(self) -> String:
		return self._d["audio_file_id"]
	# @var caption Optional. Caption, 0-1024 characters after entities parsing
	@property
	def caption(self) -> String:
		return self._d["caption"]
	# @var parse_mode Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
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
	# @var input_message_content Optional. Content of the message to be sent instead of the audio
	@property
	def input_message_content(self) -> InputMessageContent:
		return self._d["input_message_content"]

