
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#webappinfo# ['Describes a Web App.']
class WebAppInfo(DefaultType):

    
	# @var url An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps
	@property
	def url(self) -> String:
		return self._d["url"]

