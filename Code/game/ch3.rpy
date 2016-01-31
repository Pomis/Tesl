init:
    define ra = Character('Голос из рации', color="#e4e4e4")
    define pi = Character('Пилот', color="#e1e4e1")
    define ma = Character('Мария', color="#faf0b8")
    define sl = Character('Слава', color="#faf0b8")
    define stranger = Character('Странный', color="#8c8c8c")
    define str_nvl = Character('Странный', color="#8c8c8c", kind=nvl)
    # bulka: Цвет можно заменить, просто скопировал, имя временное, пока не придумал
    define golos = Character('Голос', color="#f8349f")
    define regf = Character('Офицер', color="#f8349f")
    image bg entrace = "images/entrace.jpg"
    image bg mountains = "images/mountains.jpg"
    image bg mountains middle = "images/mountains-mid.png"
    image bg mountains forward = "images/mountains-front.png"
    image bg hangar = "images/hangar.png"
    image bg room = "images/room.jpg"
    image bg yuming room = "images/yu-room.png"
    image chess = "images/chess.jpg"
    image chess hovered = "images/chess-hovered.jpg"
    image bg coridor = "images/coridor.png"
    image bg coridor second = "images/coridor-e.png"

label warBase:
    hide yuming onlayer forward
    hide boat onlayer middle
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
    show marie smiling at left2 onlayer middle
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
        $ camera_move(-8000,0,472,0, 1.5, "easeout")
        "Откуда-то выбежало белое существо и с криками бросилось на Юминг."
        "Белым существом оказалась симпотичная блондинка в белом халате."
        yu "— Мария, может перестанешь так делать? Ты уже взрослый человек..."
        "Хотя Юминг так и говорила, было видно, что она сама далеко не против."
        "Хотя она этого и стеснялась."
        ma "— А взрослые не могут обниматься?"
        yu "— Могут, но... Хотя, забей."
        # bulka: Наверное нужен будет рисунок их обнимашек.
        yu "— Ладно, я побежала, надо написать отчёт по операции."
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
    hide marie onlayer middle
    hide bg onlayer background
    scene bg lift with dissolve
    "Что мне остаётся делать..."
    show marie smiling at center2
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
    # bulka: Он же только прилетел. Когда успели-то?
    # pomis: Как только за ним вылетели, начали бумажную работу
    # bulka: А как же великая русская бюрократия?
    # pomis: А это не совсем Россия
    # bulka: Все русскоязычные, но это не Россия. Ок.
    regf "— Ну, кроме очевидного, что ты теперь солдат и подчиняешься приказам командования, ты теперь не имеешь права работать в государственных структурах."
    regf "— По Берлинскому соглашению, ни один, даже бывший сотрудник комплекса не может работать ни на одно государство ООН."
    "— А что меня вообще ждёт?"
    regf "— Краткий семидневный инструктаж. Потом экзамен, где тебя направят на пилотирование, или ещё куда-то. Узнаешь."
    "Я пробежался глазами по бумагам, в целом, ничего особенного, да и как-то без разницы. "
    regf "— Распишитесь здесь, здесь... И здесь. И поставьте отпечаток пальца рядом."
    "— Что теперь?"
    regf "— Вам всё объяснят. Вообще, к таким как ты максимально хорошее отношение. \"Способные\" на вес золота, без вас войну мы никогда не выиграем."
    regf "— Кстати. У вас уровень доступа А. Это даёт вам право посещать учебные кабинеты, ангар, стрельбище, или как его у нас называют, тир. В остальные помещения, такие, как лаборатория, командный центр, нужно приглашение руководства."
    "Меня там за дверью Мария ждёт, не хочу её заставлять долго меня ждать. Она хоть и немного самоуверенная, но, вроде бы, хороший человек."
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
    if wantToAskAboutSignal == True:
        "— Кстати... Совсем забыл спросить... А что за сигнал был в передатчике, на который Инферно слетелись как акулы на кровь?"
        ma "— О чём ты вообще?"
        "— Юминг сказала ты знаешь. Во время операции, в которой я потерпел кораблекрушение, передатчики были установлены где-то в корабле."
        ma "— Ну и зверство! Вы что, были наживкой? Зачем ты в этом участвовал? Я думала, ты умнее."
        "— Ты издеваешься, что ли? Я не знал об этом! У меня там вся семья погибла!"
        "Мария виновата опустила глаза."
        ma "— Ясно..."
        ma "— Но я правда ничего об этом не знаю. А Юминг считает, что я знаю всё, вот и сказала так."
        ma "— Ну по сравнению с ней... Я же действительно всё знаю."
        # bulka: О, а вот тут рядом можно намутить переходик в инферно. Продолжаем копать по этому поводу, узнаём, что люди зло/нами воспользовались ради всеобщего блага/ещё чё и решаем быть за инферно.
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

            show marie shamed at center2
            "Мария немного покраснела. Видно, не ожидала такого вопроса."
            show marie smiling at center2
            "Далее, невозмутимым тоном стала рассказывать:"
            ma "— Сейчас я работаю над оптимизацией оборонительной системы этой базы. {w}Я использую усовершенствованный мною алгоритм Дейкстры для управления ботами, торпедами и ракетами."
            ma "— А то на прошлых учениях несколько ботов минуту не могли покинуть доки. А часть торпед преодолела расстояние вдвое больше минимального из-за опасности столкновения с другими торпедами или ботами."
            "Тем временем мы ехали вглубь горы на лифте."
            show bg laba opened
            "Прибыли в необыное футуристичное помещение."
            ma "— Так... Мы приехали. Я покажу тебе ботов! Их спроектировали на исследовательской базе, а я переработала их искусственный интеллект."
            "— И как эти малявки могут сражаться?"
            ma "— Они оснащены самым передовым оружием! А благодаря своему размеру они почти незаметны для подводных титанов и их свиты."
            ma "— Вот только использовать их мы можем только для обороны военной базы. У нас их всего около пятидесяти. Расчётные боевые потери ботов при сражении близки к 90 процентам."
            ma "— Так что они нам сейчас нужнее здесь. "
            "— А почему бы не производить их тысячами?"
            ma "— Неоправданно дорого, говорят."
            # bulka: Тут условие если инферно тру. Ибо в солдатском руте юзлесс
            if inferno == True:
                "— Можешь показать алгоритм?"
                ma "— Показать? Хм... Могу нарисовать! "
                "Она старательно разрисовывала ближайшую доску, а я запоминал. Может, я и не пойму это, но память у меня хорошая. Солью врагам, так сказать."
                "Хотя, немного даже жалко."
                "Посмотрим."
                "Я всегда так откладывал решения — \"посмотрим\"."
                "— Честно говоря, я ничего не понял..."
                ma "— Да никто не понимает..."
            else:
                "— Почему у тебя на столе разобранный пистолет?"
                ma "— Эм. Мне сказали, что...{w} Не важно!"
                "— Что внутри конфетка?"
                ma "— Да нет же! Я пыталась починить, но только сильнее сломала его!"
                "— Можно посмотреть?"
                "Я взял в руки часть пистолета, и тут же получил ладонью по рукам."
                ma "— Не трожь!"
                "— Странно это всё!"
                ma "— Ты на военной базе, расположенной внутри горы, у тебя способность управлять нейроинтерфейсом, а странным тебе кажется только это?"
                "— Ну да, как-то так... "
            ma "— Что-то ты какой-то уставший..."
            jump goHome
