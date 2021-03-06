label ch5enlil_day1:
    "Утро. Реактор постепенно запускается на полную мощность заливая столицу ярким светом.{w} Сегодня такой важный день! Надо бы не забыть ничего... Передатчик, бумажка Алилума... Может, нужно что-то, что пригодится в земном обществе?"
    "Точно, заберу с работы что-нибудь!"
    scene bg inferno lab with dissolve
    "Может, взять с собой ящик-разогревашку? Ах, он же сломан... И тяжёлый.{w} Не зна-а-аю!"
    "Надоедливая коллега" "— О, привет. Опять до ночи сидела?"
    "— А?{w} что?"
    "Надоедливая коллега" "— Да не... Чего в облаках витаешь?"
    "— Что с собой взять на поверхность?"
    "Мой вопрос явно застал её врасплох."
    "Надоедливая коллега" "— Ну... Я бы взяла удлинитель! Там все люди зависят от электричества. Приборы не смогут работать, если отойти далеко от стен. А с удлинителем можно будет. Наверное."
    "— Да, ты права, возьму удлинитель, спасибо!"
    $ hasExtensionCord = True
    # bulka: Хз зачем эта переменная. Выбора же нет.
    "Надоедливая коллега" "— Ты что, серьёзно на поверхность?{w} Кто вообще тебя туда пустит?"
    menu:
        # Будет какой-то поинт, но пока хз
        "— Пустят. У меня пропуск.":
            "Я показала ей пропуск."
            "Надоедливая коллега" "— Да как так? Почему именно тебе его дали? Из всех нас ты наихудший вариант!"
        "— Просто я лучше тебя.":
            $ enlilRude += 1
            "Надоедливая коллега" "— Да ты бестолочь! Ненавижу тебя!"
    "Но я уже не слушала её, а направлялась на выход с удлинителем."
    "Так... Куда там двигаться?{w} На пропуске написано, что в Ниппур. Ладно. Проеду к порталу через Дворцовую башню."
    "Я спустилась на несколько десятков этажей вниз к транспортному тоннелю, села в вагон."
    "На удивление пусто. Обычно в это время такие толпы..."
    "Я не выпускала пропуск из рук. Не верится, что я наконец-то попаду на поверхность!"
    # сцена — вагон
    "Объявление" "— Дворцовая башня."
    "Приехали... Дальше пешком дойду."
    "Проходя мимо колонн моё внимание привлёк экран."
    "— Это же людская технология! Как он здесь оказался!"
    "прохожий" "— Королевская семья привезла с поверхности несколько таких. Даже не знаю, зачем нам это. Хотя, они наши технологии тоже воруют."
    "— Какие?"
    "прохожий" "— Нейронты, на которых построены все наши достижения науки. Они используют их, чтобы убивать нас."
    "прохожий" "— Они хоть понимают, что их организм не приспособлен к этому? Самоубийцы."
    es "— ...и только объединившись, мы сможем выжить."
    # bulka: Имхо, так выглядит естественнее 
    "— Ого, это же принцесса Эсхалия! В экране. Круто! Она всегда была за мир с людьми."
    "прохожий" "— Тьфу, бред! Они нас убивают, а эта аристократка хочет объединиться!"
    "Я вошла в здание межгородского портала. С каждой минутой я начинаю волноваться всё сильнее."
    "Работник портала" "— Куда вам?"
    # TODO: описание портала, да и города вообще
    $ result = renpy.imagemap("images/bg/pacific.jpg", "images/bg/pacific-hover.jpg", [(375, 333, 540, 497, "nippur")], focus="imagemap")
    jump nippur



