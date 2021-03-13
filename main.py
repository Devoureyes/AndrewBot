from telegram import Update, bot, TelegramObject
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from User import User

questions = [
    '1. Мои доходы превышают расходы',
    '2. Мои накопления хранятся в разных валютах',
    '3. Я не храню деньги под матрасом, они должны работать',
    '4. У меня есть подушка безопасности в быстром доступе (сумма 3ех месячных расходов)',
    '5. Я использую ИИС для улучшения инвестиционного результата',
    '6. Я использую кэшбеки и программы лояльности в магазинах, куда постоянно хожу',
    '7. У меня есть финансовый план с целями и сроками их достижениями',
    '8. Я использую налоговые вычеты и льготы',
    '9. Я пользуюсь страховкой (жизни, каско, квартиры)',
    '10. Я знаю на что и сколько я трачу',
    '11. Я стараюсь не брать кредиты, а если и беру, то выплачиваю без просрочек и по-возможности закрываю досрочно',
    '12. Я формирую (пытаюсь) дополнительные источники заработка',
]

# users = []
user: object


def run_bot(update: Update, context: CallbackContext) -> None:
    #for user in users:
    replica = user.clear_phrase(update.message.text)
    if (replica != False):
        # global start
        if user.start == 1:
            num = user.correctAnswer(replica, questions)
            if (num == 100):
                answer = "Хотите ещё раз пройти тест?"
            else:
                if (num == len(questions)):
                    answer = user.getResult()
                    user.start = 0
                else:
                    answer = questions[num]
        else:
            answer = user.start_test(replica, questions)
    else:
        answer = "Ответьте либо да, либо нет"
    update.message.reply_text(answer)


def start(update: Update, context: CallbackContext) -> None:
    global user
    id = update.message.from_user.id
    user = User(0, 0, 0, id)
    # users.append(User(0, 0, 0, id))
    """Send a message when the command /start is issued."""
    update.message.reply_text('Привет! Хотите пройти тест?')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def main():
    """Start the bot."""
    updater = Updater("1658115182:AAHuYqQ6A5QRJsYK98IZPGvbUXp8ez3zFlo")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, run_bot))
    # Start the Bot
    updater.start_polling()
    updater.idle()


main()
