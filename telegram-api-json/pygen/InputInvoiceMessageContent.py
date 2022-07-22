
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inputinvoicemessagecontent# ['Represents the content of an invoice message to be sent as the result of an inline query.']
class InputInvoiceMessageContent(DefaultType):

    
	# @var title Product name, 1-32 characters
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var description Product description, 1-255 characters
	@property
	def description(self) -> String:
		return self._d["description"]
	# @var payload Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
	@property
	def payload(self) -> String:
		return self._d["payload"]
	# @var provider_token Payment provider token, obtained via @BotFather
	@property
	def provider_token(self) -> String:
		return self._d["provider_token"]
	# @var currency Three-letter ISO 4217 currency code, see more on currencies
	@property
	def currency(self) -> String:
		return self._d["currency"]
	# @var prices Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
	@property
	def prices(self) -> Array of LabeledPrice:
		return self._d["prices"]
	# @var max_tip_amount Optional. The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0
	@property
	def max_tip_amount(self) -> Integer:
		return self._d["max_tip_amount"]
	# @var suggested_tip_amounts Optional. A JSON-serialized array of suggested amounts of tip in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
	@property
	def suggested_tip_amounts(self) -> Array of Integer:
		return self._d["suggested_tip_amounts"]
	# @var provider_data Optional. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider.
	@property
	def provider_data(self) -> String:
		return self._d["provider_data"]
	# @var photo_url Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.
	@property
	def photo_url(self) -> String:
		return self._d["photo_url"]
	# @var photo_size Optional. Photo size in bytes
	@property
	def photo_size(self) -> Integer:
		return self._d["photo_size"]
	# @var photo_width Optional. Photo width
	@property
	def photo_width(self) -> Integer:
		return self._d["photo_width"]
	# @var photo_height Optional. Photo height
	@property
	def photo_height(self) -> Integer:
		return self._d["photo_height"]
	# @var need_name Optional. Pass True, if you require the user's full name to complete the order
	@property
	def need_name(self) -> Boolean:
		return self._d["need_name"]
	# @var need_phone_number Optional. Pass True, if you require the user's phone number to complete the order
	@property
	def need_phone_number(self) -> Boolean:
		return self._d["need_phone_number"]
	# @var need_email Optional. Pass True, if you require the user's email address to complete the order
	@property
	def need_email(self) -> Boolean:
		return self._d["need_email"]
	# @var need_shipping_address Optional. Pass True, if you require the user's shipping address to complete the order
	@property
	def need_shipping_address(self) -> Boolean:
		return self._d["need_shipping_address"]
	# @var send_phone_number_to_provider Optional. Pass True, if the user's phone number should be sent to provider
	@property
	def send_phone_number_to_provider(self) -> Boolean:
		return self._d["send_phone_number_to_provider"]
	# @var send_email_to_provider Optional. Pass True, if the user's email address should be sent to provider
	@property
	def send_email_to_provider(self) -> Boolean:
		return self._d["send_email_to_provider"]
	# @var is_flexible Optional. Pass True, if the final price depends on the shipping method
	@property
	def is_flexible(self) -> Boolean:
		return self._d["is_flexible"]

