import * as type from '../types'
import Type from './type'

export declare type JsonChatPermissions = {
	can_send_messages?: type.Boolean
	can_send_media_messages?: type.Boolean
	can_send_polls?: type.Boolean
	can_send_other_messages?: type.Boolean
	can_add_web_page_previews?: type.Boolean
	can_change_info?: type.Boolean
	can_invite_users?: type.Boolean
	can_pin_messages?: type.Boolean
}

export default class ChatPermissions extends Type {
	can_send_messages?: type.Boolean
	can_send_media_messages?: type.Boolean
	can_send_polls?: type.Boolean
	can_send_other_messages?: type.Boolean
	can_add_web_page_previews?: type.Boolean
	can_change_info?: type.Boolean
	can_invite_users?: type.Boolean
	can_pin_messages?: type.Boolean

	defaultObject!: JsonChatPermissions

	constructor(chatPermissions: JsonChatPermissions) {
		super()
		this.defaultObject = chatPermissions

		this.can_send_messages = chatPermissions.can_send_messages
		this.can_send_media_messages = chatPermissions.can_send_media_messages
		this.can_send_polls = chatPermissions.can_send_polls
		this.can_send_other_messages = chatPermissions.can_send_other_messages
		this.can_add_web_page_previews = chatPermissions.can_add_web_page_previews
		this.can_change_info = chatPermissions.can_change_info
		this.can_invite_users = chatPermissions.can_invite_users
		this.can_pin_messages = chatPermissions.can_pin_messages
	}
}