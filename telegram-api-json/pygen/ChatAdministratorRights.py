
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chatadministratorrights# ['Represents the rights of an administrator in a chat.']
class ChatAdministratorRights(DefaultType):

    
	# @var is_anonymous True, if the user's presence in the chat is hidden
	@property
	def is_anonymous(self) -> Boolean:
		return self._d["is_anonymous"]
	# @var can_manage_chat True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
	@property
	def can_manage_chat(self) -> Boolean:
		return self._d["can_manage_chat"]
	# @var can_delete_messages True, if the administrator can delete messages of other users
	@property
	def can_delete_messages(self) -> Boolean:
		return self._d["can_delete_messages"]
	# @var can_manage_video_chats True, if the administrator can manage video chats
	@property
	def can_manage_video_chats(self) -> Boolean:
		return self._d["can_manage_video_chats"]
	# @var can_restrict_members True, if the administrator can restrict, ban or unban chat members
	@property
	def can_restrict_members(self) -> Boolean:
		return self._d["can_restrict_members"]
	# @var can_promote_members True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
	@property
	def can_promote_members(self) -> Boolean:
		return self._d["can_promote_members"]
	# @var can_change_info True, if the user is allowed to change the chat title, photo and other settings
	@property
	def can_change_info(self) -> Boolean:
		return self._d["can_change_info"]
	# @var can_invite_users True, if the user is allowed to invite new users to the chat
	@property
	def can_invite_users(self) -> Boolean:
		return self._d["can_invite_users"]
	# @var can_post_messages Optional. True, if the administrator can post in the channel; channels only
	@property
	def can_post_messages(self) -> Boolean:
		return self._d["can_post_messages"]
	# @var can_edit_messages Optional. True, if the administrator can edit messages of other users and can pin messages; channels only
	@property
	def can_edit_messages(self) -> Boolean:
		return self._d["can_edit_messages"]
	# @var can_pin_messages Optional. True, if the user is allowed to pin messages; groups and supergroups only
	@property
	def can_pin_messages(self) -> Boolean:
		return self._d["can_pin_messages"]

