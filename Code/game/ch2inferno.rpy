
define s = Character('Сосед', color="#c8ffc8")
define med = Character('Медработник', color="#f4f4f4")
init:
    $ roommatePoints = 0
    $ seenLab = False


label rootInferno:
    "— С чего бы мне помогать тебе?"
    yu "— Ты что, совсем дурной?? Нам надо вызвать военных, чтобы нас спасли!"
    yu "— Чтобы ты вступил в армию и воевал за спокойствие людей! Быстро взял в руки мультипаяльник и за работу!"

    "— А если я не хочу вам помогать? Вы ничем не лучше террористов!"
    yu "— Защищаешь этих тварей??"
    "Она замахнулась, чтобы дать мне пощечину."
    yu "— Ладно... Ты наверное ещё не осознал происходящее... А я сразу давлю на тебя..."
    "Её тон опять сменился. Но помогать ей я ни в коем случае не собирался. Она потопила корабль..."
    "Именно из-за неё я сейчас могу умереть. Тут у меня предательски заурчал живот. "
    yu "— Кушать хочешь?"
    "Юминг начала рыться в кейсах. Всё что она нашла это две бутылки воды и растаявший сырок."
    yu "— А-ха-ха-ха! Как глупо было его брать с собой на задание! Давай поделим всё пополам?"
    "Вся такая закрытая и строгая, когда говорит с обычными людьми."
    "Сейчас она смотрела на меня добродушно и дружелюбно. "
    "Но у меня она вызывала только отвращение. Её улыбка не вернёт мне мою семью."

    "— Знаешь... — Я взял в руки сломанный передатчик, осматривал его. — Думаю, я смогу справиться с этой штуковиной."

    "— Ураа, я знала, что ты сможешь."
    "В глазах этой загадочной китаянки заиграла радость. "
