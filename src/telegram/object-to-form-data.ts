import FormData from 'form-data'
import { InputFile, ReplyMarkup, InlineKeyboardMarkup } from './types'
import fs from 'node:fs'

function isObject(value: any) {
	return value === Object(value)
}

function isArray(value: any) {
	return Array.isArray(value)
}

export function serialize(obj: any, fd?: FormData, pre = '') {
	fd = fd || new FormData()

	if (obj instanceof InputFile) {
		fd.append(pre, fs.createReadStream(obj.file_path), obj.file_name)
	}

	else if (obj instanceof ReplyMarkup || obj instanceof InlineKeyboardMarkup) {
		fd.append(pre, obj.toJSON())
	}

	else if (isArray(obj)) {
		if (obj.length) {
			obj.forEach((value: any, index: any) => {
				serialize(value, fd, pre + '[' + index + ']')
			})
		} else {
			fd.append(pre + '[]', '')
		}
	}


	else if (isObject(obj)) {
		Object.keys(obj).forEach((prop) => {
			const value = obj[prop]

			if (isArray(value)) {
				while (prop.length > 2 && prop.lastIndexOf('[]') === prop.length - 2) {
					prop = prop.substring(0, prop.length - 2)
				}
			}

			const key = pre
				? pre + '[' + prop + ']'
				: prop

			serialize(value, fd, key)
		})
	}

	else {
		fd.append(pre, obj)
	}

	return fd
}