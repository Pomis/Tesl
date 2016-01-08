init:
    define ra = Character('Голос из рации', color="#e4e4e4")
    define pi = Character('Пилот', color="#e1e4e1")
    define ma = Character('Мария', color="#faf0b8")
    define sl = Character('Слава', color="#faf0b8")
    define golos = Character('Голос', color="#f8349f")
    define regf = Character('Офицер', color="#f8349f")
    image bg entrace = "images/entrace.jpg"
    image bg mountains = "images/mountains.jpg"
    image bg mountains middle = "images/mountains-mid.png"
    image bg mountains forward = "images/mountains-front.png"
    image bg hangar = "images/hangar.png"

    image marie smiling = "images/marie-smiling.png"
    image marie shamed = "images/marie-shamed.png"


label warBase:
    scene bg mountains onlayer background
    show bg mountains forward onlayer forward at center
    show bg mountains middle onlayer middle
    $ camera_move(0, -2000, 0, 0, 0)
    $ camera_move(0, -2000, 1000, 0, 10, "easein")
    "Мы подлетали к заснеженным горным вершинам и постепенно снижали скорость"
    "Неужели они собираются приземлиться на гору?"
    "Генерал достаёт свою необычную рацию и громогласно заявляет:"
    gen "— Генерал Ганц запрашивает разрешение на посадку."
    ra "— Подтвердите ваши идентификационные данные."
    "Генерал прикасается к датчику на рации."
    "Хм, а я и не думал, что нейроинтерфейсом могут управлять люди его возраста."
    ra "— Идентификация пройдена. Приземляйтесь, генерал Ганц!"
    "Куда мы приземлимся???"
    hide bg onlayer forward
    hide bg onlayer middle
    scene bg entrace onlayer background
    "Вертолёт медленно приближался к горе. Вскоре я заметил небольшую металлическую поверхность шестиугольной формы."
    "Мы приземлились на эту платформу. Спустя несколько секунд платформа плавно провалилась в гору. Это что, лифт для вертолётов?"
    pi "— Ну как тебе наш въезд? {w}А-ха-ха-ха!"
    "— У меня бы язык не повернулся назвать это въездом..."
    if inferno==False:
        "Юминг тем временем вообще уснула. Как вообще можно было уснуть в такой ситуации? Мы влетели на вертолёте в горный лифт!"
    scene bg hangar onlayer background
    $ camera_move(8000,0,472,0)
    "Наконец, лифт закончил движение. Мы оказались в просторном ангаре. {w}Интересно, а сопровождающие вертолёты куда приземлились?"
    gen "— Сперва тебе нужно пройти регистрацию и медицинское обследование. Тебя сопроводят."
    "— Хм, понятно."
    show marie smiling at left onlayer background
    if inferno==True:
        ma "Генерал, а где Юминг?"
        $ camera_move(-8000,0,472,0, 1.5, "easeout")
        "Услышав это имя, я сразу напрягся и развернулся в сторону голоса"
        "Им оказалась молодая девушка в белом халате с обеспокоенным лицом"
        #Рисунок обеспокоенной Марии
        gen "-Спасательная операция ещё ведётся. Скоро мы её найдём, не беспокойся."
        gen "-Лучше пока покажи новичку базу."
    "Генерал развернулся и удалился."
    if inferno==False:
        "ОБНИМАШКИИИИИИИИИ!"
        "Откуда-то выбежало белое существо и с криками бросилось на Юминг"
        "Белым существом оказалась симпотичная блондинка в белом халате"
        yu "Мария, может перестанешь так делать? Ты уже взрослый человек..."
        ma "А взрослые не могут обниматься?"
        yu "Могут, но... Хотя забей"
        #Наверное нужен будет рисунок их обнимашек.
    
    ma "— Меня зовут Мария. Добро пожаловать на базу TESL."
    "— Как ты назвала это место?"
    ma "— И мне очень приятно познакомиться. Это база входящая в комплекс TESL — последняя надежда на защиту человечества от нападений Инферно."
    "— Сколько гордости-то! Ладно, меня зовут [playerName]."
    ma "— Договоришься у меня. За мной иди."
    "— Ладно, ладно..."
    if inferno==False:
        yu "Я пока отдохну, пусть Мария тебе всё покажет."
    "Мария направилась в сторону одного из выходов из ангара. {w}Почему она так быстро идёт?"
    "— Что, ещё один лифт?"
    ma "— Ну же, заходи!"
    "Что мне остаётся делать..."
    ma "— Наша военная база распределена по всей горе.{w} Разные узлы расположены в разных частях горы. Это позволит системе функционировать в случае, когда часть будет уничтожена."
    "— А что тут у вас вообще есть?"
    ma "— У нас лучший подводный флот в дальневосточном регионе! Ну, это военная база, особо интересных вещей, как лаборатории исследования природы Инферно тут нет..."
    ma "— Я хочу попасть на исследовательскую базу в Сибири, но доступ туда почти на 100 процентов закрыт даже для таких гениев, как я."
    "— В чём твоя гениальность?"
    "Так, стоп, это не важно. "
    ma "— Начнём с того, что..."
    "Кажется, её уже не остановить. "
    ma "— Я изобрела улучшенный цезиевый снаряд для поражения лавовых гигантов!{w} При контакте встроенные датчики рассчитывают максимально эффективное распределение цезия по площади цели и взрывает снаряд так, что ..."
    "— Ладно, я понял. А почему цезий?"
    ma "— Не перебивай меня. Лава - В абсолютом большинстве случаев это базальтовые породы, наполовину состоящие из диоксида кремния."
    ma "— А так как диоксид кремния вещество кислотное, эффективнее всего оно будет разлагаться щелочами. А при реакции с водой цезий производит сильнейшую щелочь."
    "Боже... "
    ma "— Так-с, мы приехали. Кстати, как будет вернее назвать это? Лифт или метро? Он двигается не только вертикально!"
    "— Лифт. В метро вагоны."
    "Зачем я подыгрываю ей?"
    ma "— Так, тебе в кабинет R01. Вперёд. Я тебя даже подожду."
    "Мария присела на скамейку рядом с кабинетом, а я стучу в дверь."
    golos "— Входите."
    regf "— А. Я кажется припоминаю, [playerFullName]? Большинство бумаг уже заполнено. Вам нужно только подписать."
    "— За что я расписываюсь?"
    regf "— Ну, кроме очевидного, что ты теперь солдат и подчиняешься приказам командования, ты теперь не имеешь права работать в государственных структурах."
    regf "— По Берлинскому соглашению, ни один, даже бывший сотрудник комплекса не может работать ни на одно государство ООН."
    "— А что меня вообще ждёт?"
    regf "— Краткий семидневный инструктаж. Потом экзамен, где тебя направят на пилотирование, или ещё куда-то. Узнаешь."
    "Я пробежался глазами по бумагам, в целом, ничего особенного, да и как-то без разницы. "
    regf "— Распишитесь здесь, здесь... И здесь. И поставьте отпечаток пальца рядом."
    "— Что теперь?"
    regf "— Вам всё объяснят. Вообще, к таким как ты максимально хорошее отношение. \"Способные\" на вес золота, без вас войну мы никогда не выиграем."
    "Меня там за дверью Мария ждёт, не хочу её заставлять долго меня ждать. Она хоть и немного надменная, но, вроде бы, хороший человек."
    "— Ну ладно, я пойду...{w} До свидания."
    regf "— Бывайте..."
    "Я покинул кабинет регистрации."
    ma "— Ну-с, как?"
    "— Да ничего особенного, всё ожидаемо."
    ma "— Тоже так считаю! А некоторые так удивляются!"
    "— Не наскучило меня ждать?"
    ma "— А что мне остаётся? Мне сам генерал Ганц приказал сопровождать тебя первый день. Выбора нет, понимаешь..."
    "— А кто такой, этот Ганц? По его виду, можно сказать, что он успел побывать во всех возможных боевых ситуациях. "
    ma "— Да он 20 лет служил в Российской армии. А сейчас он командует всеми боевыми операциями, проводимыми нашей базой. "
    ma "— У него редкое сочетание навыков. Он управляет нейроинтерфейсом и обладает огромным боевым опытом. {w}Большинство \"способных\" — люди в возрасте от 16 до 25 лет. А Ганцу 40."
    "— И как это ему помогает в командовании боевыми операциями?"
    ma "— Специальные устройства позволяют получать все данные, поступаемые с боевых единиц и представлять в удобном для восприятия через нейроинтерфейс виде."
    ma "— Короче говоря, только он может сразу увидеть всю картину боя целиком и принять лучшее решение."
    "— Знаешь, у меня немного странный вопрос... {w}А зачем они вообще нападают?"
    ma "— Есть информация, что мстят нам за уничтожение города. Я не знаю, правда ли это. Да и как-то не пыталась узнать."
    ma "— Политика — не моё."
    ma "— Ладно, пошли уже? Что тебе показать?"
    menu:
        "— Где я буду жить?":
            jump goHome
        "— Чем тут можно заниматься в свободное время?":
            ma "— Ну... Я всё свободное время в лаборатории провожу..."
            ma "— Если ты развлечений ищешь, то ты не по адресу."
            ma "— Здесь даже пива не достать... Эх..."
            "Тяжело представить эту мадам за бутылкой пива."
            "— А чем занимаются остальные?"
            ma "— Обучение, тренировки. Тут нет бездельников!"
            "— Какое ещё обучение?"
            ma "— Ну ты же понимаешь, что здесь есть люди, которым по 15 лет? Да и русскому учим заодно. Официальный язык базы русский, как ты уже понял."
            ma "— Но тут довольно много китайцев и японцев."
            "— Никак нельзя пропустить это обучение?"
            ma "— А как ты собрался воевать? {w}Да и это же всего лишь неделя! Потерпи!"
            "А ведь логично, что никто не доверит необученным бойцам дорогостоящее оборудование."
            "— А каким оружием обладает наш враг?"
            ma "— Я бы рассказала... Но вам этим будут выносить мозг всё последующее время на военной базе. Могу лишь только сказать, что мы очень мало знаем."
            ma "— И наша база знаний увеличивается после каждого сражения."
            jump goHome
        "— Покажи, над чем ты сейчас работаешь?":
            # Мария очень любит рассказывать, особенно о научной теме и о своей работе. Всякий раз когда игрок спрашивает её об этом, набираются поинты.
            $ mariePoints += 1
            $ visitedLab = True
            show marie shamed at left onlayer background
            "Мария немного покраснела. Видно, не ожидала такого вопроса."
            show marie smiling at left onlayer background
            "Далее, невозмутимым тоном стала рассказывать:"
            ma "— Сейчас я работаю над оптимизацией оборонительной системы этой базы. {w}Я использую усовершенствованный мною алгоритм Дейкстры для управления ботами, торпедами и ракетами."
            ma "— А то на прошлых учениях несколько ботов минуту не могли покинуть доки. А часть торпед преодолела расстояние вдвое больше минимального из-за опасности столкновения с другими торпедами или ботами."
            "Тем временем мы ехали вглубь горы на лифте."
            "Прибыли в необыное футуристичное помещение."
            ma "— Так... Мы приехали. Я покажу тебе ботов! Их спроектировали на исследовательской базе, а я переработала их искусственный интеллект."
            "— И как эти малявки могут сражаться?"
            ma "— Они оснащены самым передовым оружием! А благодаря своему размеру они почти незаметны для подводных титанов и их свиты."
            ma "— Вот только использовать их мы можем только для обороны военной базы. У нас их всего около пятидесяти. Расчётные боевые потери ботов при сражении близки к 90 процентам."
            ma "— Так что они нам сейчас нужнее здесь. "
            "— А почему бы не производить их тысячами?"
            ma "— Неоправданно дорого, говорят."
            "— Можешь показать алгоритм?"
            ma "— Показать? Хм... Могу нарисовать! "
            "Она старательно разрисовывала ближайшую доску, а я запоминал. Может, я и не пойму это, но память у меня хорошая. Солью врагам, так сказать."
            "Хотя, немного даже жалко."
            "Посмотрим."
            "Я всегда так откладывал решения — \"посмотрим\"."
            "— Честно говоря, я ничего не понял..."
            ma "— Да никто не понимает..."
            ma "— Что-то ты какой-то уставший..."
            jump goHome
    jump  ch3day1
