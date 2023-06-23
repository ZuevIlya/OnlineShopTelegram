import callback

import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

# log
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

# prices
PRICE1 = types.LabeledPrice(label="575 Wild Cores - 300RUB", amount=300 * 100)  # в копейках (руб)
PRICE2 = types.LabeledPrice(label="1050 Wild Cores - 600RUB", amount=600 * 100)  # в копейках (руб)
PRICE3 = types.LabeledPrice(label="2200 Wild Cores - 1200RUB", amount=1200 * 100)  # в копейках (руб)
PRICE4 = types.LabeledPrice(label="5500 Wild Cores - 2500RUB", amount=2500 * 100)  # в копейках (руб)
PRICE5 = types.LabeledPrice(label="11000 Wild Cores - 5000RUB", amount=5000 * 100)  # в копейках (руб)


@dp.message_handler(commands=['start'])
async def firstAnswer(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup1 = types.InlineKeyboardButton('Купить игровую валюту по низкой цене', callback_data='prices')
    markup2 = types.InlineKeyboardButton('Связаться с администратором', callback_data='administrator')
    markup.add(markup1)
    markup.add(markup2)
    markup3 = types.InlineKeyboardButton('Наша группа в Telegram', url='https://t.me/leagueofakshan')
    markup4 = types.InlineKeyboardButton('Наша беседа в Telegram', url='https://t.me/+ULE-Y09c0BJhNGU6')
    markup.row(markup3, markup4)
    markup5 = types.InlineKeyboardButton('Наша группа ВКонтакте', url='https://vk.com/leagueofakshan')
    markup6 = types.InlineKeyboardButton('Наша беседа ВКонтакте', url='https://vk.me/join/AJQ1d6Q7mR2eQgYgL6lkChcc')
    markup.row(markup5, markup6)
    await message.reply('Что вас интересует?', reply_markup=markup)


@dp.callback_query_handler(lambda call: True)
async def callback(callback: types.CallbackQuery):
    message: types.Message
    if callback.data == 'prices':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('575 Wild Cores - 300RUB', callback_data='price1'))
        markup.add(types.InlineKeyboardButton('1050 Wild Cores - 600RUB', callback_data='price2'))
        markup.add(types.InlineKeyboardButton('2200 Wild Cores - 1200RUB', callback_data='price3'))
        markup.add(types.InlineKeyboardButton('5500 Wild Cores - 2500RUB', callback_data='price4'))
        markup.add(types.InlineKeyboardButton('11000 Wild Cores - 5000RUB', callback_data='price5'))
        await callback.message.reply('Какой набор вы хотите выбрать?', reply_markup=markup)

    if callback.data == 'price1':
        if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
            await callback.message.answer("Ваш товар")
        await bot.send_invoice(chat_id=callback.from_user.id,
                                   title="575 Wild Cores",
                                   description="Пакет на 575 Wild Cores",
                                   provider_token=config.PAYMENTS_TOKEN,
                                   currency="rub",
                                   photo_url="https://ibb.co/vLq5PH3",
                                   photo_width=512,
                                   photo_height=512,
                                   photo_size=512,
                                   is_flexible=False,
                                   prices=[PRICE1],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload")

    if callback.data == 'price2':
        if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
            await callback.message.answer("Ваш товар")
        await bot.send_invoice(chat_id=callback.from_user.id,
                                   title="1050 Wild Cores",
                                   description="Пакет на 1050 Wild Cores",
                                   provider_token=config.PAYMENTS_TOKEN,
                                   currency="rub",
                                   photo_url="1050.jpeg",
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   is_flexible=False,
                                   prices=[PRICE2],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload")

    if callback.data == 'price3':
        if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
            await callback.message.answer("Ваш товар")
        await bot.send_invoice(chat_id=callback.from_user.id,
                                   title="2200 Wild Cores",
                                   description="Пакет на 2200 Wild Cores",
                                   provider_token=config.PAYMENTS_TOKEN,
                                   currency="rub",
                                   photo_url="550.jpeg",
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   is_flexible=False,
                                   prices=[PRICE3],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload")

    if callback.data == 'price4':
        if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
            await callback.message.answer("Ваш товар")
        await bot.send_invoice(chat_id=callback.from_user.id,
                                   title="5500 Wild Cores",
                                   description="Пакет на 5500 Wild Cores",
                                   provider_token=config.PAYMENTS_TOKEN,
                                   currency="rub",
                                   photo_url="5500.jpeg",
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   is_flexible=False,
                                   prices=[PRICE4],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload")

    if callback.data == 'price5':
        if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
            await callback.message.answer("Ваш товар")
        await bot.send_invoice(chat_id=callback.from_user.id,
                                   title="11000 Wild Cores",
                                   description="Пакет на 11000 Wild Cores",
                                   provider_token=config.PAYMENTS_TOKEN,
                                   currency="rub",
                                   photo_url="11000.jpeg",
                                   photo_width=416,
                                   photo_height=234,
                                   photo_size=416,
                                   is_flexible=False,
                                   prices=[PRICE5],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload")

    if callback.data == 'administrator':
        await callback.message.answer(
                               'Админ ВКонтакте: <a href="">https://vk.com/avekuroro</a>\n'
                               'Админ в Телеграме: @avekuroro',
                               parse_mode='html')


    await callback.answer()  # Чтобы телеграм не ждал ответа


# pre checkout  (must be answered in 10 seconds)
@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    await bot.send_message(message.chat.id,
                           f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!")


# run long-polling
executor.start_polling(dp, skip_updates=False)
