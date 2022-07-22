
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultvenue# ['Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.', 'Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.']
class InlineQueryResultVenue(DefaultType):

    
	# @var type Type of the result, must be venue
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 Bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var latitude Latitude of the venue location in degrees
	@property
	def latitude(self) -> Float:
		return self._d["latitude"]
	# @var longitude Longitude of the venue location in degrees
	@property
	def longitude(self) -> Float:
		return self._d["longitude"]
	# @var title Title of the venue
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var address Address of the venue
	@property
	def address(self) -> String:
		return self._d["address"]
	# @var foursquare_id Optional. Foursquare identifier of the venue if known
	@property
	def foursquare_id(self) -> String:
		return self._d["foursquare_id"]
	# @var foursquare_type Optional. Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
	@property
	def foursquare_type(self) -> String:
		return self._d["foursquare_type"]
	# @var google_place_id Optional. Google Places identifier of the venue
	@property
	def google_place_id(self) -> String:
		return self._d["google_place_id"]
	# @var google_place_type Optional. Google Places type of the venue. (See supported types.)
	@property
	def google_place_type(self) -> String:
		return self._d["google_place_type"]
	# @var reply_markup Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> InlineKeyboardMarkup:
		return self._d["reply_markup"]
	# @var input_message_content Optional. Content of the message to be sent instead of the venue
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

