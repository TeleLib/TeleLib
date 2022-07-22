
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#chatinvitelink# ['Represents an invite link for a chat.']
class ChatInviteLink(DefaultType):

    
	# @var invite_link The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with "...".
	@property
	def invite_link(self) -> String:
		return self._d["invite_link"]
	# @var creator Creator of the link
	@property
	def creator(self) -> User:
		return self._d["creator"]
	# @var creates_join_request True, if users joining the chat via the link need to be approved by chat administrators
	@property
	def creates_join_request(self) -> Boolean:
		return self._d["creates_join_request"]
	# @var is_primary True, if the link is primary
	@property
	def is_primary(self) -> Boolean:
		return self._d["is_primary"]
	# @var is_revoked True, if the link is revoked
	@property
	def is_revoked(self) -> Boolean:
		return self._d["is_revoked"]
	# @var name Optional. Invite link name
	@property
	def name(self) -> String:
		return self._d["name"]
	# @var expire_date Optional. Point in time (Unix timestamp) when the link will expire or has been expired
	@property
	def expire_date(self) -> Integer:
		return self._d["expire_date"]
	# @var member_limit Optional. The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
	@property
	def member_limit(self) -> Integer:
		return self._d["member_limit"]
	# @var pending_join_request_count Optional. Number of pending join requests created using this link
	@property
	def pending_join_request_count(self) -> Integer:
		return self._d["pending_join_request_count"]