label goHome:
    "Мне уже надоело слушать Марию, хотелось бы узнать, где я буду жить."
    "Едва заметно вздохнув она встала и вызвала лифт."
    scene bg lift with dissolve
    show marie smiling at center2 
    ma "— Пошли, покажу..."
    "Она нажала на экран в лифте, выбрала какой-то элемент. Лифт сразу же начал набирать скорость."
    "И правда, чем-то похоже на метро."
    "Может, шумом? {w}Зато быстро. "
    scene bg coridor with dissolve
    show marie smiling at right
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
                $ liePoints += 1
                ma "— Ну и зануда."
                ma "— Ладно, я пошла..."
    hide marie with dissolve
    scene bg room
    "Я вошёл в свою комнату. Довольно тесноватая, как в общежитии. Искусственное окно. Соседа не было, хотя стояло две кровати."
    if inferno == True:
        "Как-то совсем не хочется проходить этот семидневный инструктаж."
        "Хотя... Возможно, это будет интересно. Я же никуда не спешу со своими планами?"
    else:
        "Интересно, а что будет на этом инструктаже? {w}Чему нас научат?"
    "Тут открылась дверь и в комнату зашёл парниша. На вид ровесник."
    show slava serious at left:
        xalign -0.3 yalign 0.0
        ease 1.0 xalign 0.1   
    sl "— О, новый сосед! Какими судьбами? Меня кстати Славой зовут!"
    "— Да, думаю, такими же, как и ты? Я [playerName]."
    "Я оценивающе оглядел его с ног до головы."
    sl "— Приятно познакомиться! Завтра наконец-то начнутся занятия! Я уже две недели жду. А ты очень вовремя прибыл!"
    "— Почему именно так?"
    sl "— Ну, \"способных\" новобранцев очень мало, вот и занятия проводят только лишь каждый месяц. Или как наберётся хотя бы 5-6 человек."
    sl "— Я только с тренировок... Я в душ и спать!"
    hide slava with dissolve
    menu:
        "Дождаться Славу":
            "Пока осмотрюсь в комнате. Интересное искусственное окно. И почему в нём запущен браузер?"
            "Судя по всему, это 4 монитора, подключенных к компьютеру. Интересное решение."
            jump ch3day1
        "Прогуляться по жилому комплексу":
            $ seenChessGame == True
            scene bg coridor with dissolve
            "Я не спеша вышел из комнаты, осмотрелся по сторонам. И что тут есть?"
            "Ни души в коридоре. Дошёл до конца, поднялся по лестнице на следующий этаж."
            scene bg coridor second with dissolve
            "Может тут хоть кто-то есть... "
            "На диванчике расположился странный парень с забавной причёской. Он разложил на шахматной доске фигуры в случайном порядке и перемещал их."
            show tenko thinking at right
            "Или не в случайном порядке? Кто знает, что у него в голове, может это ещё один гений?"
            if knowYumingRoom == True:
                "Комната Е01, Е02..."
                "А, точно. Надо заглянуть к Юминг.{w} Или потом? Всегда успею."
                menu:
                    "Зайти к Юминг":
                        hide tenko
                        # TODO: Тут сделаю картинку с дверью в Е09
                        "Та-а-ак, комната Е09. Нерешительно стучу в дверь. {w}Тук.{w} Тук-тук."
                        "Открывай давай!"
                        "Да чего я боюсь? Стукнул по двери посильнее."
                        "А может тут есть замок?"
                        yu "— Это ещё кто в такое время?"
                        "— А... Это я{w}, [playerName]."
                        show yuming at center
                        "Юминг открыла мне дверь и пригласила жестом внутрь."
                        "— Тебе идёт эта смешная пижамка!"
                        yu "— Ну а как иначе?"
                        # bulka: Это неправильная цундере и она даёт неправильный мёд! Или цундере-Юминг потеряна для нас навсегда среди коммитов и правок?
                        call inYumingRoom from _call_inYumingRoom_1
                        "К тому времени, Слава уже спал богатырским сном. Я плюхнулся в кровать и отключился."
                        
                    "Подойти к гроссмейстеру.":
                        jump grossmeister
            else:
                jump grossmeister

            # Pomis: Если знает где живёт Юминг — выбор, идти к ней, или дальше гулять
            # Выбор обоснован тем, что он мог бы зайти к ней и в любой другой день. Печалька заключается в том, что другого раза не будет
            # Если просто гуляет, то играет с Жориком в шахматы и выигрывает.
            # bulka: Думаю херачить шахматную игру будет излишним, но почему бы не захерачить шахматную задачку? Аля несколько вариантов и после каждого свой результат. Аля гг сыграл сейвово, защитив короля, соперник херачит фразу Лелуша: "Если не двинется король, окружение тоже останется на месте." Если выбрал агрессию, то чё-нибудь аля "Выигрывает тот, кто сумеет захватить инициативу." Гг сыграл умеренно - ещё что-нибудь. Причём, чтобы в одном варианте гг проигрывал, в другом выигрывал, в третьем ничья/игра продолжалась. З.ы. Я вот тут это понаписывал, а потом понял, что это наш тупой координатор\ А мне сначала показалось, что это просто загадочный парень и немного пафоса не повредит( Ладно, пофигу, пусть будет - мб потом во что-то превращу. Всё-таки такому мужлану шахматы не идут, как не посмотри. 

