import * as type from '../types'
import Type from './type'


export declare type JsonPollAnswer = {
	poll_id: type.String
	user: type.JsonUser
	option_ids: type.Number[]
}

export default class PollAnswer extends Type {
	poll_id: type.String
	user: type.User
	option_ids: type.Number[]

	defaultObject!: JsonPollAnswer
	constructor(options: JsonPollAnswer) {
		super()

		this.defaultObject = options

		this.poll_id = options.poll_id
		this.user = new type.User(options.user)
		this.option_ids = options.option_ids
	}
}
