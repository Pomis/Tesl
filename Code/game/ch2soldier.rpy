define r = Character('Голос из рации', color = "#f45678")
label rootSoldier:

    
    "— Ну я по большей части скорее кодер, чем техник, но раз это требует лишь базовых познаний думаю справлюсь."
    nvl clear
    nvlc "C этими словами я принялся за работу."
    nvlc "Конструкция рации не была похожа на что-либо, что бывало у меня в руках, но по каким-то непонятным причинам я понимал, что и как делать. Это больше напоминало сотворение предмета искусства, чем починку технической новинки. Какие-то волокна, рисунки. Видимо за основу взяты технологии этих самых Инферно"
    nvlc "За починкой рации я и сам не заметил как моя обида на неё куда-то улетучилась. Достаточно сложно обижаться на столь несерьёзного человека. Да и подобные вещи всегда успокаивали меня. Помнится в детстве я мог часами собирать пазлы или налаживать какую-нибудь бытовую технику. "
    nvlc "Когда я повзрослел, то это уже перестало меня так завлекать, но то чарующее спокойствие до сих пор проявляется при погружении в подобное занятие."
    nvlc "Надо признать, что в какой-то степени я благодарен этой девушке за столь грубое вмешательство в мою жизнь. "
    nvlc "Мне всегда нужен был какой-то пинок, чтобы что-то поменять в моей жизни, ибо она быстро обрастала какой-то рутинной, а сам изменить я ничего не мог. Даже не совсем не мог - скорее не хотел. "
    nvlc "Не сказать, что моя жизнь меня не устраивала, но определённо мне хотелось большего. Но самостоятельно я не был готов прикладывать усилий, ибо считал, что раз сейчас мне нормально, то результат не будет стоить потраченных усилий, ведь мне будет лишь чуть лучше, чем сейчас."
    nvlc "Может я просто не мог полностью наслаждаться успехами и горевать над потерями? Да, скорее всего так и было."
    nvl clear
    yu "— Эй, ты там не уснул? Скоро закончишь?"
    "Юминг вытащила меня из размышлений."
    "— Да, уже всё."
    "Задумавшись, я и сам не заметил, как закончил ремонт."
    $ usedDirectRadio = True
    "Она взяла в руки передатчик, послышался характерный треск. Вот только не из динамиков, а прямо в ушах. Да что это за хрень такая?"
    yu "— Орихалк, приём, это Чайка."
    "— Орихалк на связи. Чайка, ты жива? Доложи ситуацию."
    yu "— Я в порядке, подлодка потеряна. Я нахожусь на спасательной шлюпке. Требуется эвакуация."
    r "По твоим координатам направлен транспортник. Жди на месте."
    yu "— Куда я денусь-то, с подводной лодки."
    r "— Ты же сказала, что подлодка потеряна..."
    yu "— Забей, выражение такое... В общем жду. Конец связи."
    menu:
        "— Почему Чайка?":
            yu "— Не знаю. Просто позывной."
        "— А ты, похоже, очень ценный солдат?":
            "— Ради тебя спасательную операцию проводят."
            $ yumingPoints += 1
            yu "— Ну конечно! Я незаменима."
    yu "— Эх, скорее бы на базу. Небось Мария там волнуется."
    "— Кто такая Мария?"
    yu "— Сумасшедший учёный нашей базы и, по совместительству моя подруга."
    "— В смысле сумасшедший учёный?"
    yu "— Она является главой научного отдела и очень любит придумывать странные вещи. Вы с ней чем-то похожи."
    "— Тогда, думаю, мы подружимся."
    "— Стоп. "
    "— Вы использовали этот передатчик в качестве приманки для Инферно?"
    yu "— Ой..." 
    "— Они придут за нами?"
    yu "— Мы сейчас прямо над их городами. Думаю, они уже засекли сигнал."
    "— Ты чего такая спокойная? Они же нас прикончат! У нас нет оружия!"
    "Я выхватил из её рук передатчик и замахнулся зашвырнуть его как можно дальше."
    yu "— СТОЙ! Просто сломай его!"
    "Я ударил им со всей силы о борт лодки. {w}Ещё раз. "
    "Готово."
    yu "— Посмотрим, кто быстрее, подводный титан, или вертолёты Ка-70."
    $ heardAboutTitan = True
    "— Такие вообще существуют?"
    "— Титан? "
    yu "— Да, с таким мы сражались. Эта тварь сломала мою любимую подводную лодку!"
    "— Титан значит..." with bloodrage
    yu "— Ой... Прости, забыла совсем."
    "— Я найду и уничтожу каждого титана!"
    # bulka: "Потому я обязательно попаду в разведкорпус!" Найс отсылка
    yu "— Бессмысленно. Это просто управляемые существа. У них нет сознания."
    "— Мне всё равно. Они все будут уничтожены! Я отомщу за свою семью!"
    "Юминг явно чувствовала себя неуютно и ничего не говорила."
    "..."
    "— Сколько примерно будет лететь вертолёт?"
    yu "— Часа два, наверное. Я надеюсь, что Инферно просто не успели засечь сигнал."
    "— Какой смысл вообще провоцировать нападение искусственных существ?"
    yu "— Таким образом они выдают своё местоположение."
    "— И всё?"
    yu "— Я всего лишь пилот, отстань."
    yu "— Я устала, дай отдохнуть!{w} Ладно, ещё один вопрос и я спать."
    "СПАТЬ? В ТАКОЙ СИТУАЦИИ? СЕРЬЁЗНО?"
    "— Ладно."
    menu:
        "— Той ночью. Они же не сразу напали на корабль... Может у них проблемы с точностью?":
            $ askedAboutAccuarcy = True
            yu "— Нет же, мы встретили их под водой."
            yu "— Всё, а теперь я спать!"
            "Она что, серьёзно?"
        "— Что за сигнал такой подаёт передатчик?":
            yu "— Понятия не имею.{w} Марию спросишь."
            $ wantToAskAboutSignal = True
            "— Это не считается за ответ!"
            yu "— А я и не обещала ответить."
            "Юминг хитро улыбнулась."
        "— Кто главный в Инферно?":
            yu "— Вот сам и выяснишь. "# Наши социологи исследуют их поведение и придерживаются мнения, что у них строгий авторитарный режим, но это просто догадки. 
            # pomis: слишком научно говорит
            "— Это не считается за ответ!"
            yu "— А я и не обещала ответить."
            yu "— Хотя, стоп. Мне кидали какие-то разведданные. Загляни ко мне как-нибудь, поделюсь. Комната E09." 
            $ knowYumingRoom = True 
            # Pomis: Ключевая переменная для возоможности выхода на Юминг-рут. Нужно дать игроку ещё шанс получить этот True
            # bulka: Немножко тупо, что переменная даётся таким образом. Тут же наугад фактически.
            # pomis: шанс стал выше
            "— Разве это не секретная информация?"
            yu "— Само наше существование — секретная информация."
            "Юминг хитро улыбнулась."
    "— Юминг!"
    yu "— Ну что тебе?{w} Уф, спроси ещё что-нибудь, раз так хочешь. И спать."
    menu:
        "— Той ночью. Они же не сразу напали на корабль... Может у них проблемы с точностью?" if askedAboutAccuarcy==False:
            yu "— Нет же, мы встретили их под водой."
            yu "— Всё, а теперь я спать!"
            "Она что, серьёзно?"
        "— Что за сигнал такой подаёт передатчик?" if wantToAskAboutSignal==False:
            yu "— Понятия не имею.{w} Марию спросишь."
            $ wantToAskAboutSignal = True
            "— Это не считается за ответ!"
            yu "— А я и не обещала ответить."
        "— Где мне найти Марию?" if wantToAskAboutSignal:
            yu "— Она почти всегда в лаборатории."
        "— Кто главный в Инферно?" if knowYumingRoom==False:
            yu "— Вот сам и выяснишь."
            "— Это не считается за ответ!"
            yu "— А я и не обещала ответить."
            yu "— Хотя, стоп. Мне кидали какие-то разведданные. Загляни ко мне как-нибудь, поделюсь. Комната E09." 
            $ knowYumingRoom = True
            "— Разве это не секретная информация?"
            yu "— Само наше существование — секретная информация."
        "— А какая ещё секретная информация у тебя для меня есть?" if knowYumingRoom:
            yu "— На то она и секретная, чтобы не делиться ею с тобой."
            "— Да ты сама себе противоречишь!"
            yu "— Ладно, я тебе расскажу, свой сон!"
    "Через пару мгновений она уже сладко спала."
    "Глядя на неё, мне тоже захотелось спать..."
    "Я закрыл глаза, но долго не мог уснуть."
    "Мне не важно, что это за война. Я даже не слышал, что мы воюем с кем-то. Но я найду тех, кто забрал мою семью."
    "Найду. {w}И уничтожу."
    hide boat onlayer middle
    hide yuming onlayer forward
    call flashback2
    play music kiitos
    scene bg ocean night onlayer background
    show boat night onlayer middle at bottom
    $ camera_move(500, -2000, 0, 0, 0)
    $ camera_moves( ( (660, -2100, 0, 0, 2, 'ease'),(500, -2000, 0, 0, 4, 'ease') ), loop=True)
    "Ого, уже так темно...{w} Нас до сих пор не забрали вертолёты? {w}Хотя, нас до сих пор и не убили..."
    "И как это вообще получилось? О нас забыли обе стороны? Я в сердцах ударил по первому попавшемуся под руку кейсу."
    show yuming night onlayer forward at center
    yu "— А? Что?"
    "— Почему нас не забрали?"
    yu "— Я надеялась очнуться на военной базе... Зачем ты меня разбудил? Мне снилось, что я дома..."
    "— Ты говорила, что нас заберут через два часа. Почему уже ночь?"
    "Бесит!{w} Я толкнул её в плечо."
    "— ЭЙ!"
    # bulka: Грубовато мы с ней. Может тут тогда выбор запилить. В одном из вариантов очки с Юминг забирают.
    yu "— Да заберут нас, не переживай."
    "— Нас бы давно уже забрали! Сколько времени прошло!"
    yu "— Наверняка на то есть причины, остынь."
    # Pomis: Так как они вышли на связь с помощью передатчика-приманки, а потом сигнал пропал, руководство пришло к выводу, что Инферно тут же их уничтожили на месте. Из-за этого спасательную операцию отменили.
    play sound helicopter
    "Утром меня разбудил шум пролетающего вдали вертолёта. Он пролетал совсем далеко, и на приличной высоте, должно быть, чтобы площадь обзора была больше. "
    "— Они всё-таки прилетели!"
    "В таком случае, он быстро заметит нас. Я всячески привлекал внимание, махал руками, кричал, хоть я и понимал, что это не поможет, но всё равно, я не мог спокойно сидеть на месте."
    yu "— Это не Ка-70. {w}Это какой-то гражданский отстой."
    "Я даже не знаю, что более удивительно, что это не тот вертолёт, или что она на таком расстоянии способна различать модели вертолётов."
    "Это оказался испанский спасательный вертолёт, всего выжило около 20 человек. Я искал среди них маму, папу, Тоню, но безуспешно."
    stop sound 
    "Я не стал ни с кем разговаривать. Какая-то дама безостановочно рыдала, да и у других вид был не лучше."
    "Мы расположились на обочине и ждали, когда прилетит последний вертолёт."
    "Тем временем, Юминг что-то доказывала стражам порядка на английском, а как ультимативный аргумент, достала корочку, чем изменила выражение их лиц со снисходительно-жалостливых на глубоко удивлённые."
    yu "— Эй, [playerName], нам пора!"
    "К нам подошли двое военных и жестом позвали за собой. Нас повезли на внедорожнике отдельно от остальной группы."
    yu "— Они попытаются выйти на связь с русскими, чтобы те, в свою очередь, вышли на связь с нашей базой."
    "— Попытаются? Это так сложно?"
    yu "— По правде говоря, эти испанцы даже не в курсе о существовании нашей базы, я просто передала им набор кодовых слов, по которым русские должны понять ситуацию."
    "— Далеко еще ехать? Как-то укачивает, того и гляди..."
    "Я вовремя осекся. Чуть было не рассказал о своем страхе высоты в не самой тактичной форме."
    yu "— Не особо. Сейчас довезут до базы и пересядем."
    "Юминг сдержанно обернулась, и, не заметив снаружи видимой угрозы, окончательно успокоилась."
    yu "— Погодка так себе."
    "— Согласен."
    "Я слишком устал, чтобы вести разговоры ни о чем. К тому же произошло слишком многое, чтобы я вообще мог трезво соображать."
    "Глаза начали закрываться, как вдруг автомобиль остановился."

    yu "— Вставай. Пересадка."

    "Я уж понял..."

    "Голова болела так, словно в нее загрузили по меньшей мере три откупоренных баллона, нещадно заполнявших ее кислородом."
    "Ко мне подошёл мужчина в российской военной форме."
    "Военный" "— Черт, шевели булками! Гражданские, мля. Дали им спорт в массы. Занимайся! Не хочу, хочу за компуктером сидеть! Мужики, называется..."
    "Кажется, я это где-то слышал."
    yu "— Генерал Ганц! Что произошло?"
    gen "— Отставить расспросы."
    "Генерал перевёл взгляд на меня."
    gen "— Полагаю, ты уже в курсе происходящего. Залезай в вертолёт, живее!"
    "Ничего себе, бесцеремонность. Перед нами стоял какой-то необычный вертолёт, правда, слегка поцарапанный. Даже думать страшно, насколько там суровый пилот... Мы последовали за генералом и расположились внутри."


    # "Неудивительно. Вояки всегда признавали только грубую силу. У гражданских ее попросту нет, а посему им положена низшая ступень в иерархии."