#    "— Посмотри в том кей..."
    play music cooper
    "Её полный энтузиазма голос заглох после звука тупого удара передатчика о её висок. "
    $ killedPeopleCount += 1
    $ inferno = True
    $ yumingAlive = False
    hide yuming onlayer forward with fade
    "Это ОНА уничтожила корабль.{w}Мы были приманкой."
    "Мы.{w} Я, Тоня и мама с папой."
    "А теперь только я." with bloodrage
    "Один.{w} И снова один."
    "Я столкнул дрожащими руками её обездвиженное тело в воду."
    "Это было довольно тяжело, так как всё моё тело болело после крушения. Да и я не был крепкого телосложения."
    # тут наверное нужен будет рисунок моря с тёмным пятном тела в глубине.

    "Я провожал взглядом расплывающийся в толще воды контур её тела... "
    "По немногу я приходил в себя. Всё тело охватила дрожь, что же я натворил? За что? Неужели я способен вот так просто убить человека?"
    "Всю свою жизнь я не причинял никому боли, даже не дрался ни с кем... А сейчас приступ слепой ярости ударил в голову, и что самое страшное, я даже не чувствую своей вины."
    hide boat onlayer middle
    scene black onlayer background with closing
    "Может, это из-за жары и изнеможения? Постепенно я отключился..."
    call flashback2
    scene bg ocean night onlayer background with opening
    show boat night onlayer middle at bottom
    $ camera_move(500, -2000, 0, 0, 0)
    $ camera_moves( ( (660, -2100, 0, 0, 2, 'ease'),(500, -2000, 0, 0, 4, 'ease') ), loop=True)
    "Проснулся я от брызг солёной воды попавших мне в лицо: в море разыгрались волны, конечно, не такие большие, чтобы представлять какую-то опасность для моей лодки..."
    "Уже наступила ночь, лишь только звёзды и луна хоть как-то освещали бесконечную водную поверхность. "
    "Вокруг не виднелось даже и намёка на берег. Я вспоминал события прошедшего дня, ужасаясь от своего поступка. В тусклом лунном свете я стал рыться в разбросанных ящиках. "
    "Должно же в них быть хоть что-то, что могло бы помочь мне выбраться? Один хлам! И вообще... Эта сумасшедшая китаянка затопила наш лайнер, но почему же я один на лодке в куче хлама? "
    "Выжили ли остальные? Боюсь, что я никогда не узнаю ответы на эти вопросы. А может, уже организовали спасательную экспедицию? Не мог же я далеко уплыть на этой лодке? Точно! "

    "— Меня точно спасут!"
    "Я нервно засмеялся, постепенно мой смех переходил в истерику. Я стал сбрасывать ящики с хламом за борт, как днём сбросил причину моего незавидного положения."

    "— Сброшу все эти странные вещи, чтобы не вызывать лишних вопросов, если меня всё таки спасут."
    "Вгляд упал на растаявший сырок. У меня всё сжалось внутри... Живой человек взял его с собой чёрт знает откуда, а я лишил этого человека жизни. "
    "У меня предательски заурчало в животе. Неужели придётся есть это?"

    "Пытаясь убедить себя, что у предметов нет памяти, если только это не запоминающее устройство, я заставил себя съесть этот сырок. "
    "На обёртке было что-то по китайски написано."

    "Оставшаяся ночь была самой кошмарной за всю мою жизнь — я остался один на один со своей совестью. {w}Хоть я и был атеистом, мне казалось, что теперь мне обязательно вернётся моё зло. "
    "И даже аргумент, что из-за Юминг погибли люди был уже не убедителен для меня. "

    play sound helicopter
    play music kiitos
    "Утром меня разбудил шум пролетающего вдали вертолёта. Он пролетал совсем далеко, и на приличной высоте, должно быть, чтобы площадь обзора была больше. "
    "В таком случае, он быстро заметит меня. Если, конечно, это действительно спасатели... Я всячески привлекал внимание, махал руками, кричал, хоть я и понимал, что это не поможет, но всё равно, я не мог спокойно сидеть на месте."
    stop sound
    "Меня и остальных выживших доставили в Испанию, власти которой и организовали спасательную операцию. {w}Около двадцати человек, в основном, россияне. "
    "Я не стал ни с кем разговаривать. Какая-то дама безостановочно рыдала, да и у других вид был не лучше."
    hide boat day onlayer middle

    scene bg bus onlayer background
    nvl clear
    nvlc "Нас везли в больницу в какой-то испанский город, названия я не запомнил, да и голова была загружена другими мыслями. Я поставил себе цель пройти тест на возможность управления тем странным оборудованием. Китаянка говорила о каком-то тесте на вирус в своей провинции..."
    nvlc "Если доберусь до интернета, то без проблем найду информацию даже в китайском сегменте, благо современными инструментами поиска я хорошо владею. "
    nvlc "А может, кто в больнице знает про эту проверку? Погруженный в свои мысли, я даже не заметил, как мы приехали. Наша больница представляла собой несколько десятков небольших корпусов, должно быть, разные отделения находились в отдельных корпусах."
    nvlc "А где тут интернет? Должны же нам дать хоть какие-то средства связи! "
    nvl clear
    scene bg hospital reg onlayer background 
    nvlc "Панический настрой улетучился, когда нас привели в корпус, где проходит регистрация. Всё было оборудовано настолько современно, насколько это возможно."
    nvlc "Под потолком летали небольшие коптеры, разносили какие-то бумаги, баночки. Наверное, они и между корпусами летают, но я не обратил внимание. "
    nvlc "Интересное решение, у себя я такого никогда не видел. Зарегистрировали нас быстро, спросили информацию о родных, чтобы сообщить им о случившемся. Я соврал, что давно с ними в ссоре. Не хватало ещё жалости с их стороны."
    nvl clear
    
    scene bg hospital room night onlayer background
    nvlc "Меня заселили в просторную двухместную палату. На соседней кровати были разбросаны рваные куски каких-то тряпок, самого же соседа в палате не было. Уже было поздно. "
    scene black onlayer background with closing
    nvlc "Стоило мне коснуться постели, как глаза сами стали закрываться и я провалился в сон. {w}Однако сильная усталось не помешала недавним событиям повториться во сне. Я сбрасывал Юминг с лодки, а потом падал вместе с ней, падал в бездну, просыпался, снова засыпал. И так несколько раз."
    nvl clear

    scene bg hospital room day onlayer background
    nvlc "На следующий день нам пообещали, что вернут в Россию так скоро, как проведут все тесты и необходимое лечение. "
    nvlc "Однако, мне повезло больше чем другим, и я не получил никаких серьёзных повреждений, даже эмоционально я казался невозмутимым на фоне остальных. "
    nvlc "Это такое свойство интроверта — все переживания происходят внутри, снаружи их заметить довольно тяжело, если не знаешь человека. "
    nvl clear
    scene bg hospital diner onlayer background
    nvlc "Завтрак был неплохим: какие-то местные фрукты и чай. {w}Я отнёс посуду и вышел из столовой. Куда теперь направиться?"
    menu:
        "Обратно в палату": 
            $ lazynessPoints += 1
            "Что-то меня совсем в сон клонит... Вздремну-ка я часок..."
            "Неспешными шагами направился в сторону своей палаты"
            "Лениво открываю дверь в палату"
            scene bg hospital room day onlayer background
            "Передо мной появляется высокий мужчина, на вид лет сорока"
            s "— Здарова, по-русски говоришь?"
            menu:
                "Да, земляк!":
                    $ roommatePoints += 1
                    "— Да, земляк. Можно пройти?"
                    s "— О-о! Я так рад. А то совсем не понимаю этих испанцев. Всю жизнь только по-русски говорю."
                    "— Даже английского не знаете?"
                    s "— Нет!"
                    "Сосед засмеялся"
                    s "– Меня привезли почти сразу после крушения, а ты, небось сутки в воде провёл? Хотя...{w} Видок у тебя здоровый"
                    "—Мне повезло попасть на лодку..."
                    s "Ах ты засранец!"
                    with vpunch
                    "Сосед засмеялся ещё громче и похлопал меня по плечу"
                    s "— А что, собственно, произошло с кораблем?"
                    "— Помню только взрывы..."
                    "Произнося это я рухнул в кровать и отключился"
                "Сейчас я хочу только спать":
                    $ lazynessPoints+=1
                    "Я пробурчал, что хочу спать и попытался обойти его, случайно задев плечом"
                    s "Хааа, ты тоже русский!"
                    "Сосед громко засмеялся. Я тем временем рухнул на кровать и притворился спящим, чтобы сосед отстал. {w}Через минуту я отключился"
                "Промолчать":
                    "Я притворился, что не понимаю его, аккуратно обошёл его и рухнул на кровать."
                "Отвали, мужик!":
                    $ agressionPoints += 1
                    $ roommatePoints -= 1
                    "— Отвали мужик! Дай пройти!"
                    "Сосед явно не ожидал такой реакции, и даже не ответил мне. "
                    "Я плюхнулся в кровать и довольный собой уснул"
                    # bulka: А с чего довольный-то? С того, что нагрубил?
                    # pomis: сделал гадость — сердцу радость
        "Прогуляться":
            scene bg hospital outdoors onlayer background
            "Интересно, в этой стране всегда такая хорошая погода? Любуясь видом из окна, решаю прогуляться"
            "Выходя из корпуса чуть не сбиваю с ног пожилого врача"
            "— Ой... Простите!"
            "Пытаюсь помочь ему встать, но он отмахивается от меня и ругается на своём языке. Хорошо, что я ни слова не понял"
            "..."
            "Я наслаждался прогулкой примерно час, ни с кем не разговаривая. Мне очень нравится это место, когда-нибудь я обязательно вернусь в Испанию"
            "Моё внимание привлёк корпус с нарисованной красной ленточкой на входе"
            "Это международный символ ВИЧ, возможно я смогу там найти информацию об этом тестировании"
            "Хотя... Так подумать. Там ведь занимаются реальной болезнью, значит и обследования там реальные."
            "Или, может, исследование на совместимость с нейроинтерфейсом уже является стандартной частью анализа?"
            "Вполне реально."
            "Пока я был в раздумьях, ноги сами меня донесли до входа. Что-ж, решено."
            $ seenLab = True
            "Я попытался открыть дверь, но она оказалась закрыта. Я постучал, но никто не среагировал. Ну и ладно..."
            scene bg hospital room sunset onlayer background
            "Я вернулся в палату и лёг в кровать"
    "Проснулся я под вечер: к соседу пришёл врач и что-то спросил по-английски, на что сосед ответил классическим русским матом."
    # bulka: Улыбнуло)
    menu:
        "Вызваться переводчиком":
            $ roommatePoints += 1
            "Я могу без проблем читать английские тексты, но вот говорить никогда хорошо не получалось.{w} С ужасным акцентом окликаю врача"
            "— Хэй, ай кан транслейт!"
            "Но его ответ я не смог разобрать. Смотрю на него и не знаю, что сказать. Он швырнул бумажку на кровать соседа и вышел из палаты"
            s "— Ха-ха-ха-хаа! Чёртовы пиндосы!"
            "Сосед заливался смехом, не обращая внимания на бумажку. {w}Я встал с кровати и поднял этот документ."
            "— Здесь говорится, что у вас всё в порядке, и вечером вас отправят в Москву."
            s "— В Москву? И что мне там делать? А-ха-ха-ха!"
            "— Они просто не знают, куда вас отправить."
            s "— Ну и ладно. У меня там есть знакомые, не пропаду.{w} Есть курить?"
            "— Нет... Не курю."
        "Продолжать наблюдать":
            $ lazynessPoints += 1
            "Я не подавал никаких признаков того, что проснулся, и наблюдал за этой сценой.{w} Забавно, сосед так искренне отвечает врачу, будто бы правда хочет что-то объяснить ему."
            "Наконец, врач ушёл, швырнув бумажку соседу на кровать."
    "Сосед потянулся за своей сумкой. {w}Стоп, как у него уцелела сумка? Везучий-то какой!"
    "Он достал небольшой серебристый ноутбук, открыл его и стал что-то смотреть"
    "— Это ваш ноутбук?"
    if roommatePoints>0:
        s "— Да, сумка была на мне во время крушения. {w}Мне крупно повезло, что она плотная, и ноут не успел промокнуть. Жаль, что документы были в чемодане..."
        s "— Если хочешь, можешь воспользоваться, вижу как ты смотришь на него."
        "— Да, мне очень нужно выйти в сеть! Спасибо."
        "Я взял его ноутбук и в первую очередь начал искать информацию об этом месте."
        "Потом стал искать информацию об исследовании на совместимость. В испанском сегменте действительно были некоторые упоминания."
        "Географически эти люди расположены в разных уголках страны и в разное время. Есть упоминание и в моём городе. Можно попробовать пройти анализ в этом госпитале, только как мне объяснить врачу необходимость этого?"
        "Ноутбук предательски запищал о низком заряде аккумулятора"
        s "— Так, а теперь я. Всю батарею мне посадил!"
        "Сосед забрал свой ноут."
        "— Зарядник тоже был в чемодане?"
        s "— А ты умён! Хах."
        "На этом я решил покинуть палату и найти врача. И как мне напроситься на анализ? Его же не проходят просто так? Понятия не имею..."
        "Может, прикинуться наркоманом? {w}Нет, бред! Тут мой взгляд привлекает плакат на посту. Судя по его содержанию, это клиника одна из ведущих в области борьбы с ВИЧ."
        "Я показываю на него пальцем и говорю проходящему мимо врачу:"
        "— Ай нид...{w}Аналайсис...{w}Вич... Эйдс... Нид ту ду аналайсис!"
        "Врач с недоверием смотрит на меня. Я говорю с ужасным акцентом и путаюсь в словах"
        "— Ай нид ту тест майселф фор эйдс!"
        "Кое как выдавил из себя более-менее осмысленную фразу."
        "Кажется, врач понял меня. Он написал что-то в своём смартфоне и вручил мне."
        "Там был открыт переводчик с испанского на русский. Удивительно, врач в Испании не знает английского."
        "«Если Вам нужно пройти ВИЧ анализ, приходите в 8 часов утра в 12 корпус. Ничего не есть.»"
        "Я переключаю переводчик в обратный режим, и пишу «Спасибо» по-русски, отдаю смартфон врачу и ухожу в свою палату."
        "Ну что же, надеюсь, получится."
        "Остаток дня я провожу в палате, общаясь с соседом о всяких глупостях."
        "Ложусь спать примерно в полночь, ставлю будильник на электронных часах в палате."
        "Утром направляюсь сдавать анализ"
        jump analysis

    # Если плохие отношения с соседом
    else:
        "— Тебе-то какое дело? Иди спи, малой."
        "Такая грубость вводит меня в ступор. Хотя, я и сам не был с ним особо вежлив. Лишь спустя несколько секунд отвечаю ему"
        menu: 
            "Да не, ничего...":
                "— Да я так, просто..."
                s "Что хитро, то и просто! Ха-ха-ха"
                "Сосед залился смехом"
                s "— Можешь воспользоваться моим ноутом... Но сначала курить найди мне, малой."
                menu:
                    "Согласиться":
                        "— Ладно... Я согласен."
                        s "— Ха-ха-ха! Жду!"
                        # фон улица
                        nvl clear
                        nvlc "И где мне искать сигареты? Денег у меня нет...{w} Наверняка, тут есть курилка. Попрошу там парочку."
                        nvlc "Я бродил по территории где-то 20 минут. Нашёл компанию курящих испанцев. Они что-то громко обсуждали и смеялись, страшновато подходить."
                        nvlc "Пересилив себя, я подошёл к ним и жестом показал, что хотел бы сигарету. На что получил облако дыма в лицо. Ну и гадкий запах! Не похоже на табачный..."
                        nvlc "К нам выбежал охранник, испанцы бросились врассыпную. {w}Я замешкался, но через секунду побежал за ними."
                        nvl clear
                        nvlc "Вроде бы пронесло.{w} Я выпросил несколько сигарет и зажигалку у растаманов и направился в свою палату озираясь по сторонам, чтобы не встретить охранника."
                        nvlc "Знакомый коридор, прохожу мимо поста."
                        nvlc "Сосед тем временем смотрел в окно. Услышав, как я зашёл, он повернулся в мою сторону."
                        nvl clear
                        scene bg hospital room sunset onlayer background
                        s "— Ну, чем обрадуешь?"
                        "Я протянул ему сигареты."
                        s "— Хорош, малой."
                        "Он взял сигареты и направился к выходу.{w} Наверное, это означает, что я могу взять его ноут."
                        "Я взял его ноутбук и в первую очередь начал искать информацию об этом месте."
                        "Потом стал искать информацию об исследовании на совместимость. В испанском сегменте действительно были некоторые упоминания."
                        "Географически эти люди расположены в разных уголках страны и в разное время. Есть упоминание и в моём городе. Можно попробовать пройти анализ в этом госпитале, только как мне объяснить врачу необходимость этого?"
                        "Ноутбук предательски запищал и разрядился."
                        "На этом я решил покинуть палату и найти врача. И как мне напроситься на анализ? Его же не проходят просто так? Понятия не имею..."
                        "Может, прикинуться наркоманом? {w}Нет, бред! Тут мой взгляд привлекает плакат на посту. Судя по его содержанию, это клиника одна из ведущих в области борьбы с ВИЧ."
                        "Я показываю на него пальцем и говорю проходящему мимо врачу:"
                        "—Ай нид...{w}Аналайсис...{w}Вич... Эйдс... Нид ту ду аналайсис!"
                        "Врач с недоверием смотрит на меня. Я говорю с ужасным акцентом и путаюсь в словах."
                        "—Ай нид ту тест майселф фор эйдс!"
                        "Кое как выдавил из себя более-менее осмысленную фразу."
                        "Кажется, врач понял меня. Он написал что-то в своём смартфоне и вручил мне."
                        "Там был открыт переводчик с испанского на русский. Удивительно, врач в Испании не знает английского."
                        "«Если Вам нужно пройти ВИЧ анализ, приходите в 8 часов утра в 12 корпус. Ничего не есть.»"
                        "Я переключаю переводчик в обратный режим, и пишу «Спасибо» по-русски, отдаю смартфон врачу и ухожу в свою палату."
                        "Ну что же, надеюсь, получится."
                        "Остаток дня я провожу в палате, общаясь с соседом о всяких глупостях."
                        "Ложусь спать примерно в полночь, ставлю будильник на электронных часах в палате."
                        "Утром направляюсь сдавать анализ."
                        jump analysis
                    "Всё-таки показать ему средний палец.":
                        jump fuckRoommate
            "Показать средний палец": 
                jump fuckRoommate

    # Конец дня

