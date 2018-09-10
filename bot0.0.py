import botlib as bl
import datetime

token = '632431770:AAE-UTV3V1P9qlNH2qTNhQ2X_ZSQOEmndcw'
greet_bot = bl.BotHandler(token)
greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()


def main():
	new_offset = None
	today = now.day
	hour = now.hour
	new_timeout=20
	now_time = now

	while True:
		greet_bot.get_updates(new_offset, new_timeout)

		last_update=greet_bot.get_last_update()
		print (last_update, datetime.datetime.now())

		if last_update:
			last_update_id = last_update['update_id']
			last_chat_text = last_update['message']['text']
			last_chat_id = last_update['message']['chat']['id']
			last_chat_name = last_update['message']['chat']['first_name']

			if last_chat_text.lower() in greetings and today == now.day and 6 <= hour <12:
				greet_bot.send_mess(last_chat_id, 'Good Morning, {}'.format(last_chat_name))
				#today+=1
				new_offset = last_update_id + 1

			elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour <17:
				greet_bot.send_mess(last_chat_id, 'Good Afternoon, {}'.format(last_chat_name))
				#today+=1
				new_offset = last_update_id + 1

			elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour <23:
				greet_bot.send_mess(last_chat_id, 'Good Evening, {}'.format(last_chat_name))
				#today+=1

				new_offset = last_update_id + 1
			else:
				greet_bot.send_mess(last_chat_id, 'I am sorry. I do not know what to say.')
				new_offset = last_update_id + 1


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()