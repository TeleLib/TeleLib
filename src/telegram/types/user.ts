import * as type from '../types'
import Type from './type'

export declare type JsonUser = {
	id: type.UserId
	is_bot: type.Boolean
	first_name?: type.String
	last_name?: type.String
	username?: type.String
	language_code?: type.LanguageCode
	can_join_groups?: type.Boolean
	can_read_all_group_messages?: type.Boolean
	supports_inline_queries?: type.Boolean
}

export default class User extends Type {
	id!: type.UserId
	is_bot!: type.Boolean
	first_name?: type.String
	last_name?: type.String
	username?: type.String
	language_code?: type.LanguageCode
	can_join_groups?: type.Boolean
	can_read_all_group_messages?: type.Boolean
	supports_inline_queries?: type.Boolean

	defaultObject!: JsonUser

	constructor(user: JsonUser) {
		super()
		this.defaultObject = user
		this.id = user.id
		this.is_bot = user.is_bot
		this.first_name = user.first_name
		this.last_name = user.last_name
		this.username = user.username
		this.language_code = user.language_code
		this.can_join_groups = user.can_join_groups
		this.can_read_all_group_messages = user.can_read_all_group_messages
		this.supports_inline_queries = user.supports_inline_queries
	}
}