label fuckRoommate:
    # тут будет драка в которой гг отхватит леща. С некоторой вероятностью может сломать палец. Будет выслан в Россию. В конце концов итог будет тот же, что и разветвление с анализом
    $ agressionPoints += 1
    "Я чётким движением показываю средний палец своему соседу. Вся моя робость вмиг пропала."
    s "Ах ты ублюдок!"
    "Сосед схватил меня за средний палец и выворачивает его, тянет к себе"
    menu:
        "Ударить кулаком":
            "Так как он гораздо сильнее меня, единственный шанс победить — грамотный и точный удар. {w}Сейчас он тянет на себя, что придаст дополнительный испульс удару"
            "Я ударяю ему в глаз, он сразу же отпускает мой палец, хватается за лицо, я наношу ещё один удар. {w}Следом, он одним ударом отталкивает меня на пару метров."
            "Я падаю на пол, а в комнату забегает медработник."
            "Он что-то кричит на своём языке, я тем временем встаю и ухожу из комнаты."
            "Медработник не мешает мне выйти."
            "Я вышел на улицу, гулял в одиночестве до самого вечера."
            "Когда вернулся в палату, сосед уже собирался уезжать. У него откуда-то появился целый пакет вещей."
            "Я старался не пересекаться с ним взглядом, просто лёг на кровать."
            jump nextDay
        "Пытаться освободить палец":
            "Свободной рукой я пытаюсь освободиться, но сосед гораздо сильнее меня. "
            menu:
                "Плюнуть соседу в лицо":
                    $ brokenFinger = True
                    "Я чувствую, как хрустят кости в пальце. Я изо всех сил зову на помощь."
                "Закричать":
                    "Я изо всех сил зову на помощь" 
        "Закричать": 
            "Я изо всех сил зову на помощь"
    "Сосед тут же отпускает меня, отворачивается и делает вид, что не при чём. В палату забегает медработник, смотрит на меня."
    "Мы смотрим друг на друга секунды две, он разворачивается и уходит."
    s "— Ладно, живи."
    "— Живее тебя буду!"
    "Сосед усмехнулся."
    s "— Смельчак, да? А ну пошёл вон из моей палаты!"
    "— Это не твоя па..."
    s "— Молчать, щегол!"
    if brokenFinger == True:
        s "— Ещё что-нибудь сломать?"
    "Я не нашёл чего ответить и просто лёг на кровать."
    s "Ну и хрен с тобой."
    "Ну что за урод этот сосед? Хотя, я и сам был не особо вежлив с ним."
    "Может...{w} Его тоже убить?"
    menu:
        "Да":
            $ killedPeopleCount += 1
            "Помнится, тут была тележка с лекарствами..."
            jump killing
        "Нет":
            "Нет! Он обычный человек и не виноват в смертях моих близких!"
    # bulka: СМЕЕЕЕЕЕЕЕЕЕЕЕЕРТЬ. Надо тут проработать. За убийство дать ещё пойнтов агрессии. Или что там в третьей главе будет даваться вместо шпионства? Того самого короч.
    "Но он сволочь."
    # bulka: Мы же злые. Слабенькое оправдание.
    "Может подставить его?"
    menu:
        "Да":
            $ spyPoints += 1
            "Помнится, тут была тележка с лекарствами..."
            call kidding
        "Нет":
            "Да ну к чёрту это вредительство, надо сконцентрироваться на своих проблемах."
    # bulka: МЕЕЕЕЕЕЕЕЕЕЕЕЕЕСТЬ. Это будет выбор из трёх вариантов. За подставу очки шпионства дать.
    # pomis: чёт я хз какие варианты сделать
    # TODO: сделать три варианта
    # bulka: Можно сделать выбор сейчас, а после предоставить возможность исполнить один из вариантов в зависимости от выбора.
    # bulka: Какую-то чушь написал, но тут надо будет что-то сделать.
    # pomis: нунах. 
    "Верно."
    if brokenFinger == True:
        "Надо бы показать палец врачу..."
        "Я не могу заставить встать себя с кровати, я даже не хочу шевелиться, чтобы не привлекать внимание соседа"
        "Точно.{w} Вот уйдёт.{w} Сразу к врачу."
        "..."
        "Я так никуда и не пошёл. Под вечер я уснул"
    else:
        "Мысли отомстить соседу долго пытались захватить взять верх, пока я не уснул"
    "..."
    jump nextDay

