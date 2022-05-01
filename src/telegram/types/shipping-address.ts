import * as type from '../types'
import Type from './type'


export declare type JsonShippingAddress = {
	country_code: type.String
	state: type.String
	city: type.String
	street_line1: type.String
	street_line2: type.String
	post_code: type.String
}


export default class ShippingAddress extends Type {
	country_code: type.String
	state: type.String
	city: type.String
	street_line1: type.String
	street_line2: type.String
	post_code: type.String

	defaultObject!: JsonShippingAddress

	constructor(object: JsonShippingAddress) {
		super()

		this.defaultObject = object

		this.country_code = object.country_code
		this.state = object.state
		this.city = object.city
		this.street_line1 = object.street_line1
		this.street_line2 = object.street_line2
		this.post_code = object.post_code
	}
}