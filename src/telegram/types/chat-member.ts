import * as type from '../types'
import Type from './type'


export declare type JsonChatMemberOwner = {
	status: 'creator'
	user: type.JsonUser
	is_anonymous: type.Bool
	custom_title?: type.Str
}

export declare type JsonChatMemberAdministrator = {
	status: 'administrator'
	user: type.JsonUser
	can_be_edited: type.Bool
	is_anonymous: type.Bool
	custom_title?: type.Str

	can_manage_chat: type.Bool
	can_delete_messages: type.Bool
	can_manage_video_chats: type.Bool
	can_restrict_members: type.Bool
	can_promote_members: type.Bool
	can_change_info: type.Bool
	can_invite_users: type.Bool
	can_post_messages?: type.Bool
	can_edit_messages?: type.Bool
	can_pin_messages?: type.Bool
}

export declare type JsonChatMemberMember = {
	status: 'member'
	user: type.JsonUser
}

export declare type JsonChatMemberLeft = {
	status: 'left'
	user: type.JsonUser
}

export declare type JsonChatMemberBanned = {
	status: 'kicked'
	user: type.JsonUser
	until_date: type.Num
}

export declare type JsonChatMemberRestricted = {
	status: 'restricted'
	user: type.JsonUser
	is_member: type.Bool
	until_date: type.Num

	can_change_info: type.Bool
	can_invite_users: type.Bool
	can_pin_messages: type.Bool
	can_send_messages: type.Bool
	can_send_media_messages: type.Bool
	can_send_polls: type.Bool
	can_send_other_messages: type.Bool
	can_add_web_page_previews: type.Bool
}



export declare type JsonChatMember = {
	status: 'creator' | 'administrator' | 'member' | 'left' | 'kicked' | 'restricted'
	user: type.JsonUser

	is_anonymous?: type.Bool
	is_member?: type.Bool

	custom_title?: type.Str

	can_be_edited?: type.Bool

	until_date?: type.Num

	can_manage_chat?: type.Bool
	can_delete_messages?: type.Bool
	can_manage_video_chats?: type.Bool
	can_restrict_members?: type.Bool
	can_promote_members?: type.Bool
	can_change_info?: type.Bool
	can_invite_users?: type.Bool
	can_post_messages?: type.Bool
	can_edit_messages?: type.Bool
	can_pin_messages?: type.Bool

	can_send_messages?: type.Bool
	can_send_media_messages?: type.Bool
	can_send_polls?: type.Bool
	can_send_other_messages?: type.Bool
	can_add_web_page_previews?: type.Bool
}

export default class ChatMember extends Type {
	status: 'creator' | 'administrator' | 'member' | 'left' | 'kicked' | 'restricted'
	user: type.User

	is_anonymous?: type.Bool
	is_member?: type.Bool

	custom_title?: type.Str

	can_be_edited?: type.Bool

	until_date?: type.Num

	can_manage_chat?: type.Bool
	can_delete_messages?: type.Bool
	can_manage_video_chats?: type.Bool
	can_restrict_members?: type.Bool
	can_promote_members?: type.Bool
	can_change_info?: type.Bool
	can_invite_users?: type.Bool
	can_post_messages?: type.Bool
	can_edit_messages?: type.Bool
	can_pin_messages?: type.Bool

	can_send_messages?: type.Bool
	can_send_media_messages?: type.Bool
	can_send_polls?: type.Bool
	can_send_other_messages?: type.Bool
	can_add_web_page_previews?: type.Bool

	defaultObject!: JsonChatMember

	constructor(json: JsonChatMember) {
		super()

		this.defaultObject = json

		this.user = new type.User(json.user)
		this.status = json.status

		this.is_anonymous = json.is_anonymous
		this.is_member = json.is_member

		this.custom_title = json.custom_title

		this.can_be_edited = json.can_be_edited

		this.until_date = json.until_date

		this.can_manage_chat = json.can_manage_chat
		this.can_delete_messages = json.can_delete_messages
		this.can_manage_video_chats = json.can_manage_video_chats
		this.can_restrict_members = json.can_restrict_members
		this.can_promote_members = json.can_promote_members
		this.can_change_info = json.can_change_info
		this.can_invite_users = json.can_invite_users
		this.can_post_messages = json.can_post_messages
		this.can_edit_messages = json.can_edit_messages
		this.can_pin_messages = json.can_pin_messages

		this.can_send_messages = json.can_send_messages
		this.can_send_media_messages = json.can_send_media_messages
		this.can_send_polls = json.can_send_polls
		this.can_send_other_messages = json.can_send_other_messages
		this.can_add_web_page_previews = json.can_add_web_page_previews
	}
}