import * as type from '../types'
import Type from './type'


export declare type JsonPassportFile = {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	file_size: type.Number
	file_date: type.Number
}


export default class PassportFile extends Type {
	file_id: type.FileId
	file_unique_id: type.UniqueFileId
	file_size: type.Number
	file_date: type.Number

	defaultObject!: JsonPassportFile

	constructor(passportFile: JsonPassportFile) {
		super()
		this.defaultObject = passportFile

		this.file_id = passportFile.file_id
		this.file_unique_id = passportFile.file_unique_id
		this.file_size = passportFile.file_size
		this.file_date = passportFile.file_date
	}
}