define r = Character('Голос из рации', color = "#f45678")
label rootSoldier:

    
    "— Ну я по большей части скорее кодер, чем техник, но раз это требует лишь базовых познаний думаю справлюсь."
    "C этими словами я принялся за работу."
    "Конструкция рации не была похожа на что-либо, что бывало у меня в руках, но по каким-то непонятным причинам я понимал, что и как делать."
    "Это больше напоминало сотворение предмета искусства, чем починку технической новинки. Какие-то волокна, рисунки. Видимо за основу взяты технологии этих самых Инферно"
    "За починкой рации я и сам не заметил как моя обида на неё куда-то улетучилась. Достаточно сложно обижаться на столь несерьёзного человека. Да и подобные вещи всегда успокаивали меня. Помнится в детстве я мог часами собирать пазлы или налаживать какую-нибудь бытовую технику. "
    "Когда я повзрослел, то это уже перестало меня так завлекать, но то чарующее спокойствие до сих пор проявляется при погружении в подобное занятие."
    "Надо признать, что в какой-то степени я благодарен этой девушке за столь грубое вмешательство в мою жизнь. "
    "Мне всегда нужен был какой-то пинок, чтобы что-то поменять в моей жизни, ибо она быстро обрастала какой-то рутинной, а сам изменить я ничего не мог. Даже не совсем не мог - скорее не хотел. "
    "Не сказать, что моя жизнь меня не устраивала, но определённо мне хотелось большего. Но самостоятельно я не был готов прикладывать усилий, ибо считал, что раз сейчас мне нормально, то результат не будет стоить потраченных усилий, ведь мне будет лишь чуть лучше, чем сейчас."
    "Может я просто не мог полностью наслаждаться успехами и горевать над потерями? Да, скорее всего так и было."
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
    "СПАТЬ? В ТАКОЙ СИТУАЦИИ? ОТ ЧЕГО ТЫ УСТАЛА?"
    "— Ладно."
    menu:
        "— Той ночью. Они же не сразу напали на корабль... Может у них проблемы с точностью?":
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
            yu "— Вот сам и выяснишь. Наши социологи исследуют их поведение и придерживаются мнения, что у них строгий авторитарный режим, но это просто догадки."
            "— Это не считается за ответ!"
            yu "— А я и не обещала ответить."
            yu "— Хотя, стоп. Мне кидали какие-то разведданные. Загляни ко мне как-нибудь, поделюсь. Комната E09." 
            $ knowYumingRoom = True 
            # Pomis: Ключевая переменная для возоможности выхода на Юминг-рут. Нужно дать игроку ещё шанс получить этот True
            # bulka: Немножко тупо, что переменная даётся таким образом. Тут же наугад фактически.
            "— Разве это не секретная информация?"
            yu "— Само наше существование — секретная информация."
            "Юминг хитро улыбнулась."
    "Через пару мгновений она уже сладко спала."
    "Глядя на неё, мне тоже захотелось спать..."
    hide boat onlayer middle
    hide yuming onlayer forward
    call flashback2
    scene bg ocean night onlayer background
    show boat night onlayer middle at bottom
    $ camera_move(500, -2000, 0, 0, 0)
    $ camera_moves( ( (660, -2100, 0, 0, 2, 'ease'),(500, -2000, 0, 0, 4, 'ease') ), loop=True)
    "Ого, уже так темно...{w} Нас до сих пор не забрали вертолёты? {w}Хотя, нас до сих пор и не убили..."
    "И как это вообще получилось? О нас забыли обе стороны? Я в сердцах ударил по первому попавшемуся под руку кейсу."
    show yuming night onlayer forward at center
    yu "— А? Что?"
    "— Почему нас не забрали?"
    yu "— Я надеялась очнуться на военной базе... Зачем ты меня разбудил?"
    "— Ты говорила, что нас заберут через два часа. Почему уже ночь?"
    "Но Юминг уже спала. Бесит!{w} Я толкнул её в плечо."
    "— ЭЙ!"
    # bulka: Грубовато мы с ней. Может тут тогда выбор запилить. В одном из вариантов очки с Юминг забирают.
    yu "— Да заберут нас, не переживай."
    "— Нас бы давно уже забрали! Сколько времени прошло!"
    yu "— Наверняка на то есть причины, остынь."
    # Pomis: Так как они вышли на связь с помощью передатчика-приманки, а потом сигнал пропал, руководство пришло к выводу, что Инферно тут же их уничтожили на месте. Из-за этого спасательную операцию отменили.
    play sound "music/258007__dallasbass__helicopter-in-mountains.wav"
    play music "music/Janneh_-_06_-_Kiitos.mp3"
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
    "К нам подошли двое военных и жестом позвали за собой. Нас повезли отдельно от остальной группы."
    yu "— Они попытаются выйти на связь с русскими, чтобы те, в свою очередь, вышли на связь с нашей базой."
    "— Попытаются? Это так сложно?"
    yu "— По правде говоря, эти испанцы даже не в курсе о существовании нашей базы, я просто передала им набор кодовых слов, по которым русские должны понять ситуацию."
    "По приезде на военную базу нас уже ждали люди в форме, которую я раньше никогда не видел."
    "Особенного внимания заслуживал статный мужчина, стоявший посередине."
    yu "— Генерал Ганц! Что произошло?"
    gen "— Отставить расспросы."
    "Генерал перевёл взгляд на меня."
    gen "— Полагаю, ты уже в курсе происходящего. Прошу пройти на борт вертолёта."
    "Ничего себе, бесцеремонность. Мы последовали за генералом и расположились внутри вертолёта. Снаружи выглядит как обычный российский Ка-60. Но начинка очень необычна. Я никогда подобного не видел."
    "В кабине пилота даже нет привычных элементов управления."
    "Пилот заметил моё внимание, и повернулся ко мне."
    pi0 "— Приветствую на борту Чёрного Стрижа! Объясняю ситуацию."
    pi0 "— Вы использовали передатчик, предназначенный для привлечения внимания Инферно. Через минуту сигнал с передатчика пропал. Вот командование и решило, что вас уже не спасти. Так что же произошло на самом деле?"
    "— Я сломал передатчик. Взял его. И с размаху ударил о борт лодки."
    pi0 "— Красава!"
    gen "— Так, я должен тебе кое-что показать."
    "Генерал достаёт из сумки ноутбук и включает запись с рабочего стола. Должно быть, часто приходится показывать."
    "На видеозаписи существа, ростом с девятиэтажку, покрытые лавой, перемещаясь с невероятной скоростью разрушают всё на своём пути."
    gen "— Ну раз ты посмотрел... Теперь ты знаешь военную тайну, у тебя нет выбора." 
    # bulka: Я просто в голос заорал на этом моменте"
    "Ты издеваешься что ли? С какой радости ты мне в лицо военной тайной тыкаешь? Мы в аниме что ли?"
    "Тоже мне, военная тайна."
    "— Что это за монстры?"
    gen "— Мы не знаем всего об их природе. Но мы знаем, как с ними бороться. На нашей стороне лучшие учёные со всего мира и финансирование сильнейших держав."
    gen "— Ты готов сражаться?"
    "— Да."
    "Думаю, что даже если бы я собрал всю смелость в кулак, я бы не смог сказать что-то другое."
    "В эту же минуту вертолёт взлетел. Пилот управлял им не прикладывая никаких усилий. Ну, или так выглядело со стороны. Он просто положил одну руку на круглое устройство на панели управления и весело разговаривал с другим солдатом."
    "Наш вертолёт сопровождали два таких же. Зачем?"
    "Постепенно мы набрали огромную скорость. Не уверен, что обычные вертолёты вообще способны преодолеть скорость звука. Но через полтора часа мы уже были в Японском море."
    
    

    jump warBase

    # yu "—Если у тебя есть небольшие познания в технике, то, будучи \"способным\", ты спокойно сможешь починить практически любую вещь с подобной архитектурой. "
    # yu "—Я, к сожалению, гуманитарий."
    # "Высунув язык, она склонила голову и ткнула себя кулаком в макушку."
    # "— Ну я по большей части скорее кодер, чем техник, но раз это требует лишь базовых познаний думаю справлюсь."
    # "C этими словами я принялся за работу."
    # "Конструкция рации не была похожа на что-либо, что бывало у меня в руках, но по каким-то непонятным причинам я понимал, что и как делать."
    # "Это больше напоминало сотворение предмета искусства, чем починку технической новинки. Какие-то волокна, рисунки. Видимо за основу взяты технологии этих самых Инферно"
    # "За починкой рации я и сам не заметил как моя обида на неё куда-то улетучилась. Достаточно сложно обижаться на столь несерьёзного человека. Да и подобные вещи всегда успокаивали меня. Помнится в детстве я мог часами собирать пазлы или налаживать какую-нибудь бытовую технику. "
    # "Когда я повзрослел, то это уже перестало меня так завлекать, но то чарующее спокойствие до сих пор проявляется при погружении в подобное занятие."
    # "Надо признать, что в какой-то степени я благодарен этой девушке за столь грубое вмешательство в мою жизнь. "
    # "Мне всегда нужен был какой-то пинок, чтобы что-то поменять в моей жизни, ибо она быстро обрастала какой-то рутинной, а сам изменить я ничего не мог. Даже не совсем не мог - скорее не хотел. "
    # "Не сказать, что моя жизнь меня не устраивала, но определённо мне хотелось большего. Но самостоятельно я не был готов прикладывать усилий, ибо считал, что раз сейчас мне нормально, то результат не будет стоить потраченных усилий, ведь мне будет лишь чуть лучше, чем сейчас."
    # "Может я просто не мог полностью наслаждаться успехами и горевать над потерями? Да, скорее всего так и было."
    # yu "— Эй, ты там не уснул? Скоро закончишь?"
    # "Юминг вытащила меня из размышлений."
    # "— Да, уже всё."
    # "Задумавшись, я и сам не заметил, как закончил ремонт."
    # yu "— Какой-то ты странный."
    # menu: 

    #     "Кто бы говорил!":
    #         "— Кто бы говорил... "
    #         "Буркнул я и протянул рацию."
    #         "— Сама-то как снег на голову рухнула и ещё что-то требуешь. Ты здесь не одна, кто попал в тяжёлую ситуацию."
    #         "Не говоря уже о том, что именно по твоей вине мы тут чалимся..."
    #         "Я всегда был человеком, который найдёт причину поворчать. Даже вернее будет сказать повод."
    #         "А когда от меня ещё что-то так нагло требуют, выгоняя из зоны комфорта, то тут уже грех не поворчать."

    #     "— Какой есть, такой есть":
    #         "— Какой есть, такой есть"
    #         "Я улыбнулся я и протянул рацию."
    #         yu "— Чего это ты улыбаешься? Какую-то пошлость вообразил?"
    #         "Она обхватила себя руками."
    #         "— Слушай, ты аниме много смотришь что ли?"
    #         yu "— Да, откуда ты узнал?"
    #         "Я решил подшутить над ней"
    #         "— Я ясновидец просто."
    #         yu "— Ясновидец? Такого таланта среди способных я замечала."
    #         "Юминг серьёзно задумалась. Видимо, шуток она не понимает."
    #         "— Забудь."
    #         $ humorousPoints += 1
    # #похоже способные за исключением возможности работать с нейроинтам нихуя неспособные (исходя из третьей главы) так что это придется переделать

    # "В детстве мне очень нравился сериал про паренька, который отличался высокой внимательностью и дедуктивными способностями. "
    # "Но это прикидывался дураком и называл себя ясновидцем, выдавая свои догадки за подсказки духов. Мне очень импонировала его модель поведения и довольно часто у меня это тоже проявлялось. Вот и сейчас тоже. "

    # "Не думаю, что стоит ей говорить, что я тоже посмотрел немало аниме и её поведение слишком заштампованно. Знаю я этих цундере - обидится ещё. Лучше буду дурачком-ясновидцем."

    # yu "— Орихалк, приём, это Чайка."
    # "— Орихалк на связи. Чайка, ты жива? Доложи ситуацию."
    # yu "— Я в порядке, подлодка потеряна. Я нахожусь на спасательной шлюпке. Требуется эвакуация."
    # r "— Слава богу ты цела. По твоим координатам направлен транспортник. Жди на месте."
    # yu "— Куда я денусь-то, с подводной лодки."
    # r "— Ты ж сказала, что подлодка потеряна..."
    # yu "— Забей, выражение такое... В общем жду. Конец связи."
    # yu "— Эх, скорее бы на базу. Небось Мария там волнуется."
    # "— Кто такая Мария?"
    # yu "— Сумасшедший учёный нашей базы и, по совместительству моя подруга."
    # "— В смысле сумасшедший учёный?"
    # yu "— Она является главой научного отдела и очень любит придумывать странные вещи. Вы с ней чем-то похожи."
    # "— Тогда, думаю, мы подружимся."
    # "— ----------> Тут их забирает генерал Ганц"