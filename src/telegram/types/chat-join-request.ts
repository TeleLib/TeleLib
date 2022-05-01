import * as type from '../types'
import Type from './type'


export declare type JsonChatJoinRequest = {
	chat: type.JsonChat
	from: type.JsonUser
	date: type.Number
	bio?: type.String
	invite_link? : type.JsonChatInviteLink
}


export default class ChatJoinRequest extends Type {
	chat: type.Chat
	from: type.User
	date: type.Number
	bio?: type.String
	invite_link? : type.ChatInviteLink

	defaultObject!: JsonChatJoinRequest

	constructor(ChatJoinRequest: JsonChatJoinRequest) {
		super()

		this.defaultObject = ChatJoinRequest

		this.chat = new type.Chat(ChatJoinRequest.chat)
		this.from = new type.User(ChatJoinRequest.from)
		this.date = ChatJoinRequest.date
		this.bio = ChatJoinRequest.bio
		this.invite_link = ChatJoinRequest.invite_link ? new type.ChatInviteLink(ChatJoinRequest.invite_link) : undefined
	}
}