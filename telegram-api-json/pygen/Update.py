
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#update# ['This object represents an incoming update.', 'At most one of the optional parameters can be present in any given update.']
class Update(DefaultType):

    
	# @var update_id The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
	@property
	def update_id(self) -> Integer:
		return self._d["update_id"]
	# @var message Optional. New incoming message of any kind - text, photo, sticker, etc.
	@property
	def message(self) -> Message:
		return self._d["message"]
	# @var edited_message Optional. New version of a message that is known to the bot and was edited
	@property
	def edited_message(self) -> Message:
		return self._d["edited_message"]
	# @var channel_post Optional. New incoming channel post of any kind - text, photo, sticker, etc.
	@property
	def channel_post(self) -> Message:
		return self._d["channel_post"]
	# @var edited_channel_post Optional. New version of a channel post that is known to the bot and was edited
	@property
	def edited_channel_post(self) -> Message:
		return self._d["edited_channel_post"]
	# @var inline_query Optional. New incoming inline query
	@property
	def inline_query(self) -> InlineQuery:
		return self._d["inline_query"]
	# @var chosen_inline_result Optional. The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
	@property
	def chosen_inline_result(self) -> ChosenInlineResult:
		return self._d["chosen_inline_result"]
	# @var callback_query Optional. New incoming callback query
	@property
	def callback_query(self) -> CallbackQuery:
		return self._d["callback_query"]
	# @var shipping_query Optional. New incoming shipping query. Only for invoices with flexible price
	@property
	def shipping_query(self) -> ShippingQuery:
		return self._d["shipping_query"]
	# @var pre_checkout_query Optional. New incoming pre-checkout query. Contains full information about checkout
	@property
	def pre_checkout_query(self) -> PreCheckoutQuery:
		return self._d["pre_checkout_query"]
	# @var poll Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
	@property
	def poll(self) -> Poll:
		return self._d["poll"]
	# @var poll_answer Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
	@property
	def poll_answer(self) -> PollAnswer:
		return self._d["poll_answer"]
	# @var my_chat_member Optional. The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user.
	@property
	def my_chat_member(self) -> ChatMemberUpdated:
		return self._d["my_chat_member"]
	# @var chat_member Optional. A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify "chat_member" in the list of allowed_updates to receive these updates.
	@property
	def chat_member(self) -> ChatMemberUpdated:
		return self._d["chat_member"]
	# @var chat_join_request Optional. A request to join the chat has been sent. The bot must have the can_invite_users administrator right in the chat to receive these updates.
	@property
	def chat_join_request(self) -> ChatJoinRequest:
		return self._d["chat_join_request"]

