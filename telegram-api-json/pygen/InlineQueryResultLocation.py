
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultlocation# ['Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.', 'Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.']
class InlineQueryResultLocation(DefaultType):

    
	# @var type Type of the result, must be location
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 Bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var latitude Location latitude in degrees
	@property
	def latitude(self) -> Float:
		return self._d["latitude"]
	# @var longitude Location longitude in degrees
	@property
	def longitude(self) -> Float:
		return self._d["longitude"]
	# @var title Location title
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var horizontal_accuracy Optional. The radius of uncertainty for the location, measured in meters; 0-1500
	@property
	def horizontal_accuracy(self) -> Float:
		return self._d["horizontal_accuracy"]
	# @var live_period Optional. Period in seconds for which the location can be updated, should be between 60 and 86400.
	@property
	def live_period(self) -> Integer:
		return self._d["live_period"]
	# @var heading Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
	@property
	def heading(self) -> Integer:
		return self._d["heading"]
	# @var proximity_alert_radius Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
	@property
	def proximity_alert_radius(self) -> Integer:
		return self._d["proximity_alert_radius"]
	# @var reply_markup Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> InlineKeyboardMarkup:
		return self._d["reply_markup"]
	# @var input_message_content Optional. Content of the message to be sent instead of the location
	@property
	def input_message_content(self) -> InputMessageContent:
		return self._d["input_message_content"]
	# @var thumb_url Optional. Url of the thumbnail for the result
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

