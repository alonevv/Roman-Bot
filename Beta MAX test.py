import asyncio
import logging
import random
import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '6137672948:AAGKD2Zivl1g00qOwLG8IFkZBraIqXN1_WQ'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

                                                    #КЛАВИАТУРА ОБЫЧНАЯ#


b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/info')
b4 = KeyboardButton('/Портфолио')
b5 = KeyboardButton('/Наш_сайт')
b6 = KeyboardButton('/comands')
b7 = KeyboardButton('/menu')
b8 = KeyboardButton('Антоновка')
b9 = KeyboardButton('Макс')
b10 = KeyboardButton('/Секреты_макса')
b11 = KeyboardButton('/Покормить')
b12 = KeyboardButton('Основная')
b13 = KeyboardButton('Макс1')
b14 = KeyboardButton('Отмена')
b15 = KeyboardButton('Макс2')
b16 = KeyboardButton('Далее-->')
b17 = KeyboardButton('<--Назад')
b18 = KeyboardButton('Далее-->>')
b19 = KeyboardButton('<<--Назад')
b20 = KeyboardButton('Макс лох')
b21 = KeyboardButton('Максим мамонт')
b22 = KeyboardButton('Мне скучно')
b23 = KeyboardButton('Максим мамонт')
b24 = KeyboardButton('Максим')
b25 = KeyboardButton('Максим дебил')
b80 = KeyboardButton('Шутка--1')
b81 = KeyboardButton('Шутка--2')
b82 = KeyboardButton('Шутка--3')
b83 = KeyboardButton('Шутка--4')
b84 = KeyboardButton('Шутка--5')
b85 = KeyboardButton('Шутка--6')
b86 = KeyboardButton('Шутка--7')
b87 = KeyboardButton('Шутка--8')
b88 = KeyboardButton('Шутка--9')
b89 = KeyboardButton('Шутка--Бомба')
b90 = KeyboardButton('Шутка-1')
b91 = KeyboardButton('Шутка-2')
b92 = KeyboardButton('Шутка-3')
b93 = KeyboardButton('Шутка-4')
b94 = KeyboardButton('Шутка-5')
b95 = KeyboardButton('Шутка-6')
b96 = KeyboardButton('Шутка-7')
b97 = KeyboardButton('Шутка-8')
b98 = KeyboardButton('Шутка-9')
b99 = KeyboardButton('<Назад>')
b100 = KeyboardButton('Шутка-Бомба')
b101 = KeyboardButton('Чёрный юмор')
b102 = KeyboardButton('Белый юмор')
b103 = KeyboardButton('Шутка-Бомба')
b104 = KeyboardButton('Шутки')
b105 = KeyboardButton('`Назад`')
b106 = KeyboardButton('АУФФ')
b107 = KeyboardButton('Пожиратель чокопаек')
b108 = KeyboardButton('Мамонт')
b109 = KeyboardButton('Антоновка')
b110 = KeyboardButton('Позывные Макса')
b111 = KeyboardButton('/Страхи_макса')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).row(b2,b6,b3).row(b5,b4).add(b7).add(b16)

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)

kb_menu.add(b12).row(b13,b12).add(b14)

kb_max1 = ReplyKeyboardMarkup(resize_keyboard=True)

kb_max1.add(b8,b24).row(b2,b9,b3).row(b10,b111).row(b17,b18)

kb_max2 = ReplyKeyboardMarkup(resize_keyboard=True)

kb_max2.add(b110).row(b22,b106,b104).row(b10,b111).row(b19)

kb_menushutka = ReplyKeyboardMarkup(resize_keyboard=True)

kb_menushutka.add(b101,b102).add(b105)

kb_white = ReplyKeyboardMarkup(resize_keyboard=True)

kb_white.add(b99).row(b80,b81,b82).row(b83,b84,b85).row(b86,b87,b88).add(b89)

kb_black = ReplyKeyboardMarkup(resize_keyboard=True)

