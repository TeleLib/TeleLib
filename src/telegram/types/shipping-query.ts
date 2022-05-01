import * as type from '../types'
import Type from './type'


export declare type JsonShippingQuery = {
	id: type.String
	from: type.JsonUser
	invoice_payload: type.String
	shipping_address: type.JsonShippingAddress
}


export default class ShippingQuery extends Type {
	id: type.String
	from: type.User
	invoice_payload: type.String
	shipping_address: type.ShippingAddress

	defaultObject!: JsonShippingQuery

	constructor(ShippingQuery: JsonShippingQuery) {
		super()

		this.defaultObject = ShippingQuery

		this.id = ShippingQuery.id
		this.from = new type.User(ShippingQuery.from)
		this.invoice_payload = ShippingQuery.invoice_payload
		this.shipping_address = new type.ShippingAddress(ShippingQuery.shipping_address)
	}
}