
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chatpermissions# ['Describes actions that a non-administrator user is allowed to take in a chat.']
class ChatPermissions(DefaultType):

    
	# @var can_send_messages Optional. True, if the user is allowed to send text messages, contacts, locations and venues
	@property
	def can_send_messages(self) -> Boolean:
		return self._d["can_send_messages"]
	# @var can_send_media_messages Optional. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages
	@property
	def can_send_media_messages(self) -> Boolean:
		return self._d["can_send_media_messages"]
	# @var can_send_polls Optional. True, if the user is allowed to send polls, implies can_send_messages
	@property
	def can_send_polls(self) -> Boolean:
		return self._d["can_send_polls"]
	# @var can_send_other_messages Optional. True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages
	@property
	def can_send_other_messages(self) -> Boolean:
		return self._d["can_send_other_messages"]
	# @var can_add_web_page_previews Optional. True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages
	@property
	def can_add_web_page_previews(self) -> Boolean:
		return self._d["can_add_web_page_previews"]
	# @var can_change_info Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
	@property
	def can_change_info(self) -> Boolean:
		return self._d["can_change_info"]
	# @var can_invite_users Optional. True, if the user is allowed to invite new users to the chat
	@property
	def can_invite_users(self) -> Boolean:
		return self._d["can_invite_users"]
	# @var can_pin_messages Optional. True, if the user is allowed to pin messages. Ignored in public supergroups
	@property
	def can_pin_messages(self) -> Boolean:
		return self._d["can_pin_messages"]

