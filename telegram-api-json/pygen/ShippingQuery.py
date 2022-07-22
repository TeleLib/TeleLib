
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#shippingquery# ['This object contains information about an incoming shipping query.']
class ShippingQuery(DefaultType):

    
	# @var id Unique query identifier
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var from User who sent the query
	@property
	def from(self) -> User:
		return self._d["from"]
	# @var invoice_payload Bot specified invoice payload
	@property
	def invoice_payload(self) -> String:
		return self._d["invoice_payload"]
	# @var shipping_address User specified shipping address
	@property
	def shipping_address(self) -> ShippingAddress:
		return self._d["shipping_address"]

