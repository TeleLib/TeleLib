import * as type from '../types'
import Type from './type'

export declare type JsonVenue = {
	location: type.JsonLocation
	title: type.String
	address: type.String
	foursquare_id?: type.String
	foursquare_type?: type.String
	google_place_id?: type.String
	google_place_type?: type.String
}

export default class Venue extends Type {
	location: type.Location
	title: type.String
	address: type.String
	foursquare_id?: type.String
	foursquare_type?: type.String
	google_place_id?: type.String
	google_place_type?: type.String

	defaultObject!: JsonVenue
	constructor(options: JsonVenue) {
		super()

		this.defaultObject = options

		this.location = new type.Location(options.location)
		this.title = options.title
		this.address = options.address
		this.foursquare_id = options.foursquare_id || undefined
		this.foursquare_type = options.foursquare_type || undefined
		this.google_place_id = options.google_place_id || undefined
		this.google_place_type = options.google_place_type || undefined
	}
}
