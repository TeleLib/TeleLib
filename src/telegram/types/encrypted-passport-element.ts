import * as type from '../types'
import Type from './type'


export declare type JsonEncryptedPassportElement = {
	type: type.String
	data: type.String
	phone_number?: type.String
	email?: type.String
	files?: type.JsonPassportFile[]
	front_side?: type.JsonPassportFile
	reverse_side?: type.JsonPassportFile
	selfie?: type.JsonPassportFile
	translation?: type.JsonPassportFile[]
	hash: type.String
}

export default class EncryptedPassportElement extends Type {
	type: type.String
	data: type.String
	phone_number?: type.String
	email?: type.String
	files?: type.PassportFile[]
	front_side?: type.PassportFile
	reverse_side?: type.PassportFile
	selfie?: type.PassportFile
	translation?: type.PassportFile[]
	hash: type.String

	defaultObject!: JsonEncryptedPassportElement

	constructor(encryptedPassportElement: JsonEncryptedPassportElement) {
		super()
		this.defaultObject = encryptedPassportElement

		this.type = encryptedPassportElement.type
		this.data = encryptedPassportElement.data
		this.phone_number = encryptedPassportElement.phone_number
		this.email = encryptedPassportElement.email
		this.files = encryptedPassportElement.files ? encryptedPassportElement.files.map(file => new type.PassportFile(file)) : undefined
		this.front_side = encryptedPassportElement.front_side ? new type.PassportFile(encryptedPassportElement.front_side) : undefined
		this.reverse_side = encryptedPassportElement.reverse_side ? new type.PassportFile(encryptedPassportElement.reverse_side) : undefined
		this.selfie = encryptedPassportElement.selfie ? new type.PassportFile(encryptedPassportElement.selfie) : undefined
		this.translation = encryptedPassportElement.translation ? encryptedPassportElement.translation.map(file => new type.PassportFile(file)) : undefined
		this.hash = encryptedPassportElement.hash
	}
}
