import * as type from '../types'
import Type from './type'


export declare type JsonVoiceChatEnded = {
	chat_id: type.ChatId
}


export default class VoiceChatEnded extends Type {
	chat_id: type.ChatId

	defaultObject!: JsonVoiceChatEnded

	constructor(options: JsonVoiceChatEnded) {
		super()

		this.defaultObject = options

		this.chat_id = options.chat_id
	}
}


