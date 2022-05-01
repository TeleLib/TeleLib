import * as type from '../types'
import Type from './type'


export declare type JsonChatMemberUpdated = {
	chat: type.JsonChat
	from: type.JsonUser
	date: type.Number
	old_chat_member: type.JsonChatMember
	new_chat_member: type.JsonChatMember
	invite_link? : type.JsonChatInviteLink
}


export default class ChatMemberUpdated extends Type {
	chat: type.Chat
	from: type.User
	date: type.Number
	old_chat_member: type.ChatMember
	new_chat_member: type.ChatMember
	invite_link? : type.ChatInviteLink

	defaultObject!: JsonChatMemberUpdated

	constructor(ChatMemberUpdated: JsonChatMemberUpdated) {
		super()

		this.defaultObject = ChatMemberUpdated

		this.chat = new type.Chat(ChatMemberUpdated.chat)
		this.from = new type.User(ChatMemberUpdated.from)
		this.date = ChatMemberUpdated.date
		this.old_chat_member = new type.ChatMember(ChatMemberUpdated.old_chat_member)
		this.new_chat_member = new type.ChatMember(ChatMemberUpdated.new_chat_member)
		this.invite_link = ChatMemberUpdated.invite_link ? new type.ChatInviteLink(ChatMemberUpdated.invite_link) : undefined

	}
}