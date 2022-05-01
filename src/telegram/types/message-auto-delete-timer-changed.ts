import * as type from '../types'
import Type from './type'

export declare type JsonMessageAutoDeleteTimerChanged = {
	message_auto_delete_time: type.Number
}

export default class MessageAutoDeleteTimerChanged extends Type {
	message_auto_delete_time: type.Number

	defaultObject!: JsonMessageAutoDeleteTimerChanged
	constructor(options: JsonMessageAutoDeleteTimerChanged) {
		super()

		this.defaultObject = options

		this.message_auto_delete_time = options.message_auto_delete_time
	}
}
