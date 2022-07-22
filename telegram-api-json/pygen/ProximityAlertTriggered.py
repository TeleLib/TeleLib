
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#proximityalerttriggered# ['This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.']
class ProximityAlertTriggered(DefaultType):

    
	# @var traveler User that triggered the alert
	@property
	def traveler(self) -> User:
		return self._d["traveler"]
	# @var watcher User that set the alert
	@property
	def watcher(self) -> User:
		return self._d["watcher"]
	# @var distance The distance between the users
	@property
	def distance(self) -> Integer:
		return self._d["distance"]