kb_black.add(b99).row(b90,b91,b92).row(b93,b94,b95).row(b96,b97,b98).add(b100)

kb_pozovnue = ReplyKeyboardMarkup(resize_keyboard=True)

kb_pozovnue.add(b107).add(b109).add(b108)


                                                    #КОМАНДЫ#


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Дарова огрызки!\nЯ существую для того, тебя оскорблять! Знай, больше всего я ненавижу тех, кто играет в ПК, те сразу получают по роже костетом.\nОгрызок, как тебя звать то? #Чтобы представиться напиши "Имя: Максим', reply_markup=kb_client)


@dp.message_handler(commands=['Инфо', 'info'])
async def send_welcome(message: types.Message):
    await message.reply('Привет! \nЭтот бот посвещён Максиму Антоновке, \nкто знает тот знает! \nВ этом боте ты найдёшь много весёлого, интересного и развлекательного, \nточно незаскучаешь!!! \n\nОтдельную благодарность, \nпо разработке бота, хочу выразить \nМаргарите Сергеевне! \nЛучшая учительница по питону! \n\nТак же, хочу поблагодарить Максима, главного персанажа этого бота, \nза то что он следит за дисциплиной, \nочень весёлый, короче, с ним не заскучаешь! \n\nСоздатель бота Роман, \nесли тебе что-то непонятно, \nнапиши /help ')


@dp.message_handler(commands=['Помощь', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Привет! Нужна помощь? \n\nДля информации об этом боте, \nнапиши /info \n\nДля помощи с командами, \nнапиши /comands, либо же, \nты можешь воспользоваться клавиатурой! ')


@dp.message_handler(commands=['comands', 'команды'])
async def send_welcome(message: types.Message):
    await message.reply('Список команд нету, админу лень писать')


@dp.message_handler(commands=['Наш_сайт'])
async def send_welcome(message: types.Message):
    await message.reply('Мы бедные, нету деньга \nна хостинги =(')

@dp.message_handler(commands=['Портфолио'])
async def send_welcome(message: types.Message):
    await message.reply('Фоток нету,\nМаксим не фоткаеться =(')


@dp.message_handler(commands=['Покормить'])
async def send_welcome(message: types.Message):
    await message.reply('Ням ням ням, спасибо! \nВкусная была печенька!')


facts = ["На самом первом логотипе Apple был изображен сидящий под яблоней сэр Исаак Ньютон. Над ним нависает вот-вот готовое упасть яблоко.", "В 2009 году корпорация Google арендовала у компании California Grazing… \nкоз! \nЗачем? \nОни очень эффективны в борьбе с сорняками на разбитом вокруг штаб-квартиры «корпорации добра» газоне.", "Основатель Microsoft Билл Гейтс – недоучившийся студент, он был отчислен из Гарварда. Что, впрочем, не помешало ему создать самую популярную в мире ОС для компьютеров и одну из богатейших IT-компаний Земли.", "Слово «робот» произошло от чешского «robota» («работа»).", "Пальцы наборщика текста в среднем за день «пробегают» 20 км.", "Первый в мире будильник умел звонить только в 4 часа утра", "30 ноября каждого года отмечается Всемирный день компьютерной безопасности («Computer Security Day“)", "1 апреля 2005 года NASA поведала миру о том, что нашла воду на поверхности Марса. Троллинг удался.", "Снимок, сделанный самой первой фотокамерой в мире, пришлось бы ждать 8 часов.", "Создатели формата фото PNG хотели, чтобы его называли «пинг».", "Skype официально заблокирован в Китае.", "Компьютер Apple II получил жесткий диск объемом 5 МБ.", "Текст с экрана читается на 10% медленнее, чем с бумаги.", "По статистике, 86% людей пытаются вставить USB-кабель «вверх ногами».", "Средний возраст геймера в США – 35 лет.", "Хирурги, выросшие на видеоиграх, делают на 37% ошибок меньше.", "По данным Message Anti-Abuse Working Group, от 88 до 92% всех электронных писем, отправленных в первой половине 2010 года, являются спамом. Сегодня присутствие спама в онлайн-переписке выросло до 97%."]


@dp.message_handler(commands=['Факты'])
async def send_welcome(message: types.Message):
    await message.reply('IT факты от максима!')
    time.sleep(1)
    await message.reply('А вы знали чтооо...')
    time.sleep(2)
    await bot.send_message(message.chat.id, random.choice(facts))


@dp.message_handler(commands=['ГДЗ'])
async def send_welcome(message: types.Message):
    await message.reply('')


@dp.message_handler(commands=['menu'])
async def send_welcome(message: types.Message):
    await message.reply('Выбери вспомогательную клавиатуру \nдля удобного пользования бота! \n\nДля отмены /Отменить', reply_markup=kb_menu)


                                                #ИНЛАЙН КЛАВИАТУРА#


inkb = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text="`Секрет 1`", callback_data="bk1")).add(InlineKeyboardButton(text="`Секрет 2`", callback_data="bk2")).add(InlineKeyboardButton(text="`Секрет 3`", callback_data="bk3")).add(InlineKeyboardButton(text="`Секрет 4`", callback_data="bk4"))


