import * as type from '../types'
import Type from './type'



export declare type JsonEncryptedCredentials = {
	data: type.String
	hash: type.String
	secret: type.String
}

export default class EncryptedCredentials extends Type {
	data: type.String
	hash: type.String
	secret: type.String

	defaultObject!: JsonEncryptedCredentials

	constructor(encryptedCredentials: JsonEncryptedCredentials) {
		super()
		this.defaultObject = encryptedCredentials

		this.data = encryptedCredentials.data
		this.hash = encryptedCredentials.hash
		this.secret = encryptedCredentials.secret
	}
}