import * as type from '../types'
import Type from './type'

export declare type JsonChat = {
	id: type.ChatId
	type: type.ChatType
	title?: type.String
	first_name?: type.String
	last_name?: type.String
	username?: type.String
	photo?: type.JsonChatPhoto
	bio?: type.String
	has_private_forwards?: type.Boolean
	description?: type.String
	invite_link?: type.String
	pinned_message?: type.JsonMessage
	permissions?: type.JsonChatPermissions
	slow_mode_delay?: type.Number
	message_auto_delete_time?: type.Number
	has_protected_content?: type.Boolean
	sticker_set_name?: type.String
	can_set_sticker_set?: type.Boolean
	linked_chat_id?: type.ChatId
	location?: type.JsonChatLocation
}

export default class Chat extends Type {
	id: type.ChatId
	type: type.ChatType
	title?: type.String
	first_name?: type.String
	last_name?: type.String
	username?: type.String
	photo?: type.ChatPhoto
	bio?: type.String
	has_private_forwards?: type.Boolean
	description?: type.String
	invite_link?: type.String
	pinned_message?: type.Message
	permissions?: type.ChatPermissions
	slow_mode_delay?: type.Number
	message_auto_delete_time?: type.Number
	has_protected_content?: type.Boolean
	sticker_set_name?: type.String
	can_set_sticker_set?: type.Boolean
	linked_chat_id?: type.ChatId
	location?: type.ChatLocation

	defaultObject!: JsonChat

	constructor(chat: JsonChat) {
		super()

		this.defaultObject = chat

		this.id = chat.id
		this.type = chat.type
		this.title = chat.title
		this.first_name = chat.first_name
		this.last_name = chat.last_name
		this.username = chat.username
		this.photo = chat.photo ? new type.ChatPhoto(chat.photo) : undefined
		this.bio = chat.bio
		this.has_private_forwards = chat.has_private_forwards
		this.description = chat.description
		this.invite_link = chat.invite_link
		this.pinned_message = chat.pinned_message
			? new type.Message(chat.pinned_message)
			: undefined
		this.permissions = chat.permissions ? new type.ChatPermissions(chat.permissions) : undefined
		this.slow_mode_delay = chat.slow_mode_delay
		this.message_auto_delete_time = chat.message_auto_delete_time
		this.has_protected_content = chat.has_protected_content
		this.sticker_set_name = chat.sticker_set_name
		this.can_set_sticker_set = chat.can_set_sticker_set
		this.linked_chat_id = chat.linked_chat_id
		this.location = chat.location ? new type.ChatLocation(chat.location) : undefined
	}
}
