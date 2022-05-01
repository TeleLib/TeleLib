import Bot from '../src/bot'

import {
	InlineKeyboardMarkup,
	Message,
	ReplyMarkup,
	InlineKeyboardButton,
	InputFile
} from '../src/telegram/types'

const _bot = new Bot({
	telegram: {
		token: '[TOKEN]',
	},
	debug: true
})


_bot.client.on(
	'message',
	(msg: Message) => {

		if (!msg.chat) {
			return msg.reply('no chat')
		}

		const key = new ReplyMarkup(
			new InlineKeyboardMarkup({
				inline_keyboard: [
					[
						new InlineKeyboardButton({
							text: 'hello',
							callback_data: 'hi'
						})
					]
				]
			})
		)

		_bot.client.methods.sendPhoto(msg.chat.id, new InputFile('./i.png', 'i.png'))

		_bot.client.methods.sendPhoto(msg.chat.id, new InputFile('./i.png', 'i.png'), 'test', undefined, undefined, undefined, key)

		if (msg.text) {
			return msg.reply(msg.text)
		}

		msg.reply(' i dunno that !')
	}
)


_bot.start()