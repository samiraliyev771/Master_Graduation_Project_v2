from telegram import ReplyKeyboardMarkup
import telegram
from telegram.ext import Updater, CommandHandler
import requests



bot = telegram.Bot('1780780782:AAGSGKBe12aNd9Yh82VpkEQvD1vrMMf1IvM')       					# @JestDiliBot token
updater = Updater("1780780782:AAGSGKBe12aNd9Yh82VpkEQvD1vrMMf1IvM", use_context=True)		# @JestDiliBot token

updates = bot.get_updates()

userIdFile = open('userId-backup1.txt', 'r')					# Open userId.txt file and assign it to 'userIdFile' variable.
line1 = userIdFile.readline()							# Take first line of the file and assign it to 'line1' variable.
line1 = line1.strip('[]\n').split(', ')					# Strip off the '[', ']', '\n' symbols of the 'line1' text and split text by ', '
														# and save it again in 'line1' as list of strings.
chat_id = [int(i) for i in line1]						# Convert string values of the list to the integer values and save as 'chat_id' list.
print(chat_id)											# Just print the outcome for checking. 


#txt = 'Əlləri ilə danışanları hər kəsin anlaması üçün göstərdiyiniz köməyə görə minnətdarıq. Məlumat üçün bildirək ki, artıq sayənizdə xeyli şəkil və video toplanıb. Belə də davam edin və botu yaxınlarınızla da paylaşın. Əllərinizə sağlıq!'

txt = 'Əlləri ilə danışanları hər kəsin anlaması üçün göstərdiyiniz köməyə görə minnətdarıq. Biz sizinlə artıq böyük bir komandayıq! Nümunə sayı nə qədər çox olarsa, tanınma dəqiqliyi də bir o qədər çox olacaq, nümunələr çəkib göndərməkdə davam edin. Əllərinizə sağlıq!'


for id in chat_id:										# Send messages to all users in the list by iterating 'chat_id' list.
	#print(id)
	try:
		bot.send_message(id, txt)
	except:
		print("Problem with %s" % id)
		pass


updater.start_polling()