# 
# 
# 
label nippur:
    "Давно я не перемещалась между городами. Ощущение, как будто тебя расплавили и снова собрали. Хотя, примерно это вроде и происходит. "
    # pomis: Совсем не хочется вводить новых персонажей, но и повествование без диалогов будет скучным.
    # pomis: Всё что написано ниже подлежит переделыванию. 
    "Этот город совсем не похож на столицу. Я вижу только одну жилую башню. Остальное — какие-то огромные установки, резервуары. И туннельный транспорт всего лишь одноуровневый.{w} И народу вокруг совсем мало. Не хотела бы я тут жить."
    "Так, а куда мне, собственно, идти? На пропуске не написано!"
    menu:
        "В здание межгородского портала.":
            $ enlilSpy += 1
            "Ну, наверное, это логично."
            "Я показала пропуск охраннику, он сказал, в какую сторону нужно идти."
            "Так, вроде тот самый кабинет. Закрыто.{w} Тук-тук."
            "Тишина. Отстой. Может, отошёл куда? Осмотрюсь пока."
            "Моё внимание привлёк плакат с инструкциями по посещению поверхности."
            nvl clear
            nvlc "*ЧЕГО НЕ СЛЕДУЕТ ДЕЛАТЬ В ОБЩЕСТВЕ ЛЮДЕЙ*"
            nvlc "Не говорите, кто вы на самом деле. Они всё равно не поверят. А ещё таким образом вы можете привлечь внимание спецслужб. Не убивайте людей без острой необходимости или должного прикрытия. Если вы планируете оставаться на поверхности долгое время, они вас вычислят по таким зацепкам, которых вы даже представить не можете. Не демонстрируйте никому достижения науки Инферно... "
            "Моё чтение прервал парниша в форме работника портала."
            port "— Ты на поверхность?"
            "— Д-да. На поверхность."
            "Как же неожиданно-то! Аж дыхание перехватило."
            port "— Ну, заходи."

            jump earth
        "На транспортную станцию":
            "Никого нет.{w} Я развернулась и пошла обратно. Не поеду же наугад?"
            "Или всё-таки кто-то есть?"
            "Паренёк в форме работника портала, сжигал скрученную бумагу и вдыхал дым."
            "Выглядит немного старше меня."
            "— Эй, что ты такое делаешь?"
            port "— А?{w} Одна из немногих привычек, оставшихся после года на поверхности."
            "— Ого, что ты там так долго делал?"
            port "— Семье по работе нужно было туда. Не оставаться же мне здесь. Другой вопрос, что ты тут делаешь?"
            port "— Да ещё из Уммы. В этот город просто так не перемещаются, тем более из столицы."
            menu:
                "— Тебе-то какое дело?":
                    $ enlilRude += 1
                    port "— Ну как это, какое. Может помочь смогу."

                "— Тоже по работе.":
                    $ portPoints += 1

            "Он выбросил свой догарающий свёрток и придавил его ботинком."
            port "— Так, ладно, мне надо идти на мою тупую и скучную работу. Ждать, что ко мне кто-то придёт, чтобы переместиться на поверхность. А приходят раз в неделю. Да и чаще портал не сможет, наверное."
            port "— Всё таки, это не твердопородистое соединение, как между нашими городами, через которое легко переносить сущность."
            "— Вот вообще не понимаю тебя."
            port "— Ну и ладно. Пойду."
            "— А я как раз тот посетитель, которого ты ждал."
            port "— Вот как. Я уж думал, сегодня опять со скуки выть начну. Следуй за мной."
            "Мы поднялись в его кабинет."
            jump earth

    # pomis: Всё что написано выше до надписи "Всё что написано ниже подлежит переделыванию." подлежит переделыванию. 
    # pomis: нет, срочно нужно ввести ещё кого-то в Инферно, а то пустыня какая-то 

