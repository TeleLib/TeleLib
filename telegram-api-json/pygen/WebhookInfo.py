
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#webhookinfo# ['Describes the current status of a webhook.']
class WebhookInfo(DefaultType):

    
	# @var url Webhook URL, may be empty if webhook is not set up
	@property
	def url(self) -> String:
		return self._d["url"]
	# @var has_custom_certificate True, if a custom certificate was provided for webhook certificate checks
	@property
	def has_custom_certificate(self) -> Boolean:
		return self._d["has_custom_certificate"]
	# @var pending_update_count Number of updates awaiting delivery
	@property
	def pending_update_count(self) -> Integer:
		return self._d["pending_update_count"]
	# @var ip_address Optional. Currently used webhook IP address
	@property
	def ip_address(self) -> String:
		return self._d["ip_address"]
	# @var last_error_date Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook
	@property
	def last_error_date(self) -> Integer:
		return self._d["last_error_date"]
	# @var last_error_message Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
	@property
	def last_error_message(self) -> String:
		return self._d["last_error_message"]
	# @var last_synchronization_error_date Optional. Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters
	@property
	def last_synchronization_error_date(self) -> Integer:
		return self._d["last_synchronization_error_date"]
	# @var max_connections Optional. The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery
	@property
	def max_connections(self) -> Integer:
		return self._d["max_connections"]
	# @var allowed_updates Optional. A list of update types the bot is subscribed to. Defaults to all update types except chat_member
	@property
	def allowed_updates(self) -> Array of String:
		return self._d["allowed_updates"]

