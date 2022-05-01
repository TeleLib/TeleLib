
import * as type from '../types'
import Type from './type'



export declare type JsonWebAppData = {
	data: type.Str
	button_text: type.Str
}


export default class WebAppData extends Type {
	data: type.Str
	button_text: type.Str

	defaultObject!: JsonWebAppData

	constructor(properties: JsonWebAppData) {
		super()

		this.defaultObject = properties

		this.data = properties.data
		this.button_text = properties.button_text
	}
}