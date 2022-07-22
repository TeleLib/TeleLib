
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultvideo# ['Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.']
class InlineQueryResultVideo(DefaultType):

    
	# @var type Type of the result, must be video
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var video_url A valid URL for the embedded video player or video file
	@property
	def video_url(self) -> String:
		return self._d["video_url"]
	# @var mime_type MIME type of the content of the video URL, "text/html" or "video/mp4"
	@property
	def mime_type(self) -> String:
		return self._d["mime_type"]
	# @var thumb_url URL of the thumbnail (JPEG only) for the video
	@property
	def thumb_url(self) -> String:
		return self._d["thumb_url"]
	# @var title Title for the result
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var caption Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> String:
		return self._d["caption"]
	# @var parse_mode Optional. Mode for parsing entities in the video caption. See formatting options for more details.
	@property
	def parse_mode(self) -> String:
		return self._d["parse_mode"]
	# @var caption_entities Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> Array of MessageEntity:
		return self._d["caption_entities"]
	# @var video_width Optional. Video width
	@property
	def video_width(self) -> Integer:
		return self._d["video_width"]
	# @var video_height Optional. Video height
	@property
	def video_height(self) -> Integer:
		return self._d["video_height"]
	# @var video_duration Optional. Video duration in seconds
	@property
	def video_duration(self) -> Integer:
		return self._d["video_duration"]
	# @var description Optional. Short description of the result
	@property
	def description(self) -> String:
		return self._d["description"]
	# @var reply_markup Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> InlineKeyboardMarkup:
		return self._d["reply_markup"]
	# @var input_message_content Optional. Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).
	@property
	def input_message_content(self) -> InputMessageContent:
		return self._d["input_message_content"]