label grossmeister:
    
    "Я подошёл к этому парню и стал внимательно наблюдать за его действиям, пытаясь найти какую-то закономерность."
    "— В чём смысл?"
    $ playedChess = True
    stranger "— Смысл? В хаосе. А я тебя никогда не видел. Хм. Новичок? Нет. Тогда бы ты был в корпусе новобранцев..."
    "Какой-то он не такой. Конечно, ещё когда я его увидел, мне он показался странноватым, но всему же должна быть мера..."
    if inferno == True:
        "Надо к нему приглядеться. Такие зачастую самые опасные, ибо никогда не знаешь, что от них ожидать..." 
    stranger "— Ладно, не важно. Не хочешь сыграть партию?"
    "— А почему бы и нет? Давай."
    "В детстве я очень любил шахматы, хотя и очень редко выигрывал. Когда я стал постарше, я даже всерьёз занимался ими, но из-за того, что не любил изучать теорию и только практиковался, особых успехов я не добился. Из-за этого, собственно, я их и забросил."
    "Однако, играть я ещё не разучился."
    "Этот странный парень не был из тех, кто долго думает, но при этом каждый ход был продуманным."
    "Хотя непохоже, что у него был большой опыт."
    scene chess with dissolve
    nvlc "В итоге, мы пришли к такой позиции."
    str_nvl "— И как же ты поступишь?"
    nvlc "У меня было три варианта:\n
        Первый - срубить слоном коня, чтобы разрубить к чертям этот гордиев узел.\n
        Второй - напасть конём, чтобы сделать то же самое через ход, только с выгодным разменом.\n
        Третий - пойти вперёд королём, чтобы забрать беззащитного слона следующим ходом."
    hide nvl
    $ result = renpy.imagemap("images/chess.jpg", "images/chess-hovered.jpg", [(786, 150, 853, 215, "first"), (720, 283, 788, 350, "second"), (855, 150, 922, 216, "third")], focus="imagemap")
    if result == "first":
        "Просто, быстро, напролом!"
        stranger "— А мне казалось ты поумнее будешь."
        if inferno:
            "Ты серьёзно считаешь, что я тут ошибся?"
        "Мы разменялись фигурами, и игра продолжилась в том же темпе."
        "Однако, из-за его преимущества в одну пешку мне пришлось несладко."
        if inferno:
            $ chesspoints = True
            $ antiTenkoPoints += 2
            "Как и планировал, я проиграл."
            "Не хочется показывать всю свою силу врагу, пускай даже и в шахматах. Пусть дальше смотрит на меня свысока."
        else:
            "В итоге, из-за своего поспешного решения я проиграл."
        stranger "— Ну что тут скажешь? Неплохо сыграно."
        if inferno == False:
            if agressionPoints>0:
                "Как же бесит! Ненавижу, когда на меня смотрят свысока!"
                "Так и хочется врезать по его наглой роже!"
            else:
                $ chesspoints = True
                "Глупо было ожидать победы после столького времени..."
        else:
            "Смейся, смейся. Посмотрим как ты будешь смеяться с ножом в спине."
    elif result == "second":
        $ strangerPoints += 1
        stranger "— Хахаха. Когда заглядываешься вдаль, ты упускаешь то, что вблизи."
        # bulka: Или "Когда засматриваешься вглубь, упускаешь то, что на поверхности." Хз какой вариант выбрать.
        # pomis: первый вариант мне больше по нраву
        $ chesspoints = True
        if inferno:
            if agressionPoints>3:
                $ chesspoints = False
                "Сууууууууууууууука. Ты ещё выпендриваться будешь. Тебе просто повезло, что я не заметил!"
            elif agressionPoints==3:
                "Только не говорите мне, что это пат. Вот же ублюдок! Он явно это просчитал. Видимо, он не так уж и глуп." 
            else:
                $ antiTenkoPoints += 1
                "Кажется это пат. Он явно это просчитал. Что ж, впредь буду с ним осторожнее."
        else:
            "А этот парень не так уж прост. Он явно специально подвёл к этой позиции."
        stranger "— Ну что тут скажешь? Неплохо сыграно."
    elif result == "third":
        $ wonchess = True
        $ strangerPoints += 2
        "— Как говорится, если не двинется король, то окружение тоже останется на месте."
        stranger "— Мдаааааа. Вот тут я немножко ошибся..."
        if inferno:
            if agressionPoints>2:
                "Немножко? Да ты запер половину своих фигур, идиот. Ты мне нарочно что ли поддаёшься?"
            else:
                $ chesspoints = True
                $ antiTenkoPoints += 1
                "Он явно мне поддавался. Видимо, надо было проиграть. Что ж, впредь буду с ним осторожнее."
        else:
            "Что-то он слишком слабо играет. Несмотря на то, что я давно не играл, вышло довольно легко."
        "Моя дальнейшая победа была очевидна. Я с лёгкостью расправился с остатками его фигур."
        stranger "— Ну что тут скажешь? Неплохо сыграно."
        # pomis: Я тут увидел отсылку к Hearthstone
        # bulka: Тут была отсылка к доте well played! Когда косячишь в доте так тоже поздравляют. 
        "— Спасибо за игру."
    hide tenko
    "Мы попрощались и я пошёл в свою комнату."
    scene bg coridor second with dissolve
    scene bg coridor with dissolve
    scene bg room with dissolve
    "К тому времени, Слава уже спал богатырским сном. Я плюхнулся в кровать и отключился."
    # bulka: Как мы узнаем на следующий день - это будет наш сосед слева (заменю павла на него), но прежде чем начать переделывать разговор с павлом, хочу приделать к этому персонажу очки аля как с женскими персонажами, но! никакого яоя или прочей лабуды. Просто в определённой ветке сюжета будет важно, считает ли он нас за дауна или нет (если просто и понятно). В инферно руте это поможет свалить к инферно/ещё что, ибо считая гг дауном, "странный" (имя ещё не придумал) не перестрахуется/не проследит за нами. Как это будет сочетаться с рутой людей пока хз. Мб в разговоре интерес проявит. Возможно, вместо очков хватит переменной, но опять же - пока хз.
    # bulka: Хочется ещё попросить прощения перед тем, кто будет переделывать эту лабуду с пробелами. Я, вроде, старался, и делал 4 пробела как у вас, но прошлый раз косяк проскочил. Кхер его знает, что будет сейчас.
    # bulka: Ну не может быть, что бы и в этот раз я не накосячил. Хочется предупредить, что количество очков агрессии сейчас точно выверено, так что аккуратнее с предыдущеми главами - это всё может полететь, если эти пойнты редактировать.
    jump ch3day1