@dp.message_handler(commands=['Секреты_макса'])
async def send_welcome(message: types.Message):
    await message.answer('Выбери любой секрет макса, который хочешь узнать!', reply_markup=inkb)


@dp.callback_query_handler(text="bk1")
async def bk1_call(calback: types.CallbackQuery):
    await calback.message.answer("Меня на свидание звал Жека!")
    await calback.answer()

@dp.callback_query_handler(text="bk2")
async def bk1_call(calback: types.CallbackQuery):
    await calback.message.answer("За хорошее поведение, Маргарита Сергеевна подкармливает меня чокопайками! \nЗа это я её уважаю!")
    await calback.answer()

@dp.callback_query_handler(text="bk3")
async def bk1_call(calback: types.CallbackQuery):
    await calback.message.answer("Я храню чай и овсянку в тумбочке, стаящая в хайтеке!")
    await calback.answer()

@dp.callback_query_handler(text="bk4")
async def bk1_call(calback: types.CallbackQuery):
    await calback.message.answer("У меня есть фиолетовый, пластмассовый костет!")
    await calback.answer()

inkb1 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text="`Страх 1`", callback_data="bk5")).add(InlineKeyboardButton(text="`Страх 2`", callback_data="bk6")).add(InlineKeyboardButton(text="`Страх 3`", callback_data="bk7")).add(InlineKeyboardButton(text="`Страх 4`", callback_data="bk8"))

@dp.message_handler(commands=['Страхи_макса'])
async def send_welcome(message: types.Message):
    await message.answer('Выбери любой страх Макса, который хочешь узнать!', reply_markup=inkb1)

@dp.callback_query_handler(text="bk5")
async def bk1_call(calback: types.CallbackQuery):
    await calback.message.answer("Максим очень сильно боиться сисадмина")
    await calback.answer()

@dp.callback_query_handler(text="bk6")
async def bk1_call(calback: types.CallbackQuery):
    await calback.message.answer("Максим очень боиться переделывать платы")
    await calback.answer()

@dp.callback_query_handler(text="bk7")
async def bk1_call(calback: types.CallbackQuery):
    await calback.message.answer("Максим не любит докладных")
    await calback.answer()

@dp.callback_query_handler(text="bk8")
async def bk1_call(calback: types.CallbackQuery):
    await calback.message.answer("Самый главный страх максима! \nОн боиться остаться голодным...")
    await calback.answer()




                                                             #РЕАКЦИИ#

