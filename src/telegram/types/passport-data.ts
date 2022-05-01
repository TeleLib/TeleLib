import * as type from '../types'
import Type from './type'

export declare type JsonPassportData = {
	data: type.JsonEncryptedPassportElement[]
	credential: type.JsonEncryptedCredentials
}

export default class PassportData extends Type {
	data: type.EncryptedPassportElement[]
	credential: type.EncryptedCredentials

	defaultObject!: JsonPassportData

	constructor(passportData: JsonPassportData) {
		super()
		this.defaultObject = passportData

		this.data = passportData.data.map(data => new type.EncryptedPassportElement(data))
		this.credential = new type.EncryptedCredentials(passportData.credential)
	}
}