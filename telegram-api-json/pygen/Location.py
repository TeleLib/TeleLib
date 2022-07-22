
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#location# ['This object represents a point on the map.']
class Location(DefaultType):

    
	# @var longitude Longitude as defined by sender
	@property
	def longitude(self) -> Float:
		return self._d["longitude"]
	# @var latitude Latitude as defined by sender
	@property
	def latitude(self) -> Float:
		return self._d["latitude"]
	# @var horizontal_accuracy Optional. The radius of uncertainty for the location, measured in meters; 0-1500
	@property
	def horizontal_accuracy(self) -> Float:
		return self._d["horizontal_accuracy"]
	# @var live_period Optional. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only.
	@property
	def live_period(self) -> Integer:
		return self._d["live_period"]
	# @var heading Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only.
	@property
	def heading(self) -> Integer:
		return self._d["heading"]
	# @var proximity_alert_radius Optional. The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
	@property
	def proximity_alert_radius(self) -> Integer:
		return self._d["proximity_alert_radius"]

