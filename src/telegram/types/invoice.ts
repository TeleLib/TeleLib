import * as type from '../types'
import Type from './type'


export declare type JsonInvoice = {
	title: type.String
	description: type.String
	start_parameter: type.String
	currency: type.String
	total_amount: type.Number
}

export default class Invoice extends Type {
	title: type.String
	description: type.String
	start_parameter: type.String
	currency: type.String
	total_amount: type.Number

	defaultObject!: JsonInvoice
	constructor(options: JsonInvoice) {
		super()

		this.defaultObject = options

		this.title = options.title
		this.description = options.description
		this.start_parameter = options.start_parameter
		this.currency = options.currency
		this.total_amount = options.total_amount
	}
}