
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#shippingoption# ['This object represents one shipping option.']
class ShippingOption(DefaultType):

    
	# @var id Shipping option identifier
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var title Option title
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var prices List of price portions
	@property
	def prices(self) -> Array of LabeledPrice:
		return self._d["prices"]

