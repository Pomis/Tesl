define r = Character('Голос из рации', color = "#f45678")
label rootSoldier:

    
    "-Ну я по большей части скорее кодер, чем техник, но раз это требует лишь базовых познаний думаю справлюсь."
    "C этими словами я принялся за работу."
    "Конструкция рации не была похожа на что-либо, что бывало у меня в руках, но по каким-то непонятным причинам я понимал, что и как делать."
    "Это больше напоминало сотворение предмета искусства, чем починку технической новинки. Какие-то волокна, рисунки. Видимо за основу взяты технологии этих самых Инферно"
    "За починкой рации я и сам не заметил как моя обида на неё куда-то улетучилась. Достаточно сложно обижаться на столь несерьёзного человека. Да и подобные вещи всегда успокаивали меня. Помнится в детстве я мог часами собирать пазлы или налаживать какую-нибудь бытовую технику. "
    "Когда я повзрослел, то это уже перестало меня так завлекать, но то чарующее спокойствие до сих пор проявляется при погружении в подобное занятие."
    "Надо признать, что в какой-то степени я благодарен этой девушке за столь грубое вмешательство в мою жизнь. "
    "Мне всегда нужен был какой-то пинок, чтобы что-то поменять в моей жизни, ибо она быстро обрастала какой-то рутинной, а сам изменить я ничего не мог. Даже не совсем не мог - скорее не хотел. "
    "Не сказать, что моя жизнь меня не устраивала, но определённо мне хотелось большего. Но самостоятельно я не был готов прикладывать усилий, ибо считал, что раз сейчас мне нормально, то результат не будет стоить потраченных усилий, ведь мне будет лишь чуть лучше, чем сейчас."
    "Может я просто не мог полностью наслаждаться успехами и горевать над потерями? Да, скорее всего так и было."
    yu "-Эй, ты там не уснул? Скоро закончишь?"
    "Юминг вытащила меня из размышлений."
    "-Да, уже всё."
    "Задумавшись, я и сам не заметил, как закончил ремонт."
    "Она взяла в руки передатчик, послышался характерный треск. Вот только не из динамиков, а прямо в ушах. Да что это за хрень такая?"
    yu "- Орихалк, приём, это Чайка."
    "-Орихалк на связи. Чайка, ты жива? Доложи ситуацию."
    yu "-Я в порядке, подлодка потеряна. Я нахожусь на спасательной шлюпке. Требуется эвакуация."
    r "По твоим координатам направлен транспортник. Жди на месте."
    yu "-Куда я денусь-то, с подводной лодки."
    r "-Ты же сказала, что подлодка потеряна..."
    yu "-Забей, выражение такое... В общем жду. Конец связи."

    yu "-Эх, скорее бы на базу. Небось Мария там волнуется."
    "-Кто такая Мария?"
    yu "-Сумасшедший учёный нашей базы и, по совместительству моя подруга."
    "-В смысле сумасшедший учёный?"
    yu "-Она является главой научного отдела и очень любит придумывать странные вещи. Вы с ней чем-то похожи."
    "-Тогда, думаю, мы подружимся."
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
    yu "— Посмотрим, кто быстрее, подводный титан, или вертолёты Ка-60."
    $ heardAboutTitan = True
    "— Такие вообще существуют?"
    "— Титан? "
    yu "— Да, с таким мы сражались. Эта тварь сломала мою любимую подводную лодку!"
    "— Титан значит..." with bloodrage
    yu "— Ой... Прости, забыла совсем."
    "— Я найду и уничтожу каждого титана!"
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
            $ knowYumingRoom = True # Ключевая переменная для возоможности выхода на Юминг-рут. Нужно дать игроку ещё шанс получить этот True
            "— Разве это не секретная информация?"
            yu "— Само наше существование — секретная информация."
            "Юминг хитро улыбнулась."
        "Через пару мгновений она уже сладко спала."
        # bulat: Тут можно просто затухание экрана и переход
    

    jump warBase

    # yu "—Если у тебя есть небольшие познания в технике, то, будучи \"способным\", ты спокойно сможешь починить практически любую вещь с подобной архитектурой. "
    # yu "—Я, к сожалению, гуманитарий."
    # "Высунув язык, она склонила голову и ткнула себя кулаком в макушку."
    # "-Ну я по большей части скорее кодер, чем техник, но раз это требует лишь базовых познаний думаю справлюсь."
    # "C этими словами я принялся за работу."
    # "Конструкция рации не была похожа на что-либо, что бывало у меня в руках, но по каким-то непонятным причинам я понимал, что и как делать."
    # "Это больше напоминало сотворение предмета искусства, чем починку технической новинки. Какие-то волокна, рисунки. Видимо за основу взяты технологии этих самых Инферно"
    # "За починкой рации я и сам не заметил как моя обида на неё куда-то улетучилась. Достаточно сложно обижаться на столь несерьёзного человека. Да и подобные вещи всегда успокаивали меня. Помнится в детстве я мог часами собирать пазлы или налаживать какую-нибудь бытовую технику. "
    # "Когда я повзрослел, то это уже перестало меня так завлекать, но то чарующее спокойствие до сих пор проявляется при погружении в подобное занятие."
    # "Надо признать, что в какой-то степени я благодарен этой девушке за столь грубое вмешательство в мою жизнь. "
    # "Мне всегда нужен был какой-то пинок, чтобы что-то поменять в моей жизни, ибо она быстро обрастала какой-то рутинной, а сам изменить я ничего не мог. Даже не совсем не мог - скорее не хотел. "
    # "Не сказать, что моя жизнь меня не устраивала, но определённо мне хотелось большего. Но самостоятельно я не был готов прикладывать усилий, ибо считал, что раз сейчас мне нормально, то результат не будет стоить потраченных усилий, ведь мне будет лишь чуть лучше, чем сейчас."
    # "Может я просто не мог полностью наслаждаться успехами и горевать над потерями? Да, скорее всего так и было."
    # yu "-Эй, ты там не уснул? Скоро закончишь?"
    # "Юминг вытащила меня из размышлений."
    # "-Да, уже всё."
    # "Задумавшись, я и сам не заметил, как закончил ремонт."
    # yu "-Какой-то ты странный."
    # menu: 

    #     "Кто бы говорил!":
    #         "-Кто бы говорил... "
    #         "Буркнул я и протянул рацию."
    #         "-Сама-то как снег на голову рухнула и ещё что-то требуешь. Ты здесь не одна, кто попал в тяжёлую ситуацию."
    #         "Не говоря уже о том, что именно по твоей вине мы тут чалимся..."
    #         "Я всегда был человеком, который найдёт причину поворчать. Даже вернее будет сказать повод."
    #         "А когда от меня ещё что-то так нагло требуют, выгоняя из зоны комфорта, то тут уже грех не поворчать."

    #     "-Какой есть, такой есть":
    #         "-Какой есть, такой есть"
    #         "Я улыбнулся я и протянул рацию."
    #         yu "-Чего это ты улыбаешься? Какую-то пошлость вообразил?"
    #         "Она обхватила себя руками."
    #         "-Слушай, ты аниме много смотришь что ли?"
    #         yu "-Да, откуда ты узнал?"
    #         "Я решил подшутить над ней"
    #         "-Я ясновидец просто."
    #         yu "-Ясновидец? Такого таланта среди способных я замечала."
    #         "Юминг серьёзно задумалась. Видимо, шуток она не понимает."
    #         "-Забудь."
    #         $ humorousPoints += 1
    # #похоже способные за исключением возможности работать с нейроинтам нихуя неспособные (исходя из третьей главы) так что это придется переделать

    # "В детстве мне очень нравился сериал про паренька, который отличался высокой внимательностью и дедуктивными способностями. "
    # "Но это прикидывался дураком и называл себя ясновидцем, выдавая свои догадки за подсказки духов. Мне очень импонировала его модель поведения и довольно часто у меня это тоже проявлялось. Вот и сейчас тоже. "

    # "Не думаю, что стоит ей говорить, что я тоже посмотрел немало аниме и её поведение слишком заштампованно. Знаю я этих цундере - обидится ещё. Лучше буду дурачком-ясновидцем."

    # yu "-Орихалк, приём, это Чайка."
    # "-Орихалк на связи. Чайка, ты жива? Доложи ситуацию."
    # yu "-Я в порядке, подлодка потеряна. Я нахожусь на спасательной шлюпке. Требуется эвакуация."
    # r "-Слава богу ты цела. По твоим координатам направлен транспортник. Жди на месте."
    # yu "-Куда я денусь-то, с подводной лодки."
    # r "-Ты ж сказала, что подлодка потеряна..."
    # yu "-Забей, выражение такое... В общем жду. Конец связи."
    # yu "-Эх, скорее бы на базу. Небось Мария там волнуется."
    # "-Кто такая Мария?"
    # yu "-Сумасшедший учёный нашей базы и, по совместительству моя подруга."
    # "-В смысле сумасшедший учёный?"
    # yu "-Она является главой научного отдела и очень любит придумывать странные вещи. Вы с ней чем-то похожи."
    # "-Тогда, думаю, мы подружимся."
    # "-----------> Тут их забирает генерал Ганц"