label killing:
    ""

label nextDay:
    scene bg hospital room night
    "Проснулся ранним утром. Солнце ещё даже не озарило палату своим светом. Соседа не было."
    "Должно быть, уехал."
    "Ну и славно!"
    "А что мне делать? Почему меня не отправили домой?"
    "Сейчас всё равно слишком рано, посплю ещё немного..."
    "..."
    "Утро было самым обычным. Насладился местной кухней, прогулялся по территории."
    if brokenFinger == True:
        "Я показал сломанный палец врачу, на что мне ответили, что ничего страшного нет."
        "Заживёт через неделю. Даже гипс не нужен.{w} Но палец всё равно болит."
        "Замотали пластырем и всё."
    "Днём я получил бумагу, что вечером меня отправят в Москву. Почему они не могли это сделать вчера?"
    "У меня нет никаких средств к существованию, и даже ключей от дома. Будет проблемно..."
    if seenLab:
        "Хм, я же видел тут какой-то корпус для борьбы с ВИЧ, может я смогу там пройти анализ сейчас?"
        "Быстрым шагом я направился к этому корпусу."
        "Стучусь"
        "На этот раз мне открывают дверь. Передо мной человек в химзащите. Что-ж, класс!"
        "Я пытаюсь объяснить, что мне нужно пройти анализ."
        "Человек в химзащите провожает меня в кабинет"
        jump analysis
    else:
        # Случай, если никаким образом не выходишь на анализ в госпитале
        # Потом можно будет сделать тут путешествие в Москву, но пока оставляю так, что в этой главе единый выход
        "Пока я в раздумьях, ноги сами ведут меня на улицу."
        "Моё внимание привлёк корпус с нарисованной красной ленточкой на входе"
        "Это международный символ ВИЧ, возможно я смогу там найти информацию об этом тестировании"
        "Хотя... Так подумать. Там ведь занимаются реальной болезнью, значит и обследования там реальные."
        "Или, может, исследование на совместимость с нейроинтерфейсом уже является стандартной частью анализа?"
        "Вполне реально."
        "Уверенным шагом я подхожу ко входу."
        "Стучусь."
        "На этот раз мне открывают дверь. Передо мной человек в химзащите. Что-ж, класс!"
        "Я пытаюсь объяснить, что мне нужно пройти анализ."
        "Человек в химзащите провожает меня в кабинет."

        jump analysis

