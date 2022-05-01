import * as type from '../types'
import Type from './type'




export declare type JsonPoll = {
	id: type.String
	question: type.String
	options: type.JsonPollOption[]
	total_voter_count: type.Number
	is_closed: type.Boolean
	is_anonymous: type.Boolean
	type: type.PollType
	allows_multiple_answers: type.Boolean
	correct_option_id?: type.Number
	explanation?: type.String
	explanation_entities?: type.JsonMessageEntity[]
	open_period?: type.Number
	close_date?: type.Number
}


export default class Poll extends Type {
	id: type.String
	question: type.String
	options: type.PollOption[]
	total_voter_count: type.Number
	is_closed: type.Boolean
	is_anonymous: type.Boolean
	type: type.PollType
	allows_multiple_answers: type.Boolean
	correct_option_id?: type.Number
	explanation?: type.String
	explanation_entities?: type.MessageEntity[]
	open_period?: type.Number
	close_date?: type.Number

	defaultObject!: JsonPoll
	constructor(options: JsonPoll) {
		super()

		this.defaultObject = options

		this.id = options.id
		this.question = options.question
		this.options = options.options.map(o => new type.PollOption(o))
		this.total_voter_count = options.total_voter_count
		this.is_closed = options.is_closed
		this.is_anonymous = options.is_anonymous
		this.type = options.type
		this.allows_multiple_answers = options.allows_multiple_answers
		this.correct_option_id = options.correct_option_id || undefined
		this.explanation = options.explanation || undefined
		this.explanation_entities = options.explanation_entities && options.explanation_entities.map(e => new type.MessageEntity(e)) || undefined
		this.open_period = options.open_period || undefined
		this.close_date = options.close_date || undefined
	}
}