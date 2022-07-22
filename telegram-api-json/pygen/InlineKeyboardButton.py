
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinekeyboardbutton# ['This object represents one button of an inline keyboard. You must use exactly one of the optional fields.']
class InlineKeyboardButton(DefaultType):

    
	# @var text Label text on the button
	@property
	def text(self) -> String:
		return self._d["text"]
	# @var url Optional. HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their ID without using a username, if this is allowed by their privacy settings.
	@property
	def url(self) -> String:
		return self._d["url"]
	# @var callback_data Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
	@property
	def callback_data(self) -> String:
		return self._d["callback_data"]
	# @var web_app Optional. Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Available only in private chats between a user and the bot.
	@property
	def web_app(self) -> WebAppInfo:
		return self._d["web_app"]
	# @var login_url Optional. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
	@property
	def login_url(self) -> LoginUrl:
		return self._d["login_url"]
	# @var switch_inline_query Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted. Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm... actions - in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
	@property
	def switch_inline_query(self) -> String:
		return self._d["switch_inline_query"]
	# @var switch_inline_query_current_chat Optional. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted. This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options.
	@property
	def switch_inline_query_current_chat(self) -> String:
		return self._d["switch_inline_query_current_chat"]
	# @var callback_game Optional. Description of the game that will be launched when the user presses the button. NOTE: This type of button must always be the first button in the first row.
	@property
	def callback_game(self) -> CallbackGame:
		return self._d["callback_game"]
	# @var pay Optional. Specify True, to send a Pay button. NOTE: This type of button must always be the first button in the first row and can only be used in invoice messages.
	@property
	def pay(self) -> Boolean:
		return self._d["pay"]

