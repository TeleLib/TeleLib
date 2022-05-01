import { Bot, types } from '../src/index'

const _bot = new Bot({
	telegram: {
		token: '[TOKEN]',
	},
	debug: true
})


_bot.client.on(
	'message',
	(msg: types.Message) => {

		if (msg.onMatch(/\/start/, () => {
			return msg.reply('hey there') as unknown as boolean
		})) return true

		if (msg.onMatch(/\$\$<(photo)\$\$type>/, () => {
			return msg.reply('photo there') as unknown as boolean
		})) return true

		// see the function to see how it works.

		if (!msg.chat) {
			return msg.reply('no chat')
		}

		const key = new types.ReplyMarkup(
			new types.InlineKeyboardMarkup({
				inline_keyboard: [
					[
						new types.InlineKeyboardButton({
							text: 'hello',
							callback_data: 'hi'
						})
					]
				]
			})
		)

		_bot.client.methods.sendPhoto(msg.chat.id, new types.InputFile('./i.png', 'i.png'))

		_bot.client.methods.sendPhoto(msg.chat.id, new types.InputFile('./i.png', 'i.png'), 'test', undefined, undefined, undefined, key)

		if (msg.text) {
			return msg.reply(msg.text)
		}

		msg.reply(' i dunno that !')
	}
)


_bot.start()