import * as type from '../types'
import Type from './type'

export declare type JsonOrderInfo = {
	name?: type.String
	phone_number?: type.String
	email?: type.String
	shipping_address?: type.JsonShippingAddress
}

export default class OrderInfo extends Type {
	name?: type.String
	phone_number?: type.String
	email?: type.String
	shipping_address?: type.ShippingAddress

	defaultObject!: JsonOrderInfo

	constructor(object: JsonOrderInfo) {
		super()

		this.defaultObject = object

		this.name = object.name
		this.phone_number = object.phone_number
		this.email = object.email
		this.shipping_address = object.shipping_address
			? new type.ShippingAddress(object.shipping_address)
			: undefined
	}
}
