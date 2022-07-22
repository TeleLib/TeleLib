
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#orderinfo# ['This object represents information about an order.']
class OrderInfo(DefaultType):

    
	# @var name Optional. User name
	@property
	def name(self) -> String:
		return self._d["name"]
	# @var phone_number Optional. User's phone number
	@property
	def phone_number(self) -> String:
		return self._d["phone_number"]
	# @var email Optional. User email
	@property
	def email(self) -> String:
		return self._d["email"]
	# @var shipping_address Optional. User shipping address
	@property
	def shipping_address(self) -> ShippingAddress:
		return self._d["shipping_address"]