label goHome:
    "Мне уже надоело слушать Марию, хотелось бы узнать, где я буду жить."
    "Едва заметно вздохнув она встала и вызвала лифт."
    ma "— Пошли, покажу..."
    "Она нажала на экран в лифте, выбрала какой-то элемент. Лифт сразу же начал набирать скорость."
    "И правда, чем-то похоже на метро."
    "Может, шумом? {w}Зато быстро. "
    ma "— Это жилой корпус новобранцев. Твоя комната N04. Найдёшь, надеюсь."
    "— Найду... И сразу пойду спать."
    if visitedLab == True:
        ma "— Зайдёшь ко мне в лабораторию как-нибудь на днях?"
        menu:
            "– Да, почему бы и нет":
                $ promisedMarie == True
                ma "— Хех, буду ждать!"
                ma "— Ладно, тогда увидимся!"
            "— Нет, я не успею, наверное...":
                ma "— Ну и зануда."
                ma "— Ладно, я пошла..."
    hide marie with dissolve
    "Я вошёл в свою комнату. Довольно тесноватая, как в общежитии. Искусственное окно. Соседей не было, хотя стояло две двухъярусные кровати."
    if inferno == True:
        "Как-то совсем не хочется проходить этот семидневный инструктаж."
        "Хотя... Возможно, это будет интересно. Я же никуда не спешу со своими планами?"
    else:
        "Интересно, а что будет на этом инструктаже? {w}Чему нас научат?"
    "Тут открылась дверь и в комнату зашёл парниша. На вид ровесник."
    sl "— О, новый сосед! Какими судьбами? Меня кстати Славой зовут!"
    "— Да, думаю, такими же, как и ты? Я [playerName]."
    "Я оценивающе оглядел его с ног до головы."
    sl "— Приятно познакомиться! Завтра наконец-то начнутся занятия! Я уже две недели жду. А ты очень вовремя прибыл!"
    "— Почему именно так?"
    sl "— Ну, \"способных\" новобранцев очень мало, вот и занятия проводят только лишь каждый месяц. Или как наберётся хотя бы 5-6 человек."
    sl "— Я только с тренировок... Я в душ и спать!"
