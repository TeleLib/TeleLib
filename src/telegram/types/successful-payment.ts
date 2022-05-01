import * as type from '../types'
import Type from './type'

export declare type JsonSuccessfulPayment = {
	currency: type.String
	total_amount: type.Number
	invoice_payload: type.String
	shipping_option_id?: type.String
	order_info?: type.JsonOrderInfo
	telegram_payment_charge_id: type.String
	provider_payment_charge_id: type.String
}

export default class SuccessfulPayment extends Type {
	currency: type.String
	total_amount: type.Number
	invoice_payload: type.String
	shipping_option_id?: type.String
	order_info?: type.OrderInfo
	telegram_payment_charge_id: type.String
	provider_payment_charge_id: type.String

	defaultObject!: JsonSuccessfulPayment

	constructor(object: JsonSuccessfulPayment) {
		super()

		this.defaultObject = object

		this.currency = object.currency
		this.total_amount = object.total_amount
		this.invoice_payload = object.invoice_payload
		this.shipping_option_id = object.shipping_option_id
		this.order_info = object.order_info ? new type.OrderInfo(object.order_info) : undefined
		this.telegram_payment_charge_id = object.telegram_payment_charge_id
		this.provider_payment_charge_id = object.provider_payment_charge_id
	}
}