# — Сюда.
# — Зачем пересадка?
# — У всех вертолетов четкий маршрут, выведенный сегодня утром. Он согласован с перемещением шпионов инферно, потому является самым безопасным.
# — Ясно.

# В общем-то, нихрена я не понял. Но если переспрошу, решит, что я полный кретин.
# pomis: не очень вписывается
    
#Stan: вот с этого места пиздец какой-то. голосую за откат на версию без наркоманов и перестрелок. И без истерики гг
    pi0 "— Заходите, налетайте!"
    "— Ч-чего?!"

    "Налетать? Разве так не говорят, когда потчуют?"

    $ knowIvanName = True
    yu "— Расслабься. Это Иван, он, скажем так, пошел в вояки только по одной причине."
    "— Много денег?"
    yu "— Нет. Разрешены легкие наркотики!"
    yu "— Правда, он их даже не принимает. Но всегда называет это своей единственной причиной."
    pi0 "— Милости прошу к нашему шалашу! Приветствую на борту Чёрного Стрижа!"
    "Он точно ничего не принимает?"
    # "Это я тоже где-то слышал. Ну да ладно."
    "— А он нас не угробит?"
    "Ясен пень, мне стало не по себе от такого «гостеприимства»."# К тому же едва ли наркоман, пусть даже торчок, способен адекватно управлять столь сложным видом транспорта."

    yu "— Ты совсем дурак? Стали бы его здесь держать, не будь он мастером своего дела."
    "— И то верно. Но эти царапины не дают мне покоя."
    yu "— А-а... Не бойся, это всего лишь следы от пуль!"

    "Всего лишь?! Страшно думать, какая же «насыщенная» у них жизнь."

    "— Значит, столько шумихи ради одного меня?"
    pi "— Ну, надо же доставить тебя в безопасное место. Мы военные, а не какая-нибудь якудза. Ты ведь из-за нас потерпел крушение."

    hide yuming onlayer forward
    hide boat onlayer middle
    hide bg onlayer forward
    hide bg onlayer middle
    hide bg onlayer background
    scene bg helic
    "Я осмотрелся. В кабине пилота даже нет привычных элементов управления."
    pi "— Вы использовали передатчик, предназначенный для привлечения внимания Инферно. Через минуту сигнал с передатчика пропал. Вот командование и решило, что вас уже не спасти. Так что же произошло на самом деле?"
    "— Я сломал передатчик. Взял его. И с размаху ударил о борт лодки."
    pi "— Красава!"
    show gantz serious onlayer master:
        xpos 0.83 ypos 1.34 xanchor 1.0 yanchor 1.0 zoom 1.42     
    gen "— Так, я должен тебе кое-что показать."
    "Генерал достаёт из сумки ноутбук и включает запись с рабочего стола. Должно быть, часто приходится показывать."
    "На видеозаписи существа, ростом с девятиэтажку, покрытые лавой, перемещаясь с невероятной скоростью разрушают всё на своём пути."
    gen "— Ну раз ты посмотрел... Теперь ты знаешь военную тайну, у тебя нет выбора." 
    # bulka: Я просто в голос заорал на этом моменте"
    "Ты издеваешься что ли? С какой радости ты мне в лицо военной тайной тыкаешь? Мы в аниме, что ли?"
    "Тоже мне, военная тайна."
    "— Что это за монстры?"
    gen "— Мы не знаем всего об их природе. Но мы знаем, как с ними бороться. На нашей стороне лучшие учёные со всего мира и финансирование сильнейших держав."
    gen "— Ты готов сражаться?"
    menu:
        "— Да.":
            $ gantzPoints += 1
            gen "— Вот и хорошо."
            "Думаю, что даже если бы я собрал всю смелость в кулак, я бы не смог сказать что-то другое."

        "— А я могу подумать?":
            $ leadershipPoints += 1
            gen "— Нет. На самом деле, всё уже решено, спросил из вежливости."

    "Вертолёт постепенно набирал высоту."
    "Иван старательно повертел странные рычаги управления, после чего повернулся к нам и подмигнул."
    "— Кошмар. А мы точно не убьемся?"
    yu "— Кто знает..."
    "Звук вращающихся лопастей стал затихать, его сменил жуткий рёв неизвестной мне природы."
    "И тут вертолет, словно движимый божественной силой, помчался вперед."#, словно бешеный пес." 
    # pomis: какой нахуй бешеный пёс
    "— Что-о-о?"
    "Мой крик потерялся где-то позади."
    "Разве вертолёты способны так быстро разгоняться?"
    "— Что тут происходит?"
    # bulka: Что не так с капсом?
    # pomis: Оскар жаловался, что слишком много, и что это дно
    # bulka: Лол. Это показывает, что реплика на повышенных тонах. И тут его было 3-4 строчки на 200+ строк.
    yu "— А? Что не так?"
    "— Разве вертолеты так летают?"
    yu "— Конечно. Это же вертолет Ивана."
    "Достойное объяснение. Но, что вполне закономерно, я от этого ещё сильнее испугался."
    "Только бы выжить! Только бы выжить! Какого чёрта это вообще со мной происходит? Почему я? Почему никто другой?"
    "Я сам не заметил, как по-мертвецки уснул. Ну или потерял сознание. {w}Голоса плыли среди бесконечного океана звука, порождаемого рёвом вертолёта."

    "Когда я очнулся, мой вестибулярный аппарат дал полнейший сбой."

    "С трудом удерживая проклятие, готовое вырваться из моего рта не самым традиционным способом, я встал."
    # bulka: Не уверен, что проклятие выходит из желудка. Офк, намёк на рвоту, но тут оно равносильно рандомному слову, имхо.
    # pomis: Не я писал, хз)
    # "И только тогда осознал."

    # pi "— Ложись! Черт вас, гражданских, дери!"

    # "Рука парня легла на мою шею и силой принудила сползти вниз."
    # pi "— Да как они вообще нас выследили? Мы промчались быстрее пули, ан нет, все-таки раскрыли."

    # "Ледяной холодок промчался по спине. Похоже, это было никакое не учение..."
    # pi "— Новичок, держись! Сейчас слегка потрясет."

    # "Услышав предупреждение, я мгновенно уцепился руками за ножки скамьи. И вовремя среагировал."

    # "Спустя секунду пропеллер издал булькающий звук, а воздух едва не стряхнул моё тело."

    # yu "— Иван! Они обстреливают нас!"
    # pi "— Спокойно. Опасная зона скоро будет пройдена!"
    
    # bulka: Хз-хз в общем. Имхо перса испортили. Хотя может игрокам понравится. Но с законами физики явно стоит подружиться. Иначе научный реализм можно исключить. Учитывая сколько раз я уже про него писал, то пора, думаю, это сделать.
    # pomis: А что с персом? Можно переделать реплики или убрать упоминание наркоты? Да, наркота тут явно лишняя. А с ненормальной скоростью вертолёта попытался разобраться.

    # nvl clear
    
    # nvlc "В эту же минуту вертолёт взлетел. Пилот управлял им не прикладывая никаких усилий. Ну, или так выглядело со стороны. Он просто положил одну руку на круглое устройство на панели управления и весело разговаривал с другим солдатом."
    # nvlc "Постепенно мы набрали огромную скорость. Не уверен, что обычные вертолёты вообще способны преодолеть скорость звука. Но через полтора часа мы уже были в Японском море."
    # nvl clear
    

    jump warBase

