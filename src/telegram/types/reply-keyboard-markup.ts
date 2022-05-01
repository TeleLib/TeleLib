import * as type from '../types'
import Type from './type'




export declare type JsonReplyKeyboardMarkup = {
	keyboard: type.JsonKeyboardButton[][]
	resize_keyboard?: type.Bool
	one_time_keyboard?: type.Bool
	selective?: type.Bool
}



export default class ReplyKeyboardMarkup extends Type {
	keyboard: type.KeyboardButton[][]
	resize_keyboard?: type.Bool
	one_time_keyboard?: type.Bool
	selective?: type.Bool

	defaultObject!: JsonReplyKeyboardMarkup

	constructor(properties: JsonReplyKeyboardMarkup) {
		super()

		this.defaultObject = properties

		this.keyboard = properties.keyboard.map(
			(i) => i.map(
				l => new type.KeyboardButton(l)
			)
		)
		this.resize_keyboard = properties.resize_keyboard
		this.one_time_keyboard = properties.one_time_keyboard
		this.selective = properties.selective
	}
}