
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#successfulpayment# ['This object contains basic information about a successful payment.']
class SuccessfulPayment(DefaultType):

    
	# @var currency Three-letter ISO 4217 currency code
	@property
	def currency(self) -> String:
		return self._d["currency"]
	# @var total_amount Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
	@property
	def total_amount(self) -> Integer:
		return self._d["total_amount"]
	# @var invoice_payload Bot specified invoice payload
	@property
	def invoice_payload(self) -> String:
		return self._d["invoice_payload"]
	# @var shipping_option_id Optional. Identifier of the shipping option chosen by the user
	@property
	def shipping_option_id(self) -> String:
		return self._d["shipping_option_id"]
	# @var order_info Optional. Order information provided by the user
	@property
	def order_info(self) -> OrderInfo:
		return self._d["order_info"]
	# @var telegram_payment_charge_id Telegram payment identifier
	@property
	def telegram_payment_charge_id(self) -> String:
		return self._d["telegram_payment_charge_id"]
	# @var provider_payment_charge_id Provider payment identifier
	@property
	def provider_payment_charge_id(self) -> String:
		return self._d["provider_payment_charge_id"]