ayf = ["Если девушка достойная, \n  она шарит в мемах!", "Тишина - тоже музыка.\n    Когда ты глухой...", "Настоящий волк идёт по жизни \n  или за майонезом \n         Или за пивом", "Красиво по жизни идёт только тот, \n    кто умеет ходить...", "Никогда не поздно, \n  никогда не рано - \nпоменять всё поздно \n    Если это рано...", "Каждый думает\n\n Но я не думаю,\n Я - не каждый, \nЯ - не шакал", "Я буду падать,\n но когда я встану,\nупадут все!", "Запомни, лучше посрать и опоздать,\n чем прийти и обосраться...", "Запомни, в жизни есть две фразы, которые помогут открыть любую дверь\n\n ~На себя~\n и  \n\n~От себя себя~", "Запомни, каждый может кинуть камень в волка,\n Но не каждый сможет кинуть волка в камень...", "Настоящий волк...\nне укусит за бочок, \n\nнастоящий волк..\nсмоет за собой толчок..."]


@dp.message_handler(regexp='(^АУФФ)')
async def cats(message: types.Message):
        await message.answer("АУФФ от Максима!")
        await asyncio.sleep(2)
        await bot.send_message(message.chat.id, random.choice(ayf))
        await asyncio.sleep(4)
        await bot.send_animation(message.chat.id,r"https://tenor.com/ru/view/ауф-auf-безумноможнобытьпервым-безумноможно-gif-18523355")


@dp.message_handler(regexp='(^Шутка--Бомба)')
async def cats(message: types.Message):
        await message.answer("Американец, немец и русский поспорили у кого в стране кинг-конги больше.\n\nАмериканец:\n— Наш кинг-конг такой большой, что он достает руками до крыши самого многоэтажного небоскреба в США.\n\nНемец:\n— Это ерунда,вот наш кинг-конг такой большой,что он достает руками в космосе две неизвестные планеты.\n\nРусский:\n— Ох и дураки же вы, эти две неизвестные планеты,яйца нашего кинг-конга.")


@dp.message_handler(regexp='(Пожиратель чокопаек)')
async def cats(message: types.Message):
        await message.answer("Всмысле?")
        await message.answer("Подумаешь, одну коропку в день у Маргариты Киприяновы съедаю...", reply_markup=kb_max2)


@dp.message_handler(regexp='(Позывные Макса)')
async def cats(message: types.Message):
        await message.answer("Выбери любую позывную максима", reply_markup=kb_pozovnue)


@dp.message_handler(regexp='(Стихи Макса)')
async def cats(message: types.Message):
        await message.answer("Выбери любую позывную максима")


@dp.message_handler(regexp='(Фото Макса)')
async def cats(message: types.Message):
        await message.answer("Выбери любую позывную максима")


@dp.message_handler(regexp='(Мамонт)')
async def cats(message: types.Message):
        await message.answer("Мамонт не тот кто большой,\nа тот кто сильнее... ", reply_markup=kb_max2)


@dp.message_handler(regexp='(^Шутка--1)')
async def cats(message: types.Message):
        await message.answer("Разбился самолет. Выжили американец, немец и русский. Поймал их вождь аборигенов и приказал:\n— Кто покажет мне кайф, того отпущу с миром, кто не покажет — тех съедим.\n\nАмериканец достал с борта самолета виски, кубинские сигары, позвал баб, вождь говорит:\n— Ну и в чем здесь кайф? Я это каждый день делаю!\nСъели американца. \n\nНемец достал с борта самолета ноутбук, показал вождю игры, суперскоростной интернет, прочие прибамбасы. Вождь говорит:\n— Ну и в чем здесь кайф? у нас шаманы и то быстрее, а игры каждый день…\nСъели немца. \n\nРусский достал с борта самолета ящик пива. Вождь выпил, спрашивает:\n— Ну и в чем здесь кайф?\nРусский:\n— Подожди, это не все!\nДостал еще два ящика пива. Вождь выпил.\n— Ну и в чем здесь кайф?\n— Да погоди ты! Будет тебе кайф!\nРусский принес еще два ящика водки, вождь выпил, говорит:\n— Да в чем же здесь кайф?\n— Ну погоди ты! Выпей еще эту маленькую бутылку минералки!\nВ вождя уже не влезает, но он какими-то усилиями выпивает. Встает, идет в кусты, ссыт и говорит:\n— Ух, каааайффф!!!")


