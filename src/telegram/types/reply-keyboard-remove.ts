import * as type from '../types'
import Type from './type'




export declare type JsonReplyKeyboardRemove = {
	remove_keyboard: true
	selective?: type.Bool
}



export default class ReplyKeyboardRemove extends Type {
	remove_keyboard: true
	selective?: type.Bool

	defaultObject!: JsonReplyKeyboardRemove

	constructor(properties: JsonReplyKeyboardRemove) {
		super()

		this.defaultObject = properties

		this.remove_keyboard = properties.remove_keyboard
		this.selective = properties.selective
	}
}