# выделил отдельно, так как этот в этот кусок текста можно попасть в разных случаях — если знать комнату, и если соврать, что искал её
label inYumingRoom:
    $ visitedYumingRoom = True
    scene bg yuming room
    show yuming night at center2
    yu "— И нет, я не предложу тебе чай."
    "— Э... А при чём тут чай?"
    yu "— Ну-у... Обычно все ожидают от меня этого. Надоели со своими стереотипами, ненавижу чай."
    yu "— Я же тебе обещала показать разведданные? На, почитай."
    "Юминг швырнула мне в руки планшет с открытым документом."
    nvlc "*ДОКЛАД Р. АЙСДЕНА. ЗНАЧИМЫЕ ФИГУРЫ В СТРУКТУРЕ ИНФЕРНО. ARBOR MUNDI*"
    nvlc "Согласно данным, полученных от наших информаторов, общественный строй Инферно представляет собой строго консервативное общество, придерживающееся авторитаризма. Каждый, кто находится ниже в звании, обязан подчиняться тому, кто выше. Мы не уверены, относится это только к военным или к каждому. Однако, высокого звания очень легко лишиться, приняв одно неверное решение. Как они поднимают своё звание, нам пока неизвестно. Предположительно, роль лидера выполняет некто Асархаддон. Его династия имеет абсолютную власть над каждым жителем Инферно. Также, проанализировав все записи с камер, мы выяснили имя одного из организаторов нападения на Гонконг — некто старший Уш. Или Уш высший. У нас возникли проблемы с переводом лексикона языка Инферно, однако отличать имена от слов мы можем уверенно. Очень много агентов Инферно среди нас. Мы анализируем каждый телефонный разговор, который наша система не может определить как разговор на любом из известных языков. В одном из перехваченных разговоров упоминалась фраза на латыни — Arbor Mundi. В переводе \"Мировое древо\". Это мифологический архетип, вселенское дерево, объединяющее все сферы мироздания. Как правило, его ветви соотносятся с небом, ствол — с земным миром, корни — с преисподней. С чего бы Инферно говорить на латыни? Мы не нашли никаких значимых упоминаний этой фразы. Следующий доклад ровно через месяц."
    hide nvl
    "— Что-то запутанно. Ты читала вообще?"
    yu "— Не особо доверяю этой шпионской организации. У них очень грязное прошлое. Верить или нет, твоё дело. Я это даже не смотрела."
    menu:
        "Там про тебя написано!":
            if liePoints>0:
                $ liePoints += 1
                yu "— Правда, дай посмотрю!"
                "С серьёзным видом вручил ей планшет. "
                yu "— Где? Где? Где?"
                yu "— Нет тут ничего!"
                "— Как ты вообще в это поверила?"
                # bulka: В принципе это логично, но всё же - стоит отметить, что возникает проблема с ложью. Игрок несовравший в первый раз, в таком темпе не сможет догнать игрока, который это сделал. Аккуратнее с этим. Иначе придётся геммороиться как мне с шахматами и агрессией.
                # pomis: В некоторых ситуациях делаю так, что наличие очков лжи — достаточное, но не необходимое условие для того, чтобы ложь проканала. Местами ложь прокатывает без условий. 
            else:
                yu "— Ты что, правда думаешь, что я в это поверю?"
                "— Я должен был попытаться..."
        "Мне кажется, это достоверная информация.":
            yu "— Тебе кажется. Да и мне это не особо интересно, если честно."
            "— А что тебе интересно?"
            yu "— Хмм... Побеждать в бою."
    "— Ладно... Скажи, а чем ты увлекалась до попадания на военную базу?"
    yu "— Ничем. Так, по дому очень много работы было..."
    "— Эм, а почему у тебя океан на заставке искусственного окна? Мне эти волны в кошмарах снятся!"
    yu "— Ахах. А что такого? Волны как волны, без разницы."
    "Даже не знаю, о чём с ней ещё поговорить."
    "— Ладно, я пойду, наверное."
    yu "— Спокойной!"
    "Юминг проводила меня до двери, я пошёл в свою комнату."
    return
