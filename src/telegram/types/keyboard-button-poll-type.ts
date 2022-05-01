
import * as type from '../types'
import Type from './type'



export declare type JsonKeyboardButtonPollType = {
	type: '*' | type.PollType
}


export default class KeyboardButtonPollType extends Type {
	type: '*' | type.PollType

	defaultObject!: JsonKeyboardButtonPollType

	constructor(properties: JsonKeyboardButtonPollType) {
		super()

		this.defaultObject = properties

		this.type = properties.type
	}
}