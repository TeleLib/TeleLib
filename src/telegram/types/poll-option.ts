import * as type from '../types'
import Type from './type'

export declare type JsonPollOption = {
	text: type.String
	voter_count: type.Number
}

export default class PollOption extends Type {
	text: type.String
	voter_count: type.Number

	defaultObject!: JsonPollOption
	constructor(options: JsonPollOption) {
		super()

		this.defaultObject = options

		this.text = options.text
		this.voter_count = options.voter_count
	}
}