@dp.message_handler(regexp='(^Шутка--2)')
async def cats(message: types.Message):
        await message.answer("Проходит соревнование «кто больше выпьет». \nСоревнуются русский, немец и американец. Ведущий:\n\n— Первый американец! Он будет пить виски стопками. \nОдна… две… пять… десять… \nВсё! Сломался американский спортсмен!\n\n— Второй немец! Он будет пить пиво кружками. \nОдна… две… пять… десять… пятнадцать… \nВсё! Сломался, сломался немецкий спортсмен!\n\n— Теперь русский! Он пьёт водку ковшами. \nОдин… два… пять… десять… двадцать… тридцать… \nВсё, сломался! Сломался ковш у русского спортсмена!")


@dp.message_handler(regexp='(^Шутка--3)')
async def cats(message: types.Message):
        await message.answer("Американец, немец и русский попали в ад.\n\n— Американец \n— какой здесь ужас!\n\n— Немец \n— какой здесь кошмар!\n\n— Русский \n— да, действительно хреново, но не хуже чем в нашем санатории")


@dp.message_handler(regexp='(^Шутка--4)')
async def cats(message: types.Message):
        await message.answer("— Если надо что-то сделать — зовите китайцев.\n\n— Если надо сделать что-то невозможное — зовите русских.\n\n— Если надо чтобы оно работало — зовите немцев.\n\n— А американцев?\n\n— А американцев звать не надо — они сами приходят.")


@dp.message_handler(regexp='(^Шутка--5)')
async def cats(message: types.Message):
        await message.answer("Попали на необитаемый остров: немец, американец и русский. Сделали невод, поймали золотую рыбку. \nРыбка говорит:\n— Отпустите, а я каждому по три желания исполню.\n\nНемец говорит:\n— Хочу счет в банке, Мерседес и верни меня домой.\n\nАмериканец говорит:\n— Хочу большой дом, жену верную и верни меня домой.\n\nА русский говорит:\n— Хочу ящик водки, ящик закуски и верни всех моих друзей обратно!")


@dp.message_handler(regexp='(^Шутка--6)')
async def cats(message: types.Message):
        await message.answer("Приходят к царю свататься к царевне русский, немец и американец. \nЦарь говорит им:\n— Вот вам по собаке и по мешку сухарей. Кто за месяц большему собаку научит, за того царевну и выдам.\n\nЧерез месяц приходят они снова к царю. \n\nВперед выходит тощий немец и жирная собака. \nЦарь его спрашивает:\n— Ну, чему собаку научил?\n\nНемец говорит:\n— Сидеть, лежать.\n\nВыходят англичанин и его собака, царь спрашивает:\n— Чему научил собаку?\n\nАмериканец говорит:\n— Сидеть, лежать, апорт, рядом.\n\nВыходит толстый русский и тощая собака. \nЦарь его спрашивает:\n— А ты чему научил?\n\nРусский поворачивается к собаке и говорит:\n— Рекс, голос!\n— Вань, дай сухарик, а?")


@dp.message_handler(regexp='(^Шутка--7)')
async def cats(message: types.Message):
        await message.answer("Террористы похитили работников оборонных предприятий: \nамериканца, немца и русского.\n После часовой пытки американец объяснил устройство крылатой ракеты. \nПосле двухчасовых пыток немец выдал схему новейшего истребителя. \nПосле недельных пыток русский нарисовал гайку в трех проекциях.")


@dp.message_handler(regexp='(^Шутка--8)')
async def cats(message: types.Message):
        await message.answer("Спорят американец, немец и русский, чья нация быстрее строит.\n\nАмериканец:\n— Мы начнем строить мост 1 января и 31 декабря по нему поедет первая машина.\n\nНемец:\n— А мы начнем строить больничный комплекс 1 января и 31 января уже сможем принимать первых больных.\n\nРусский:\n— Ерунда! Вот мы в понедельник в 9 утра начнем строить пивзавод и в 10 все уже пьяные.")


