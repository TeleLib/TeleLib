import * as type from '../types'
import Type from './type'


export declare type JsonVoiceChatStarted = {
	chat_id: type.ChatId
	performer: type.JsonUser
	title: type.String
}


export default class VoiceChatStarted extends Type {
	chat_id: type.ChatId
	performer: type.User
	title: type.String

	defaultObject!: JsonVoiceChatStarted

	constructor(options: JsonVoiceChatStarted) {
		super()

		this.defaultObject = options

		this.chat_id = options.chat_id
		this.performer = new type.User(options.performer)
		this.title = options.title
	}
}