label analysis:
    med "— Присаживайтесь."
    "Он говорил с ужасным акцентом, но хотя бы понятно..."
    med "— Левую."
    "Я протянул левую руку. Медработник воткнул в вену шприц и наполнил внушительных размеров склянку моей кровью."
    "Завершив все медицинские процедуры меня выпроводили из кабинета, сказав, что результат будет вечером."
    "И что мне делать всё это время?{w} Пойду прогуляюсь."
    "..."
    "Спустя два часа над госпиталем стали слышны звуки приближающихся вертолётов."
    "Надеюсь, это за мной! Пойду в свою палату, так им легче будет меня найти."
    "Не забыть бы сыграть удивление... А то будет немного странно."
    "От нетерпения меня начинает трясти."
    "..."
    scene bg hospital room day
    $ camera_reset()
    $layer_move("middle", 1486, duration=0)
    show gantz serious onlayer middle:
        xpos 0.27 ypos 1.06 xanchor 0.64 yanchor 1.0 
    $camera_move(-724, -471, 192, 0, duration=1)
    "В мою палату заходит здоровенный мужик в необычном костюме."
    gen "— Доброго дня. {w}Я генерал Ганц.{w} У меня к тебе дело."
    "Он говорит очень чётко и уверенно. Сразу видно, умеет управлять людьми."
    "— Что случилось? Когда я попаду в Москву?"
    gen "— Прошу следовать за мной."
    "Встаю с кровати, направляюсь за генералом."
    "Рефлекторно окидываю комнату взглядом, будто бы проверяя, что ничего не забыл, но потом вспоминаю, что никаких вещей-то у меня и нет."
    "Мы садимся в чёрный вертолёт. Снаружи выглядит как российский Ка-60. Но начинка очень необычна. Я никогда подобного не видел."
    hide gantz onlayer middle
    scene bg helic
    # bulka: В солдатском руте фигурирует Ка-60. Хз, мб у них внешность одинаковая, но так — к сведнию. 
    # pomis: Я ошибочно думал, что в реале не существует Ка-60 и хотел сделать его модифицированной нейронтами версией Ка-52, тогда как сам Ка-52 это общеизвестный и раскрученный вертолёт. В общем, заменил названия.
    # Теперь Ка-70 — никому не известный вертолёт с нейронтами, Ка-60 — распиаренный российский вертолёт

    "В кабине пилота даже нет привычных элементов управления."
    show gantz serious onlayer master:
        xpos 0.83 ypos 1.34 xanchor 1.0 yanchor 1.0 zoom 1.42 
    gen "— Итак.{w} В твоей крови были обнаружено редкое сочетание веществ, присущее только людям с открытой нервной системой."
    "— О чём это вы?"
    gen "— Дотронься до этого прибора."
    "Он протягивает мне некое подобие рации, которой я ударил китаянку. Я взял эту рацию и изобразил остолбенение."
    "— Н-невероятно! Что это?" 
    gen "— Твоя нервная система открыта к модификациям, и ты можешь управлять самым современным оружием. Ты нам нужен в боевых рядах."
    gen "— Человечество стоит на грани катастрофы. Мы столкнулись с невиданной ранее угрозой. Твари, называющие себя «Инферно» разрушают наши города."
    "— Извините, я впервые об этом слышу..."
    gen "— Ну ещё бы. Это не придаётся широкой огласке. Видел по новостям случай с Канарскими островами?"
    "— Ну... Вулкан был какой-то..."
    gen "— Нет. Его разрушили силы Инферно. Я покажу тебе видеозаписи с камер наблюдения"
    "Он что, правда думает, что в XXI веке можно кого-то убедить видеозаписью? Ну ладно, подыграю..."
    "Генерал достаёт из сумки ноутбук и включает запись с рабочего стола. Должно быть, часто приходится показывать."
    "На видеозаписи существа, ростом с девятиэтажку, покрытые лавой, перемещаясь с невероятной скоростью разрушают всё на своём пути."
    gen "— Ну раз ты посмотрел... Теперь ты знаешь военную тайну, у тебя нет выбора."
    "Тоже мне, военная тайна."
    "— Что это за монстры?"
    gen "— Мы не знаем всего об их природе. Но мы знаем, как с ними бороться. На нашей стороне лучшие учёные со всего мира и финансирование сильнейших держав."
    gen "— Ты готов сражаться?"
    "— Да."
    "Конечно. Но я не говорил на чьей стороне..."
    hide gantz onlayer middle
    "В эту же минуту вертолёт взлетел. Пилот управлял им не прикладывая никаких усилий. Ну, или так выглядело со стороны. Он просто положил одну руку на круглое устройство на панели управления и весело разговаривал с другим солдатом."
    "Наш вертолёт сопровождали два таких же. Зачем?"
    "Постепенно мы набрали огромную скорость. Не уверен, что обычные вертолёты вообще способны преодолеть скорость звука. Но через полтора часа мы уже были в Японском море."
    jump warBase










label kidding:
    return