@dp.message_handler(regexp='(^Шутка--9)')
async def cats(message: types.Message):
        await message.answer("Захватили как-то инопланетяне троих: русского, американца и немца. \nПосадили в абсолютно пустые комнаты, дали по два титановых шарика и сказали:\n— Кто из вас завтра нас больше удивит, того и отпустим.\n\nНа завтра заходят к немцу. \n\Тот поет, шариками жонглирует.\n— Ну, удивил.\n\nЗаходят к американцу — тот поет, жонглирует и степ выбивает.\n— Ну, совсем удивил. Наверно тебя выпустим. Хотя, надо к русскому зайти.\n\nВыходят от русского и говорят:\n— Все, выпускаем его.\n— Почему?\n— Он нас капитально удивил — он один шарик сломал, а другой потерял.")


@dp.message_handler(regexp='(^Шутка-1)')
async def cats(message: types.Message):
        await message.answer("Прикинь, мужик решил покончить с собой. \nЗавязал на шее петлю, привязал веревку к дереву на утесе, выпил пузырек с ядом, прыгнул с утеса в море, и в воздухе выстрелил себе в голову из пистолета. \n— Вот это гарантия! \n— Как бы не так! \nОн выстрелом перебил веревку, упал в воду, от испуга и холода его резко затошнило и он отрыгнул весь яд, осталась одна надежда, что удасться утонуть, но какой-то катер зацепил его за одежду и вытащил из воды. \n— Ух ты! Надеюсь, после такого он идею о самоубийстве выкинул из головы? \n— Не знаю, умер он. От простуды")


@dp.message_handler(regexp='(^Шутка-2)')
async def cats(message: types.Message):
        await message.answer("Одна девочка так сильно боялась прыгать с парашютом, что прыгнула без него.")


@dp.message_handler(regexp='(^Шутка-3)')
async def cats(message: types.Message):
        await message.answer("Соседский пацан вызвал меня на бой из водяных пистолетов.\nЯ просто пишу это сообщение, пока вода в кастрюле закипает.")


@dp.message_handler(regexp='(^Шутка-4)')
async def cats(message: types.Message):
        await message.answer("Я копал яму в саду и вдруг откопал целый сундук с золотом. \nЯ уж было побежал домой, чтобы рассказать жене о ценной находке. \nПотом вспомнил, зачем я копал яму.")


@dp.message_handler(regexp='(^Шутка-5)')
async def cats(message: types.Message):
        await message.answer("Аня вышла замуж за механика и родила шестерню!")


@dp.message_handler(regexp='(^Шутка-6)')
async def cats(message: types.Message):
        await message.answer("Если вам постоянно звонят с угрозами, не отчаивайтесь. \nГлавное, что вас помнят, и вы кому-то нужны.")


@dp.message_handler(regexp='(^Шутка-7)')
async def cats(message: types.Message):
        await message.answer("— Вчера я хотел утопить все свои проблемы! \nНо жена отказалась идти купаться...")


@dp.message_handler(regexp='(^Шутка-8)')
async def cats(message: types.Message):
        await message.answer("Слепой заходит в магазин, берет собаку-поводыря и начинает раскручивать ее над головой. \n— Что вы делаете?! \n— Да так, осматриваюсь")


@dp.message_handler(regexp='(^Шутка-9)')
async def cats(message: types.Message):
        await message.answer("Мама, а почему ты говорила, что нельзя есть жёлтый снег? \n Потому что он солёный?")


@dp.message_handler(regexp='(^Шутка-Бомба)')
async def cats(message: types.Message):
        await message.answer("Купил жене разводной ключ, а она не развелась!")


@dp.message_handler(regexp='(^Чёрный юмор)')
async def cats(message: types.Message):
        await message.answer("Выберите любой анегдот, они обозначены цифрой для удобства!", reply_markup=kb_black)


