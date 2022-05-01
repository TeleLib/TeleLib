import * as type from '../types'
import Type from './type'


export declare type JsonVoiceChatParticipantsInvited = {
	chat_id: type.Number
	participant_ids: type.UserId[]
}


export default class VoiceChatParticipantsInvited extends Type {
	chat_id: type.Number
	participant_ids: type.UserId[]

	defaultObject!: JsonVoiceChatParticipantsInvited

	constructor(properties: JsonVoiceChatParticipantsInvited) {
		super()

		this.defaultObject = properties

		this.chat_id = properties.chat_id
		this.participant_ids = properties.participant_ids
	}

}