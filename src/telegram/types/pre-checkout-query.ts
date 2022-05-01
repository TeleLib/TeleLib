

import * as type from '../types'
import Type from './type'


export declare type JsonPreCheckoutQuery = {
	id: type.String
	from: type.JsonUser
	currency: type.String
	total_amount: type.Number
	invoice_payload: type.String
	shipping_option_id?: type.String
	order_info?: type.JsonOrderInfo
}


export default class PreCheckoutQuery extends Type {
	id: type.String
	from: type.User
	currency: type.String
	total_amount: type.Number
	invoice_payload: type.String
	shipping_option_id?: type.String
	order_info?: type.OrderInfo

	defaultObject!: JsonPreCheckoutQuery

	constructor(PreCheckoutQuery: JsonPreCheckoutQuery) {
		super()

		this.defaultObject = PreCheckoutQuery

		this.id = PreCheckoutQuery.id
		this.from = new type.User(PreCheckoutQuery.from)
		this.currency = PreCheckoutQuery.currency
		this.total_amount = PreCheckoutQuery.total_amount
		this.invoice_payload = PreCheckoutQuery.invoice_payload
		this.shipping_option_id = PreCheckoutQuery.shipping_option_id
		this.order_info = PreCheckoutQuery.order_info ? new type.OrderInfo(PreCheckoutQuery.order_info) : undefined
	}
}