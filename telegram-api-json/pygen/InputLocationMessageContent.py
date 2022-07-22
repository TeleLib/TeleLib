
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inputlocationmessagecontent# ['Represents the content of a location message to be sent as the result of an inline query.']
class InputLocationMessageContent(DefaultType):

    
	# @var latitude Latitude of the location in degrees
	@property
	def latitude(self) -> Float:
		return self._d["latitude"]
	# @var longitude Longitude of the location in degrees
	@property
	def longitude(self) -> Float:
		return self._d["longitude"]
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

