import * as type from '../types'
import Type from './type'


export declare type JsonChatInviteLink = {
	invite_link: type.String
	creator:  type.JsonUser
	creates_join_request:  type.Boolean
	is_primary:  type.Boolean
	is_revoked:  type.Boolean
	name: type.String
	expire_date: type.Number
	member_limit?:  type.Number
	pending_join_request_count?:  type.Number
}


export default class ChatInviteLink extends Type {
	invite_link: type.String
	creator:  type.User
	creates_join_request:  type.Boolean
	is_primary:  type.Boolean
	is_revoked:  type.Boolean
	name: type.String
	expire_date: type.Number
	member_limit?:  type.Number
	pending_join_request_count?:  type.Number

	defaultObject!: JsonChatInviteLink

	constructor(ChatJoinRequest: JsonChatInviteLink) {
		super()

		this.defaultObject = ChatJoinRequest

		this.invite_link = ChatJoinRequest.invite_link
		this.creator = new type.User(ChatJoinRequest.creator)
		this.creates_join_request = ChatJoinRequest.creates_join_request
		this.is_primary = ChatJoinRequest.is_primary
		this.is_revoked = ChatJoinRequest.is_revoked
		this.name = ChatJoinRequest.name
		this.expire_date = ChatJoinRequest.expire_date
		this.member_limit = ChatJoinRequest.member_limit
		this.pending_join_request_count = ChatJoinRequest.pending_join_request_count
	}
}