@dp.message_handler(regexp='(^Белый юмор)')
async def cats(message: types.Message):
        await message.answer("Выберите любой анегдот, они обозначены цифрой для удобства!", reply_markup=kb_white)


@dp.message_handler(regexp='(^Шутки)')
async def cats(message: types.Message):
        await message.answer("Выберите какой жанр шуток вам интересен.", reply_markup=kb_menushutka)


@dp.message_handler(regexp='(^<Назад>)')
async def cats(message: types.Message):
        await message.answer("Вы вернулись к выбору!", reply_markup=kb_menushutka)


@dp.message_handler(regexp='(^`Назад`)')
async def cats(message: types.Message):
        await message.answer("Вы вернулись обратно, Макс2!", reply_markup=kb_max2)


@dp.message_handler(regexp='(^Отмена)')
async def cats(message: types.Message):
        await message.answer("Вы отменили действие", reply_markup=kb_client)


@dp.message_handler(regexp='(^Основная)')
async def cats(message: types.Message):
        await message.answer("Вы отменили действие", reply_markup=kb_client)


@dp.message_handler(regexp='Далее-->>')
async def cats(message: types.Message):
        await message.answer("Вы поменяли клавиатуру, Макс2", reply_markup=kb_max2)


@dp.message_handler(regexp='Далее-->')
async def cats(message: types.Message):
        await message.answer("Вы поменяли клавиатуру, Макс1", reply_markup=kb_max1)


@dp.message_handler(regexp='<<--Назад')
async def cats(message: types.Message):
        await message.answer("Вы поменяли клавиатуру, Макс1", reply_markup=kb_max1)


@dp.message_handler(regexp='<--Назад')
async def cats(message: types.Message):
        await message.answer("Вы поменяли клавиатуру, Основная", reply_markup=kb_client)


@dp.message_handler(regexp='(^Назад)')
async def cats(message: types.Message):
        await message.answer("Вы вернулись обратно", reply_markup=kb_max2)


@dp.message_handler(regexp='(^Макс1)')
async def cats(message: types.Message):
        await message.answer("Вы отменили действие", reply_markup=kb_max1)


@dp.message_handler(regexp='(^Макс2)')
async def cats(message: types.Message):
        await message.answer("Вы отменили действие", reply_markup=kb_max2)


@dp.message_handler(regexp='(^Антоновка)')
async def cats(message: types.Message):
    with open('max.jpg', 'rb') as photo:
            await message.reply_photo(photo, caption=f'Неназывай меня так! Ещё раз, и вилкай в ж@пy!!!', reply_markup=kb_max2)


mat = ["Сам(а) такой(ая)! Ещё раз, и костетом в глаз!", "Ты чё охренел? Тебе проблемы нужны?", "Кто обзываеться, сам так называеться!"]


@dp.message_handler(regexp='(^Максим лох|Максим даун|Максим бестолочь|Максим тварь|Максим имбицил|Максим лошара|Максим полудурок|Максим тупой|Максим мамонт|Максим дебил|Макс лох|Макс даун|Макс бестолочь|Макс тварь|Макс имбицил|Макс лошара|Макс полудурок|Макс тупой|Макс мамонт|Макс дебил)')
async def cats(message: types.Message):
    with open('max.jpg', 'rb') as photo:
        await bot.send_message(message.chat.id, random.choice(mat))

@dp.message_handler(regexp='(^Максим|Макс)')
async def cats(message: types.Message):
    with open('max.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption=f'Чо те надо, {message.from_user.first_name}')


@dp.message_handler(regexp='(^Мне скучно)')
async def cats(message: types.Message):
    with open('max.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption=f"{message.from_user.first_name}, Го побозарим? НЕТ? А я всеравно заставлю :)")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Данного сообщения я непонял! {message.from_user.first_name}, если честно, в режиме бота я немного туповат, так что вот список моих уменей! Если что в реальной жизне я очень умный.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)