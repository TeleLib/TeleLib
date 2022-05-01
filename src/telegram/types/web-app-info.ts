
import * as type from '../types'
import Type from './type'



export declare type JsonWebAppInfo = {
	url: type.HttpsUrl
}


export default class WebAppInfo extends Type {
	url: type.HttpsUrl

	defaultObject!: JsonWebAppInfo

	constructor(properties: JsonWebAppInfo) {
		super()

		this.defaultObject = properties

		this.url = properties.url
	}
}