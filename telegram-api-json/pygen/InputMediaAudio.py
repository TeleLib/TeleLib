
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inputmediaaudio# ['Represents an audio file to be treated as music to be sent.']
class InputMediaAudio(DefaultType):

    
	# @var type Type of the result, must be audio
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var media File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
	@property
	def media(self) -> String:
		return self._d["media"]
	# @var thumb Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
	@property
	def thumb(self) -> InputFile|String:
		return self._d["thumb"]
	# @var caption Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing
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
	# @var duration Optional. Duration of the audio in seconds
	@property
	def duration(self) -> Integer:
		return self._d["duration"]
	# @var performer Optional. Performer of the audio
	@property
	def performer(self) -> String:
		return self._d["performer"]
	# @var title Optional. Title of the audio
	@property
	def title(self) -> String:
		return self._d["title"]

