import * as type from '../types'
import Type from './type'




export declare type JsonContact = {
	phone_number: type.String
	first_name: type.String
	last_name?: type.String
	user_id?: type.UserId
	vcard?: type.String
}


export default class Contact extends Type {
	phone_number: type.String
	first_name: type.String
	last_name?: type.String
	user_id?: type.UserId
	vcard?: type.String

	defaultObject!: JsonContact
	constructor(options: JsonContact) {
		super()

		this.defaultObject = options

		this.phone_number = options.phone_number
		this.first_name = options.first_name
		this.last_name = options.last_name || undefined
		this.user_id = options.user_id || undefined
		this.vcard = options.vcard || undefined
	}
}
