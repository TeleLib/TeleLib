
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#userprofilephotos# ["This object represent a user's profile pictures."]
class UserProfilePhotos(DefaultType):

    
	# @var total_count Total number of profile pictures the target user has
	@property
	def total_count(self) -> Integer:
		return self._d["total_count"]
	# @var photos Requested profile pictures (in up to 4 sizes each)
	@property
	def photos(self) -> Array of Array of PhotoSize:
		return self._d["photos"]

