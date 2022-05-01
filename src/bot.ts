/* eslint-disable no-var */
import axios from 'axios'
import Telegram from './telegram'
import { AllowedUpdates, response, Update, Number as Num, String as Str, JsonUpdate, User, CURRENT_UPDATE_TYPES } from './telegram/types'
import colors from 'colors-cli'
import Methods from './telegram/methods'
import Logger from './logger'


const longPollingConfig = {
	timeout: 30,
	interval: 300,
	offset: 0,
	polling_timeout: null,
}


declare global {
	var methods: Methods
	var debug: boolean
	var config: config
	var update: Update
	var me: User
}


declare type config = {
	telegram: {
		token: Str,
		api_url?: Str,
		allowed_update_type?: AllowedUpdates[],
		update_pull_limit?: Num,
	}
	debug?: boolean,
}

export default class Bot {
	config: config
	client: Telegram

	loop_timeout: any = null

	constructor(config: config) {
		if (config.debug === undefined) {
			config.debug = false
			Logger.debug('no debug mode is defined, running in debug mode.')
		}

		globalThis.debug = config.debug

		Logger.debug('Bot is running in debug mode')
		if (!config.debug) {
			console.log(colors.blue_bbt('[DEBUG]'), colors.blue_bbt('debug mode is disabled.'))
		}

		if (!config.telegram.token) {
			Logger.debug('no Token is provided. Bot is not running')
			Logger.debug('Closing the process.')

			throw Error('Token should be Provided in `config`.')
			process.exit(1)
		}

		if (!config.telegram.allowed_update_type) {
			Logger.debug('no api_url is provided. Using the default value')
			Logger.debug('allowed_update_type = ' + CURRENT_UPDATE_TYPES.join(', '))

			config.telegram.allowed_update_type = CURRENT_UPDATE_TYPES
		}

		if (!config.telegram.api_url) {
			Logger.debug('no api_url is provided. Using the default value')
			Logger.debug('api_url = https://api.telegram.org/bot')

			config.telegram.api_url = 'https://api.telegram.org/bot'
		}

		if (!config.telegram.update_pull_limit) {
			Logger.debug('no update_pull_limit is provided. Using the default value')
			Logger.debug('update_pull_limit = 100')

			config.telegram.update_pull_limit = 100
		}

		this.config = config
		globalThis.config = config
		axios.defaults.baseURL = `${config.telegram.api_url}${config.telegram.token}/`
		this.client = new Telegram(axios)
	}

	stop = () => {
		Logger.debug('Stopping Process.')

		clearTimeout(this.loop_timeout)

		Logger.debug('Process Stopped.')
		Logger.debug('Bye =)')
		process.exit(0)
	}

	// fetches all updates and loads them in Telegram.handle method, asynchronously in an infinite loop.
	start = () => {
		Logger.debug('looping over', colors.blue_bt(String(longPollingConfig.offset)))

		if (this.loop_timeout === null) {
			Logger.debug('Initializing loop with the config:', longPollingConfig)
			Logger.debug('Listening on `SIGINT` and `SIGTERM` to gracefully kill the process.')
		}

		process.once('SIGINT', this.stop)
		process.once('SIGTERM', this.stop)

		this.client.methods
			.getUpdates(
				longPollingConfig.offset + 1,
				longPollingConfig.timeout,
				this.config.telegram.update_pull_limit,
				this.config.telegram.allowed_update_type
			)
			.then(
				(res: response<JsonUpdate[]>) =>
					res.result.forEach(
						(_update: JsonUpdate) => {
							// set the offset to latest received updates.
							const update = new Update(_update)
							Logger.tag(['[UPDATE_LOG]']).debug('last_received_update_id:', colors.blue_bt(String(update.update_id)))
							Logger.tag(['[UPDATE_LOG]']).debug('last_received_update:', _update)
							longPollingConfig.offset = update.update_id
							this
								.client
								.handle(update)
						}
					),
			)
			.finally(
				() => this.loop_timeout = setTimeout(
					this.start,
					longPollingConfig.interval
				)
			)
	}
}
