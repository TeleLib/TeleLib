
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#shippingaddress# ['This object represents a shipping address.']
class ShippingAddress(DefaultType):

    
	# @var country_code Two-letter ISO 3166-1 alpha-2 country code
	@property
	def country_code(self) -> String:
		return self._d["country_code"]
	# @var state State, if applicable
	@property
	def state(self) -> String:
		return self._d["state"]
	# @var city City
	@property
	def city(self) -> String:
		return self._d["city"]
	# @var street_line1 First line for the address
	@property
	def street_line1(self) -> String:
		return self._d["street_line1"]
	# @var street_line2 Second line for the address
	@property
	def street_line2(self) -> String:
		return self._d["street_line2"]
	# @var post_code Address post code
	@property
	def post_code(self) -> String:
		return self._d["post_code"]

