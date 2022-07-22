
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#venue# ['This object represents a venue.']
class Venue(DefaultType):

    
	# @var location Venue location. Can't be a live location
	@property
	def location(self) -> Location:
		return self._d["location"]
	# @var title Name of the venue
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var address Address of the venue
	@property
	def address(self) -> String:
		return self._d["address"]
	# @var foursquare_id Optional. Foursquare identifier of the venue
	@property
	def foursquare_id(self) -> String:
		return self._d["foursquare_id"]
	# @var foursquare_type Optional. Foursquare type of the venue. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
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