label earth:
    # смена сцены
    "Портальщик внимательно изучил пропуск."
    port "— Та-а-ак. Вас, значит, перебросить поближе к городу [cityName]?"
    # bulka: А как же великий Глубошахтинск? 
    # pomis: Можно и его. В любом случае, через переменную менять будет проще.
    "— Да-да! Вы что-нибудь знаете про это место?"
    port "— Ни разу не слышал. Я только в Токио был. Не нравится мне поверхность. То жарко, то холодно, да и столько сил надо тратить, чтобы не раскрыть себя. Жуть просто. "
    "— А как не раскрыть себя? У меня очень важное задание!"
    port "— Не показывай свои глаза. У нас они по-другому устроены и сразу же выдают нас."
    # bulka: Тут она наверное спросит, а ей ответят про линзы, очки и тд.
    # pomis: думал просто про очки, но линзы тоже збс вариант.
    "— С закрытыми глазами ходить?"
    port "— Да нет же. Возьмёшь там себе очки или линзы, которые скроют зрачки, да и всё."
    "— И где их взять?"
    port "— Да откуда я знаю, разберёшься. Тебя вообще инструктировали? Кто тебя отправил на задание?"
    # bulka: Я каждый раз фейспалмами себе лицо пробиваю от этого диалога...
    "— Вроде бы его звали Алилум."
    port "— Слишком распространённое имя. Не очень информативно."
    "— Я больше ничего не знаю о нём... А что за работа была у твоей семьи на поверхности?"
    port "— Проводили исследования по управлению человеческим сознанием. Но пришлось свернуть деятельность в Токио из-за огромной ресурсоёмкости проекта и почти полного отсутствия прогресса."
    port "— Только куче людей испортили жизнь..."
    port "— Проект не заброшен. Но опыты на людях пока что оставили. Слишком много внимания это привлекает."
    "— Зачем это вообще нам нужно? Не понимаю."
    port "— Сейчас мы можем получить контроль над сознанием с вероятностью примерно 10\%. Иначе, жертва умирает."
    # bulka: Зачем тут палочка? Или миссклик?
    # pomis: экранирование вроде называется. Для ввода зарезервированных символов. Типо кавычка это \", слэши \\ \/, перенос строки \n или \n\r, итд. В ренпае (или питоне) процент тоже зарезервирован для чего-то. Без палочки не запустится
    "— Кошмарно..."
    port "— Ладно, проехали."
    if portPoints>0:
        port "— Что ты берёшь с собой на поверхность?"
        "Я гордо протягиваю ему удлинитель."
        port "— Безусловно, самая необходимая вещь на поверхности. Деньги возьми лучше.{w} Так, у меня есть немного, всё равно они мне уже не пригодятся, возьми."
        "Парниша вручил мне несколько бумаг."
        $ yenBalance += 1200
        port "— Это иены. Не думаю, что они будут действовать в той стране, куда ты собираешься, но хотя бы обменяешь на что-то другое. Лучше, чем ничего."
        "— Ой, точно, я читала, что они очень важны. Совсем забыла!"
        # Пока хз какая альтернатива у Инферно.
        port "— У них всё построено на этом. Ты не сможешь даже поесть без денег. А кушать там придётся часто, у них нет глобальных излучателей энергии."
    port "— Что за работа у тебя на поверхности?"
    "— Следить за каким-то человеком."
    port "— Шпионская миссия, а тебя даже не снабдили самым необходимым. И даже не объяснили, кто объект твоей слежки."
    # bulka: А если подумать, то реально как-то глупо. Да и то, что она изучив два языка и столько наших технологий не знает про деньги, немножко странно.
    port "— Ладно, давай спускайся в портал. Через 5 минут отправлю тебя на поверхность."
    # смена сцены
    "До сих пор не верится, что попаду туда..."
    # сцена — вид на небольшой российский городок, примерно 20К населения, вечер, погода +7, сильный ливень
    "— Так, и где это я? Почему на меня льётся вода!!!{w} ХОЛОДНО!!!"
    "БЕЖАТЬ К ЗДАНИЯМ!"
    "Куда можно зайти? ГДЕ ЗДЕСЬ ГЕОТЕРМАЛЬНЫЙ РЕАКТОР?{w} КАК ВООБЩЕ МОЖЕТ БЫТЬ ТАК ХОЛОДНО!?"
    "прохожий" "— Эй, дура, чего полуголая носишься?{w} А-ха-ха! Зачем тебе удлинитель? Что у тебя с глазами? "
    "прохожий2" "— Кто ты вообще? Ты с какой планеты, девочка?"
    "Я развернулась и побежала как можно дальше от этих злых людей."
    "прохожий" "— Куда на красный прёшься, поехавшая!"
    # bulka: In soviet russia language learns you! В голос с "поехавшая")
    "Меня чуть не сбивает колёсный транспорт. Кажется, я уже видела такой где-то. Да что не так с этим местом?"
    "Где укрыться?{w} Забегаю в первую попавшуюся открытую дверь. Забиваюсь в угол. Обессиленная отключаюсь."
    scene black with closing
    jump ch5enlil_day2