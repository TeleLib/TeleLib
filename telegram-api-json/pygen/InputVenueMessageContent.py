
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inputvenuemessagecontent# ['Represents the content of a venue message to be sent as the result of an inline query.']
class InputVenueMessageContent(DefaultType):

    
	# @var latitude Latitude of the venue in degrees
	@property
	def latitude(self) -> Float:
		return self._d["latitude"]
	# @var longitude Longitude of the venue in degrees
	@property
	def longitude(self) -> Float:
		return self._d["longitude"]
	# @var title Name of the venue
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var address Address of the venue
	@property
	def address(self) -> String:
		return self._d["address"]
	# @var foursquare_id Optional. Foursquare identifier of the venue, if known
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

