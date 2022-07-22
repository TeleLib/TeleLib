
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chatmemberrestricted# ['Represents a chat member that is under certain restrictions in the chat. Supergroups only.']
class ChatMemberRestricted(DefaultType):

    
	# @var status The member's status in the chat, always "restricted"
	@property
	def status(self) -> String:
		return self._d["status"]
	# @var user Information about the user
	@property
	def user(self) -> User:
		return self._d["user"]
	# @var is_member True, if the user is a member of the chat at the moment of the request
	@property
	def is_member(self) -> Boolean:
		return self._d["is_member"]
	# @var can_change_info True, if the user is allowed to change the chat title, photo and other settings
	@property
	def can_change_info(self) -> Boolean:
		return self._d["can_change_info"]
	# @var can_invite_users True, if the user is allowed to invite new users to the chat
	@property
	def can_invite_users(self) -> Boolean:
		return self._d["can_invite_users"]
	# @var can_pin_messages True, if the user is allowed to pin messages
	@property
	def can_pin_messages(self) -> Boolean:
		return self._d["can_pin_messages"]
	# @var can_send_messages True, if the user is allowed to send text messages, contacts, locations and venues
	@property
	def can_send_messages(self) -> Boolean:
		return self._d["can_send_messages"]
	# @var can_send_media_messages True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
	@property
	def can_send_media_messages(self) -> Boolean:
		return self._d["can_send_media_messages"]
	# @var can_send_polls True, if the user is allowed to send polls
	@property
	def can_send_polls(self) -> Boolean:
		return self._d["can_send_polls"]
	# @var can_send_other_messages True, if the user is allowed to send animations, games, stickers and use inline bots
	@property
	def can_send_other_messages(self) -> Boolean:
		return self._d["can_send_other_messages"]
	# @var can_add_web_page_previews True, if the user is allowed to add web page previews to their messages
	@property
	def can_add_web_page_previews(self) -> Boolean:
		return self._d["can_add_web_page_previews"]
	# @var until_date Date when restrictions will be lifted for this user; unix time. If 0, then the user is restricted forever
	@property
	def until_date(self) -> Integer:
		return self._d["until_date"]

