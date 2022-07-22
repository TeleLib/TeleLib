
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inputmediaphoto# ['Represents a photo to be sent.']
class InputMediaPhoto(DefaultType):

    
	# @var type Type of the result, must be photo
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var media File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
	@property
	def media(self) -> String:
		return self._d["media"]
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

