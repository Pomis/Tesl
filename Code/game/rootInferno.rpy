image bg night ocean = "images/sky-ocean-night.jpg"
image bg black = "images/black.jpg"
image boat night = "images/boat-night.png"
define s = Character('Сосед', color="#c8ffc8")
init:
    $ roommatePoints = 0
    $ seenLab = False
label rootInferno:
    "Юминг посмотрела на меня испепеляющим взглядом."
    yu "—Ты что, совсем дурной?? Чтобы вызвать военных, чтобы нас спасли!"
    yu "—Чтобы ты вступил в армию и воевал за спокойствие людей! Быстро взял в руки мультипаяльник и за работу!"

    "—А если я не хочу вам помогать? Вы уничтожили их город, теперь расплачивайтесь!"

    "—Защищаешь этих тварей??"
    "Она замахнулась, чтобы дать мне пощечину."
    yu "— Ладно... Ты наверное ещё не осознал происходящее... А я сразу давлю на тебя..."
    "Её тон опять сменился. Поразительно, как быстро меняется настроение у этой девушки. Но помогать ей я ни в коем случае не собирался. Она потопила корабль..."
    "Именно из-за неё я сейчас могу умереть. Тут у меня предательски заурчал живот. "
    yu "—Кушать хочешь?"
    "Юминг начала рыться в кейсах. Всё что она нашла это две бутылки воды и растаявший сырок."
    yu "— А-ха-ха-ха! Как глупо было его брать с собой на задание! Давай поделим всё пополам?"
    "Она смотрела на меня добродушно и дружелюбно. "
    "Но сейчас она вызывала у меня только отвращение. Её улыбка не вернёт меня на корабль, и уж тем более, домой."

    "—Знаешь... — Я взял в руки сломанный передатчик, осматривал его. — Думаю, я смогу справиться с этой штуковиной."

    "—Ураа, я знала, что ты сможешь."
    "В глазах этой загадочной китаянки заиграла радость. "
    "— Посмотри в том кей..."
    play music "music/Alasdair_Cooper_-_06_-_2044.mp3"
    "Её полный энтузиазма голос заглох после звука тупого удара передатчика о её висок. Я столкнул дрожащими руками её обездвиженное тело в воду. "
    "Это было довольно тяжело, так как её костюм на половину состоял из металлических деталей, однако, благодаря этому, она сразу пошла ко дну."
    hide yuming onlayer forward with fade

    "Я провожал взглядом расплывающийся в толще воды контур её тела... "
    "По немногу я приходил в себя. Всё тело охватила дрожь, что же я натворил? За что? Неужели я способен вот так просто убить человека?"
    "Всю свою жизнь я не причинял никому боли, даже не дрался ни с кем... А сейчас приступ слепой ярости ударил в голову, и что самое страшное, я даже не чувствую своей вины."
    hide boat onlayer middle
    scene bg black onlayer background with fade
    "Может, это из-за жары и изнеможения? Постепенно я отключился..."

    scene bg night ocean onlayer background
    show boat night onlayer middle at bottom
    $ camera_move(500, -2000, 0, 0, 0)
    $ camera_moves( ( (660, -2100, 0, 0, 2, 'ease'),(500, -2000, 0, 0, 4, 'ease') ), loop=True)
    "Проснулся я от брызг солёной воды попавших мне в лицо: в море разыгрались волны, конечно, не такие большие, чтобы представлять какую-то опасность для моей лодки..."
    "Уже наступила ночь, лишь только звёзды и луна хоть как-то освещали бесконечную водную поверхность. "
    "Вокруг не виднелось даже и намёка на берег. Я вспоминал события прошедшего дня, ужасаясь от своего поступка. В тусклом лунном свете я стал рыться в разбросанных ящиках. "
    "Должно же в них быть хоть что-то, что могло бы помочь мне выбраться? Один хлам! И вообще... Эта сумасшедшая китаянка затопила наш лайнер, но почему же я один на лодке в куче хлама? "
    "Выжили ли остальные? Боюсь, что я никогда не узнаю ответы на эти вопросы. А может, уже организовали спасательную экспедицию? Не мог же я далеко уплыть на этой лодке? Точно! "

    "—Меня точно спасут!"
    "Я нервно засмеялся, постепенно мой смех переходил в истерику. Я стал сбрасывать ящики с хламом за борт, как днём сбросил причину моего незавидного положения."

    "—Сброшу все эти странные вещи, чтобы не вызывать лишних вопросов, если меня всё таки спасут."
    "Вгляд упал на растаявший сырок. У меня всё сжалось внутри... Живой человек взял его с собой чёрт знает откуда, а я лишил этого человека жизни. "
    "У меня предательски заурчало в животе. Неужели придётся есть это?"

    "Пытаясь убедить себя, что у предметов нет памяти, если только это не запоминающее устройство, я заставил себя съесть этот сырок. "
    "На обёртке было что-то по китайски написано."

    "Оставшаяся ночь была самой кошмарной за всю мою жизнь — я остался один на один со своей совестью. {w}Хоть я и был атеистом, мне казалось, что теперь мне обязательно вернётся моё зло. "
    "И даже аргумент, что из-за Юминг погибли люди был уже не убедителен для меня. "

    play music "music/258007__dallasbass__helicopter-in-mountains.wav"
    "Утром меня разбудил шум пролетающего вдали вертолёта. Он пролетал совсем далеко, и на приличной высоте, должно быть, чтобы площадь обзора была больше. "
    "В таком случае, он быстро заметит меня. Если, конечно, это действительно спасатели... Я всячески привлекал внимание, махал руками, кричал, хоть я и понимал, что это не поможет, но всё равно, я не мог спокойно сидеть на месте."
    play music "music/Janneh_-_06_-_Kiitos.mp3"
    "Меня и остальных выживших доставили в Испанию, власти которой и организовали спасательную операцию. {w}Около двадцати человек, в основном, россияне. "
    "Я не стал ни с кем разговаривать. Какая-то дама безостановочно рыдала, да и у других вид был не лучше."

    "Нас везли в больницу в какой-то испанский город, названия я не запомнил, да и голова была загружена другими мыслями. "
    "Я поставил себе цель пройти тест на возможность управления тем странным оборудованием. Китаянка говорила о каком-то тесте на вирус в своей провинции..."
    "Если доберусь до интернета, то без проблем найду информацию даже в китайском сегменте, благо современными инструментами поиска я хорошо владею. "
    "А может, кто в больнице знает про эту проверку? Погруженный в свои мысли, я даже не заметил, как мы приехали. Наша больница представляла собой несколько десятков небольших корпусов, должно быть, разные отделения находились в отдельных корпусах."
    "А где тут интернет? Должны же нам дать хоть какие-то средства связи! "

    "Панический настрой улетучился, когда нас привели в корпус, где проходит регистрация. Всё было оборудовано настолько современно, насколько это возможно."
    "Под потолком летали небольшие коптеры, разносили какие-то бумаги, баночки. Наверное, они и между корпусами летают, но я не обратил внимание. "
    "Интересное решение, у себя я такого никогда не видел. Зарегистрировали нас быстро, спросили информацию о родных, чтобы сообщить им о случившемся. Я соврал, что давно с ними в ссоре, и не хочу их тревожить. "

    "Меня заселили в просторную двухместную палату. На соседней кровати были разбросаны рваные куски каких-то тряпок, самого же соседа в палате не было. Уже было поздно. "
    "Стоило мне коснуться постели, как глаза сами стали закрываться и я провалился в сон. {w}Однако сильная усталось не помешала недавним событиям повториться во сне. Я сбрасывал Юминг с лодки, а потом падал вместе с ней, падал в бездну, просыпался, снова засыпал. И так несколько раз."

    "На следующий день нам пообещали, что вернут в Россию так скоро, как проведут все тесты и необходимое лечение. "
    "Однако, мне повезло больше чем другим, и я не получил никаких серьёзных повреждений, даже эмоционально я казался невозмутимым на фоне остальных. "
    "Это такое свойство интроверта — все переживания происходят внутри, снаружи их заметить довольно тяжело, если не знаешь человека. "
    "..."
    "Завтрак был неплохим: какие-то местные фрукты и чай. {w}Я отнёс посуду и вышел из столовой. Куда теперь направиться?"
    menu:
        "Обратно в палату": 
            $ lazynessPoints += 1
            "Что-то меня совсем в сон клонит... Вздремну-ка я часок..."
            "Неспешными шагами направился в сторону своей палаты"
            "Лениво открываю дверь в палату"
            "Передо мной появляется высокий мужчина, на вид лет сорока"
            s "—Здарова, по-русски говоришь?"
            menu:
                "Да, земляк!":
                    $ roommatePoints += 1
                    "—Да, земляк. Можно пройти?"
                    s "—О-о! Я так рад. А то совсем не понимаю этих испанцев. Всю жизнь только по-русски говорю."
                    "—Даже английского не знаете?"
                    s "—Нет!"
                    "Сосед засмеялся"
                    s "–Меня привезли почти сразу после крушения, а ты, небось сутки в воде провёл? Хотя...{w} Видок у тебя здоровый"
                    "—Мне повезло попасть на лодку..."
                    s "Ах ты засранец!"
                    with vpunch
                    "Сосед засмеялся ещё громче и похлопал меня по плечу"
                    s "—А что, собственно, произошло с кораблем?"
                    "—Помню только взрывы..."
                    "Произнося это я рухнул в кровать и отключился"
                "Сейчас я хочу только спать":
                    "Я пробурчал, что хочу спать и попытался обойти его, случайно задев плечом"
                    s "Хааа, ты тоже русский!"
                    "Сосед громко засмеялся. Я тем временем рухнул на кровать и притворился спящим, чтобы сосед отстал. {w}Через минуту я отключился"
                "Промолчать":
                    "Я притворился, что не понимаю его, аккуратно обошёл его и рухнул на кровать."
                "Отвали, мужик!":
                    $ agressionPoints += 1
                    $ roommatePoints -= 1
                    "—Отвали мужик! Дай пройти!"
                    "Сосед явно не ожидал такого ответа, и даже не ответил мне. "
                    "Я плюхнулся в кровать и довольный собой уснул"
        "Прогуляться":
            "Интересно, в этой стране всегда такая хорошая погода? Любуясь видом из окна, решаю прогуляться"
            "Выходя из корпуса чуть не сбиваю с ног пожилого врача"
            "—Ой... Простите!"
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
            "Я вернулся в палату и лёг в кровать"
    "Проснулся я под вечер: к соседу пришёл врач и что-то спросил по-английски, на что сосед ответил классическим русским матом"
    menu:
        "Вызваться переводчиком":
            $ roommatePoints += 1
            "Я могу без проблем читать английские тексты, но вот говорить никогда хорошо не получалось.{w} С ужасным акцентом окликаю врача"
            "—Хэй, ай кан транслейт!"
            "Но его ответ я не смог разобрать. Смотрю на него и не знаю, что сказать. Он швырнул бумажку на кровать соседа и вышел из палаты"
            s "Ха-ха-ха-хаа! Чёртовы пиндосы!"
            "Сосед заливался смехом, не обращая внимания на бумажку. {w}Я встал с кровати и поднял этот документ."
            "—Здесь говорится, что у вас всё в порядке, и вечером вас отправят в Москву."
            s "—В Москву? И что мне там делать? А-ха-ха-ха!"
            "—Они просто не знают, куда вас отправить."
            s "—Ну и ладно. У меня там есть знакомые, не пропаду.{w} Есть курить?"
            "—Нет... Не курю."
        "Продолжать наблюдать":
            $ lazynessPoints += 1
            "Я не подавал никаких признаков того, что проснулся, и наблюдал за этой сценой.{w} Забавно, сосед так искренне отвечает врачу, будто бы правда хочет что-то объяснить ему"
            "Наконец, врач ушёл, швырнув бумажку соседу на кровать."
    "Сосед потянулся за своей сумкой. {w}Стоп, как у него уцелела сумка? Везучий-то какой!"
    "Он достал небольшой серебристый ноутбук, открыл его и стал что-то смотреть"
    "—Это ваш ноутбук?"
    if roommatePoints>0:
        "—Да, сумка была на мне во время крушения. {w}Мне крупно повезло, что она плотная, и ноут не успел промокнуть. Жаль, что документы были в чемодане..."
        "—Если хочешь, можешь воспользоваться, вижу как ты смотришь на него"
        "—Да, мне очень нужно выйти в сеть! Спасибо"
        "Я взял его ноутбук и в первую очередь начал искать информацию об этом месте"
        "Потом стал искать информацию об исследовании на совместимость. В испанском сегменте действительно были некоторые упоминания."
        "Географически эти люди расположены в разных уголках страны и в разное время. Есть упоминание и в моём городе. Можно попробовать пройти анализ в этом госпитале, только как мне объяснить врачу необходимость этого?"
        "Ноутбук предательски запищал о низком заряде аккумулятора"
        s "—Так, а теперь я. Всю батарею мне посадил! "
        "Сосед забрал свой ноут."
        "—Зарядник тоже был в чемодане?"
        s "—А ты умён! Хах"
        "На этом я решил покинуть палату и найти врача. И как мне напроситься на анализ? Его же не проходят просто так? Понятия не имею..."
        "Может, прикинуться наркоманом? {w}Нет, бред! Тут мой взгляд привлекает плакат на посту. Судя по его содержанию, это клиника одна из ведущих в области борьбы с ВИЧ."
        "Я показываю на него пальцем и говорю проходящему мимо врачу:"
        "—Ай нид...{w}Аналайсис...{w}Вич... Эйдс... Нид ту ду аналайсис!"
        "Врач с недоверием смотрит на меня. Я говорю с ужасным акцентом и путаюсь в словах"
        "—Ай нид ту тест майселф фор эйдс!"
        "Кое как выдавил из себя более-менее осмысленную фразу"
        "Кажется, врач понял меня. Он написал что-то в своём смартфоне и вручил мне."
        "Там был открыт переводчик с испанского на русский. Удивительно, врач в Испании не знает английского."
        "\"Если Вам нужно пройти ВИЧ анализ, приходите в 8 часов утра в 12 корпус. Ничего не есть.\""
        "Я переключаю переводчик в обратный режим, и пишу \"Спасибо\" по-русски, отдаю смартфон врачу и ухожу в свою палату"
        "Ну что же, надеюсь, получится."
        "Остаток дня я провожу в палате, общаясь с соседом о всяких глупостях."
        "Ложусь спать примерно в полночь, ставлю будильник на электронных часах в палате."
        "Утром направляюсь сдавать анализ"
        jump analysis

    # Если плохие отношения с соседом
    else:
        "—Тебе-то какое дело? Иди спи, малой."
        "Такая грубость вводит меня в ступор. Хотя, я и сам не был с ним особо вежлив. Лишь спустя несколько секунд отвечаю ему"
        menu: 
            "Да не, ничего...":
                "—Да я так, просто..."
                s "Что хитро, то и просто! Ха-ха-ха"
                "Сосед залился смехом"
                s "—Можешь воспользоваться моим ноутом... Но сначала курить найди мне, малой."
                menu:
                    "Согласиться":
                        "Ладно... Я согласен."
                        s "Ха-ха-ха! Жду!"
                        "И где мне искать сигареты? Денег у меня нет...{w} Наверняка, тут есть курилка. Попрошу там парочку."
                        "Я бродил по территории где-то 20 минут. Нашёл компанию курящих испанцев. Они что-то громко обсуждали и смеялись, страшновато подходить."
                        "Пересилив себя, я подошёл к ним и жестом показал, что хотел бы сигарету. На что получил облако дыма в лицо. Ну и гадкий запах! Не похоже на табачный..."
                        "К нам выбежал охранник, испанцы бросились врассыпную. {w}Я замешкался, но через секунду побежал за ними."
                        "..."
                        "Вроде бы пронесло.{w} Я выпросил несколько сигарет и зажигалку у растаманов и направился в свою палату озираясь по сторонам, чтобы не встретить охранника"
                        "Знакомый коридор, прохожу мимо поста"
                        "Сосед тем временем смотрел в окно. Услышав, как я зашёл, он повернулся в мою сторону"
                        s "— Ну, чем обрадуешь?"
                        "Я протянул ему сигареты"
                        s "— Хорош, малой."
                        "Он взял сигареты и направился к выходу.{w} Наверное, это означает, что я могу взять его ноут."
                        "Я взял его ноутбук и в первую очередь начал искать информацию об этом месте"
                        "Потом стал искать информацию об исследовании на совместимость. В испанском сегменте действительно были некоторые упоминания."
                        "Географически эти люди расположены в разных уголках страны и в разное время. Есть упоминание и в моём городе. Можно попробовать пройти анализ в этом госпитале, только как мне объяснить врачу необходимость этого?"
                        "Ноутбук предательски запищал и разрядился."
                        "На этом я решил покинуть палату и найти врача. И как мне напроситься на анализ? Его же не проходят просто так? Понятия не имею..."
                        "Может, прикинуться наркоманом? {w}Нет, бред! Тут мой взгляд привлекает плакат на посту. Судя по его содержанию, это клиника одна из ведущих в области борьбы с ВИЧ."
                        "Я показываю на него пальцем и говорю проходящему мимо врачу:"
                        "—Ай нид...{w}Аналайсис...{w}Вич... Эйдс... Нид ту ду аналайсис!"
                        "Врач с недоверием смотрит на меня. Я говорю с ужасным акцентом и путаюсь в словах"
                        "—Ай нид ту тест майселф фор эйдс!"
                        "Кое как выдавил из себя более-менее осмысленную фразу"
                        "Кажется, врач понял меня. Он написал что-то в своём смартфоне и вручил мне."
                        "Там был открыт переводчик с испанского на русский. Удивительно, врач в Испании не знает английского."
                        "\"Если Вам нужно пройти ВИЧ анализ, приходите в 8 часов утра в 12 корпус. Ничего не есть.\""
                        "Я переключаю переводчик в обратный режим, и пишу \"Спасибо\" по-русски, отдаю смартфон врачу и ухожу в свою палату"
                        "Ну что же, надеюсь, получится."
                        "Остаток дня я провожу в палате, общаясь с соседом о всяких глупостях."
                        "Ложусь спать примерно в полночь, ставлю будильник на электронных часах в палате."
                        "Утром направляюсь сдавать анализ"
                        jump analysis
                    "Всё-таки показать ему средний палец":
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
    "Нет! Он обычный человек!"
    "Может подставить его?{w} Но как?"
    "Да ну к чёрту это вредительство, надо сконцентрироваться на своих проблемах."
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

label nextDay:
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
        "Стучусь"
        "На этот раз мне открывают дверь. Передо мной человек в химзащите. Что-ж, класс!"
        "Я пытаюсь объяснить, что мне нужно пройти анализ."
        "Человек в химзащите провожает меня в кабинет"
        jump analysis

    # if brokenFinger == True:
    #    "Я подбегаю к медработнику и на ломанном английском жалуюсь на соседа, показываю, что он сделал с моим пальцем"
    #    "..."
    #    "Мне загипсовали палец. Судя по снимкам, он ещё не скоро заживёт."
    #    "Я не могу здесь больше находиться!"
    #    "Надо валить из этой шараги!"

label analysis:
    "проведение анализа. С гг связываются вояки."


