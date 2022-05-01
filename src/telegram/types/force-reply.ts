import * as type from '../types'
import Type from './type'




export declare type JsonForceReply = {
	force_reply?: true
	input_field_placeholder?: type.Str
	selective?: type.Bool
}



export default class ForceReply extends Type {
	force_reply?: true
	input_field_placeholder?: type.Str
	selective?: type.Bool

	defaultObject!: JsonForceReply

	constructor(properties: JsonForceReply) {
		super()

		this.defaultObject = properties

		this.force_reply = properties.force_reply
		this.input_field_placeholder = properties.input_field_placeholder
		this.selective = properties.selective
	}
}