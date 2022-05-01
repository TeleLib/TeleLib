import * as type from '../types'
import Type from './type'



export declare type JsonVoiceChatScheduled = {
	chat_id: type.ChatId
	date: type.Number
}


export default class VoiceChatScheduled extends Type {
	chat_id: type.ChatId
	date: type.Number

	defaultObject!: JsonVoiceChatScheduled

	constructor(options: JsonVoiceChatScheduled) {
		super()

		this.defaultObject = options

		this.chat_id = options.chat_id
		this.date = options.date
	}
}


