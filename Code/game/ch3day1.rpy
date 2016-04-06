# глава 3 примерный план и эвенты

#каждый рут:
#    чувак проходит регистрацию и медобследование и попадает в группу новичков, которых собрали со всего мира, потом их раскидывают по комнатам и со следующего дня в течении некоторого времени они тренируются с технологиями нейроинтерфейса и оружием на этой базе. в конце каждого определяют на службу в конкретные типы сил. ты едешь туда, куда тебя определили и там месиво

#    новичков не много, 8 человек. Детально до 5


#    день 1
#    новичкам сообщают общую инфу об их подготовке
#    каждый из них не является солдатом, но их способности очень нужны в бою. за неделю солдат не сделаешь, поэтому их научат использовать на максимум их способности. курс такой:
#     первые 3 дня
#      в первой половине дня - теория по использованию и применениям нейроинтов, вторая половина дня - физ подготовка и обучение по выживанию в чрезвычайнах условиях ("способные" очень ценны и должны уметь выжить в любой ситуации и вернутся в строй)
#     pomis: Даааа, во второй половине второго дня получилась отличная физ подготовка) 
#    дни 4 - 6 - практика по нейроинтам и выживаниям 
#    день 7 - экзамен на полигоне и распределение исходя из результатов


#    Нейроинты используют в боевой технике, оружии и иследовательско-шпионском оборудовании  - отсуда 3 рута как для Инферно, так и для солдата:
#    пилот, спецотряд и разведка/наука
#    на эти руты попадаем по результатам выходного экзамена, а сами результаты от предпочтений и выборов во время учёбы. Вместе с тобой идут и некоторые новички с которыми подружился/стал врагом/нейтрально

#    на каждом варианте своё спецзадание, которое не подразумевает большой риск, но что-то идёт не так и мясо кровь трупы новичков 



label ch3day1:
    scene black 
    scene bg room back with opening
    $ camera_reset()
    show bg room back onlayer background 
    show bg room front onlayer forward 
    "Проснулся я от грохота распахнувшейся настеж двери и громогласного \"РОТА ПОДЬЁМ!\". В дверях стоял крепкий паренёк" # типа булата из акаме, даёшь яой в массы лол
    show coordinator serious onlayer middle with vpunch
    play music "music/E6M7_-_Dobrogo_utra.ogg"
    co "— Просыпаемся, ребятки, одеваемся, завтракаем и идём в учебный класс!"
    # "на столе под окном уже лежали 4 комплекта формы и наборы для личной гигиены."
    # pomis: Эх, эти описания не состыковываются со всем остальным. Приходится убирать.
    co "— А, да, я координатор вашей группы, меня зовут Жорик, но вы можете называть меня Братуха или Красавчик!" # bulka: ещё бы красавела, как в старом анекдоте...
    co "У вас 7 минут, время пошло! Где столовая находится, все знают?"
    co "— Потом на лифте приедете ко мне."

    show slava smiling onlayer middle:
        xpos -0.29 ypos 1.47 xanchor 0.43 yanchor 1.0 zoom 1.16 rotate 67 
        ease 0.5 xpos -0.03 ypos 1.47 xanchor 0.43 yanchor 1.0 zoom 1.16 rotate 67 
    sl "— Вставай давай!"
    hide bg onlayer background
    hide bg onlayer forward
    hide slava onlayer middle
    hide coordinator onlayer middle
    scene bg coridor newbies with dissolve
    "Вскоре мы уже шагали по коридору в направлении столовой."
    hide coordinator serious with fade
    "Я огляделся."
    "До сих пор мы всё делали впопыхах и я даже не мог как следует рассмотреть своих товарищей."  
    "Всего нас 8, по 4 парней и девушек."#" Все были одеты в одинаковую форму" # (описание формы?). 
    "Среди нас были ниггеры, пару реднеков, азиаты, европейцы, словом - пролетарии всех стран.{w} Я даже не уверен, что некоторые из них говорят по русски."
    scene bg diner with dissolve
    "Поели мы молча и отправились в класс в довольно отчуждённой обстановке." 
    scene bg educlass center with dissolve
    # Тут будет картинка класса с одним пустым местом, чтоб когда сел ты уже знал в лицо кто сидит справа и слева. 
    #можно даже не весь класс рисовать, а только место где никто не сидит и двух соседей. слева парень и справа девушка. 
    #хз как это сделать, может в классе 9 одноместных парт? типо как в катаве



    "Когда все собрались и расселись по местам, Братуха объявил:"
    show coordinator serious
    co "-Ну, добро пожаловать!"
    "Он внимательно оглядел нас и вдруг спросил"
    hide coordinator serious
    show coordinator smile with vpunch
    co "-А что это вы такие серьёзные? "
    co "Спецотряд! Даю вам первое задание! "
    co "Чтоб через 10 минут каждый из вас знал всё о каждом из вашей группы!"
    co" Кто, откуда, какой цвет глаз у его собаки и вообще всё, буду спрашивать устно и сверять с досье, кто расскажет больше всех получит...{w} кое-что! поехали!"


    "Я напрягся."
    "Как человеку необщительному мне было непросто познакомиться с кем-то в обычной жизни, а тут нужно было провести чуть ли не опрос."
    "Но взглянув на координатора я вздохнул - приказ есть приказ. Такому человеку не откажешь."
    # bulka: Я бы его нахуй послал с таким приказом. Точнее бы афк посидел. Можно такой вариант зафигачить.
    menu:
        "Посмотреть направо":
            $ minoriPoints += 1
            scene bg educlass right
            show minori at center2

            "Я повернул голову и встретился глазами с девушкой. На вид азиатка."
            "Хм... А она точно боец? Хотя, здесь смотрят только на наличие способности управлять нейронтами..."
            "Девушка смущённо смотрела в пол. Ладно, так и быть..."
            "— Привет...{w} Я [playerName]. А ты?"
            mi "— М-меня зовут Минори."
            # bulka: Кстати, у японцев же бзик с именем-фамилией. По имени звать могут только близкие/хорошо знакомые люди. Это надо бы как-то обыграть.
            "Здесь все что-ли русский знают?"
            "Минори украдкой подняла взгляд, посмотрела мне в глаза и тут же бросила взор на свои руки. Она нервно загибала себе пальцы и всячески выражала беспокойство."
            "— Как ты сюда попала?"
            mi "— Я проходила тест в клинике, а потом меня забрали. Хорошо, что я изучала русский в качестве второго иностранного, из-за этого меня взяли именно на эту базу. Так бы отправили куда-то к австралийским берегам."
            mi "— Я боюсь кенгуру."
            mi "— И пингвинов."
            mi "— И... А, неважно..."
            "Что это за существо такое? Есть способность к языкам, но какие-то очень скудные представления об окружающем мире. Пингвинов она боится. А она вообще в курсе, против кого мы воюем?"
            if inferno:
                "— Я тоже попал сюда пройдя тест..."
                "— А кем ты была в обычной жизни?"
                mi "— В обычной? Так говоришь, будто она закончилась..."
                "— Так ты не понимаешь, что вообще происходит?"
                mi "— Честно говоря... Не особо."
                "Она снова понурила голову."
                mi "— Я обычная японская школьница. Я ничего не понимаю! Хочу домой!"
                "Некоторое время мы провели в молчании, но она всё-таки нарушила тишину."
                mi "— А тебе не страшно?"
                menu:
                    "Нет, совсем":
                        $ minoriPoints += 1
                        "— Нет, совсем. Да и мне терять нечего. Мои родители погибли при кораблекрушении, которое, кстати, было по вине армии."
                    "Есть немного...":
                        "— Да, страшновато немного... Но мне и терять нечего. Мои родители погибли при кораблекрушении, которое, кстати, было по вине армии."
                mi "— Как это? А почему ты решил вступить в неё?"
                "Так, стоп, не нужно разбрасываться такими репликами. Хотя, эта девочка не особо умная... Да и доверчивая. Вроде бы..."
                "Такими очень легко манипулировать."
                # bulka: Тут мне пришла в голову гениальная идея для ачивки - мамкин манипулятор. Условия для её получения - пройти игру так, чтобы упоминались все "манипуляции", доступные в игре, но при это дико обломаться в конце. От того же павла к примеру.
                # bulka: Вторая ачивка будет называться "Многоходовочка". Условия её получения пока не продумал, но она будет схожа с предыдущей в плане облома. Скорее всего условием получения будет прохождение игры с упоминанием всех гениальных планов (многоходовочек) в игре.
                "— А что мне остаётся..."
                mi "— И правда."
                "Она что, правда поверила?"
            else:
                "— А я попал в кораблекрушение из-за Инферно. И теперь приложу все усилия, чтобы отомстить за мою семью, которая там погибла."
                mi "— Так а как тебя военные нашли?"
                "Я пересказал ей свою историю."

            co "— Осталась пять минут!"
            mi "— Ой! Мы же ничего не успели узнать!"
            # мы так и не придумали имя гг
            #знакомимся с Минори и +1 за то, что заговорил с ней
            #давать плюсы просто за разговор слишком круто) от игрока же это не зависит
            # bulka: Почему бы и нет? Мы же даём за разговор с конкретной девушкий +1 именно к ней же, не? Хотя можно делать выбор реплик в диалоге. Потом достижение дать одинокому игроку. Хотя выбор из двух вариантов убог\ Тут точно никак их кол-во не увеличить?
            # bulka: А вот и третья ачивка, яхоу!
            # просто за разговор +1 нельзя. Надо за какие-то удачные реплики или действия. Тут например девушка любит решительность, когда её защищают.
            # pomis: Количество, конечно, можно увеличить, вот только что добавить? 
            # И, вроде бы, решили, что с ней можно замутить только в Инферно-сценарии, значит плюсики нельзя получить в диалогах, уникальных для солдатского рута.
            # bulka: И нихера не понятно кто что писал\ 

        "Посмотреть налево":
            scene bg educlass left
            show tenko at left
            play music "music/E6M7 - Gagarin.mp3"
            if playedChess:
                "Я посмотрел налево и увидел того странного парня, с которым вчера играл в шахматы."
                $ knowTenkoName = True # Все разветвления ведут к тому, что гг узнаёт его имя 
                "В правой руке он вращал чёрного короля из того комплекта фигур, которым мы играли."
                "Неужто он так помешан на шахматах?"
                if chesspoints:
                    "Тогда неудивительно, что он так хорошо играл."
                    "— Привет, что ли. Меня зовут [playerName]."
                    if strangerPoints>0:
                        ten "— О, это ты, паренёк. Меня зовут Тенко. Будем знакомы."
                        # bulka: Насчёт паренька не уверен - слишком панибратское отношение для такое персонажа. Скорее это к жорику подходит. Просто тут надо было изобразить удивление, а "о, это ты" было бы слишком грубо.
                        ten "— Вчерашняя игра была довольно интересной."
                        "— Ага. Я давно не играл в шахматы. Приятно было вспомнить былое."
                        "— А ты, однако, неплохо играл. Давно играешь?"
                        ten "— Да нет. Не так уж давно увлёкся."
                        "— Очень даже неплохо для новичка."
                        ten "— Спасибо."
                    else: 
                        ten "— Тенко. Будем знакомы. Хотя, ты мне не особо интересен."
                        "— Это ещё почему?"
                        ten "— А чем ты можешь быть мне полезен?"
                        "Я даже не знаю, что и ответить на такое."
                        ten "— Ладно, не парься, просто было интересно, как ты отреагируешь."
                        "Тенко слегка усмехнулся."
                else:
                    "Тогда удивительно, что он так плохо играл."
                    ten "— О, это ты, паренёк. Меня зовут Тенко. Будем знакомы."
                    "Я промолчал."
                    ten "— Хей, ты тут?"
                    "— Чего тебе?"
                    ten "— Знаешь, когда тебе представляются, невежливо будет просто молчать."
                    "Ох, чувствую, успеет он меня достать."
                    if wonchess:
                        "— Ты слишком скучен. Мне не интересно с тобой общаться."
                        "Чувствую, если ему не назвать имя, он не отстанет."
                        "— Ну так и быть, меня зовут [playerName]."
                    else:
                        $ useless = True
                        "— Ты меня раздражаешь. Мне не интересно с тобой общаться."
                        "Чувствую, если ему не назвать имя, он не отстанет."
                        "— Ну так и быть, меня зовут [playerName]."
                    stranger "— [playerName] значит. Буду знать."
                    if strangerPoints>0:
                        "Тенко загадочно улыбнулся. Какая-то неприятная у него улыбка."
                        if antiTenkoPoints == 0:
                            "От его улыбки по спине пробежал неприятный холодок."
            else:
                if seenChessGame:
                    "Я посмотрел налево и увидел того странного парня, который вчера игрался с шахматами."
                    "В правой руке он вращал чёрного короля."
                    "Неужто он так помешан на шахматах?"
                else:
                    "Я посмотрел налево и увидел странного парня, вращающего в руках  шахматную фигуру."
                    "Кажется, это чёрный король."
                    # bulka: Изменил, ибо неразумно смотрелось, что гг не мог отличить фигуру из-за того, что не видел как парень играется с шахматами. Разве что комплект был для декора.
                "— Привет, что ли. Меня зовут [playerName]."
                ten "— Тенко. Будем знакомы. Хотя, ты мне не особо интересен."
                "— Это ещё почему?"
                ten "— А чем ты можешь быть мне полезен?"
                "Я даже не знаю, что и ответить на такое."
                ten "— Ладно, не парься, просто было интересно, как ты отреагируешь."
                "Тенко слегка усмехнулся."
            ten "— Этот координатор... Готов поспорить, он уже забыл, что хотел от нас."
            if useless:
                "О боже, ты сегодня от меня отстанешь?"
                "— С чего ты взял?"
            else:
                "— С чего такие поспешные выводы?"
            ten "— Я вижу людей насквозь."
            "Тенко стал всматриваться в меня. Он что, буквально пытается просмотреть меня насквозь?"
            if inferno:
                if strangerPoints>0:
                    ten "— Так. А ты не так прост как кажешься на первый взгляд. Уже убивал?"
                    if antiTenkoPoints>0:
                        "— Нет конечно. С чего ты взял?"
                        if antiTenkoPoints>1 or liePoints>0:
                            $ liePoints += 1
                            ten "— Вот как? Значит я ошибся. А мне казалось я разбираюсь в людях."
                            "Хэх. Не на того напал. Меня так легко не раскусишь."
                        else:
                            ten "— Не похоже. Я чую кровь на твою руках."
                            "Да что за тип..."
                            "— А ещё что чуешь?"
                            ten "— Больше ничего. Только кровь."
                            ten "— Да ладно, расслабься. Наша работа — убивать."
                            "Какой-то он очень жуткий. Впредь, буду держаться от него подальше."
                            $ tenkoAttention += 1
                            # bulka: А вот тут нам и пригодится наша ложь. Ещё надо замутить что-то, если очко странника 2. Я сонный, меня на это не хватит.
                            
                    else:
                        $ tenkoAttention += 2
                        "Меня бросило в холодную дрожь от такого вопроса."
                        "— Нет, с чего бы?"
                        ten "— Точно убивал. И очень недавно."
                        "Да кто он такой чтобы читать меня?"
                        "— Опять шуточки свои?"
                        ten "— Раскусил! Ты аж побледнел, как будто и правда кого-то грохнул."
                        "Тенко снова усмехнулся. Не верю, что это была просто шутка."
                else:
                    ten "— Я смотрю в тебя и не вижу совсем ничего интересного. Ты какой-то скучный."
                    "Тенко продолжал смотреть в меня. Как же он давит! И как мне с ним сражаться в одной команде?"
                    ten "— Ты чего такой серьёзный-то? Я же просто шучу..."
                ten "— Как ты сюда попал?"
                "Я рассказал ему вкратце про кораблекрушение. Всего ему знать не следует, не доверяю я ему. Сказал, что прямо из госпиталя забрали сюда, ничего не объяснив."
            else:
                ten "— Я смотрю в тебя и не вижу совсем ничего интересного. Ты какой-то скучный."
                "Тенко продолжал смотреть в меня. Как же он давит! И как мне с ним сражаться в одной команде?"
                ten "— Ты чего такой серьёзный-то? Я же просто шучу..."
                ten "— Как ты сюда попал?"
                "Я рассказал ему вкратце про кораблекрушение. Всего ему знать не следует, не доверяю я ему. Сказал, что прямо из госпиталя забрали сюда, ничего не объяснив."
            ten "— Прохладная история." 
            "— Не зли меня." with bloodrage
            ten "— Ладно, проехали. Расскажу о себе."
            ten "— У меня всё гораздо проще, плановая проверка на вирусы. Якобы лет 20 назад была утечка какого-то штамма ВИЧ, и нужно было всех проверить. На самом деле проверяли способность управлять нейронтами. Кстати, я слышал, что это технология Инферно."
            "— Возможно..."
            # "Он повернулся в мою сторону."
            # "Я посмотрел налево и увидел парня европейской наружности, который повернулся в мою сторону."
            # "Он смотрел на меня совершенно без эмоций и даже не собирался начинать разговор."
            # bulka: Пометка скорее для себя, ибо уже сплю. Тут будет взаимодействие (скорее всего гемморное как с шахматами) с пойнтами лжи и антипойнтами. Суть будет заключаться в том, насколько хорошо мы будем лгать и будет ли Тенко нас читать. Блин, значение имени ему отлично подходит, но не звучит\ Надо быть аккуратнее! с пойнтами лжи, ибо они могут быть использованы и переделаны чуть раньше. С антипойнтами такой проблемы нет.
            # bulka: Сделал кое-что, но недоделал. Слишком мудрённо я это делаю. Хорошо хоть переменные дополнительные использую. Правда в таком темпе их надо будет уже нумеровать.
    "Поболтав ещё немного мы принялись знакомиться с другими ребятами. На моё удивление все иностранцы говорили по-русски почти без акцента. Особенно хорошо говорила японка Минори."
    "Моё напряжение быстро спало и вскоре мы уже просто болтали одной большой компанией, рассказывая что-то о себе и слушая других. Правда не все сочли нужным представиться."
    sl "— Скорее бы уже показать этим тварям Кузькину мать!"
    "— Ещё ботинком по столу постучи!"
    isc0 "— А вы, ребята, вошли в роль."
    "В роль кого? Не могу сообразить."
    menu:
        "— Ещё бы. А ты?":
            $ iscraPoints += 1
            isc0 "— Да. Правда, до конца не понятно, что происходит, но мне нравится."
            "А вот мне не до конца понятно, о чём она говорит."
        "— Какую роль?":
            isc0 "— Ну кого они хотят из нас сделать... Отчаянных бойцов?"
            isc0 "— Или нет никакой угрозы?"
    isc0 "— А кто-нибудь вообще встречал этих Инферно? Кроме организаторов."
    if knowTenkoName==False:
        ten0 "— Не веришь в их существование?"
    else:
        ten "— Не веришь в их существование?"
    mi "— А может, мы на телешоу?"
    isc0 "— Это вряд ли. Тут что-то поинтереснее. В любом случае, от нас скроют больше, чем расскажут."
    sl "— Тебе не нужно знать всё, чтобы понимать, что люди нуждаются в нашей защите!"
    menu:
        "— А вдруг, это Инферно нуждаются в защите от нас?" if inferno:
            $ slavaPoints -= 1
            $ iscraPoints += 1
            sl "— Совсем дурак, что ли?"
            isc0 "— Всё возможно..."
        "— Однако, слепо убивать тоже не круто." if inferno==False:
            $ iscraPoints += 1
            isc0 "— Ну хоть кто-то здравомыслящий тут..."
            sl "— Они враги нашей цивилизации. Какая разница, слепо, не слепо..."
        "— Защитить человечество — вот наша цель.":
            $ slavaPoints += 1
            $ minoriPoints += 1
            $ iscraPoints -= 1
            if inferno:
                $ liePoints += 1
            sl "— Верно!"
        "Промолчать":
            "Так и хочется сказать что-то умное, но лучше промолчу."
        # тут ещё немного текста про ребят, кто откуда и общие фразы
    scene bg educlass center
    co "— Ладно, судя по тому, как вы галдите, познакомиться вы уже успели. Давайте начнём."
    hide coordinator smile
    show coordinator serious
    co "— Думаю, вам уже объяснили, почему вы здесь и что происходит, но я всё же уточню"
    co "— В настоящее время мир находится в стадии скрытной войны. Наш враг - Инферно, некая раса существ, о существовании которых мы узнали недавно."
    co "— Они похожи на людей, но их методы борьбы жестоки и хладнокровны, а оружие и технологии во многом превосходят наши."
    co "— Нам удалось получить образцы их оружия и мы открыли удивительную технологию нейроинтерфейса, благодаря которой появилась возможность создавать сложнейшее и эффективное в борьбе с врагом оружие."
    co "— Однако совместимы лишь некоторые люди. Все вы подходите для использования нейроинтов, поэтому вы здесь."
    co "— Каждый из вас станет оператором определённого типа вооружений и будет выполнять специальные задания."
    isc0 "— Хочу стрелять ракетами."
    sl "— Молчи, женщина!"
    isc0 "— Мне удалось воспользоваться пистолетом на этих ваших нейронтах. И должна сказать, это было настолько просто, будто я всю жизнь умела стрелять."
    isc0 "— Кто после такого поверит, что мы будем оператором определённого типа вооружений? Если любая пушка одинакова проста в использовании?"
    co "— Как тебя зовут?"
    isc "— Искра."
    co "— Не любым оружием так просто управляться, как пистолетом."
    "Искра вздохнула."
    co "— Борьба, на удивление, идёт не очень активно и боевые действия происходят не так часто, что позволяет скрыть сам факт войны от мирного населения. "
    co "— Мы пока не понимаем, почему противник не пытается провести крупномасштабную атаку, из опыта первых столкновений следует, что они на это способны. "
    co "— Мы не знаем сколько у нас времени, поэтому мы должны использовать его максимально эффективно и быть готовыми ко всему."

    co "— Ваш краткий курс рассчитан на 7 дней."
    co "— В следующие 6 дней я буду рассказывать вам о нашем противнике и оружии, а также о правилах и вашей роли в боевых действиях."
    co "— Это будет происходить утром, днём вы будете тренироваться на практике применять это оружие."
    co "— Вечером вы будете проходить курсы самообороны и выживания в чрезвычайных ситуациях."
    co "— Как видите, график плотный, но даже так мы не сможем сделать из вас бойцов за 6 дней. Этот курс - всего лишь базовая подготовка. "
    co "— В конце курса - на 7 день - будет нечто вроде экзамена, вас распределят в определённые отряды, где вы будете служить и продолжать свои тренировки уже на конкретном типе вооружений. "
    co "— Есть вопросы?"

    "Вопросов вроде как не оказалось и наш названный Братуха Жорик начал свой ликбез, предварительно раздав листовки"
    
    menu:
        "Почитать листовку":
            $ spyPoints += 1
            "Мне стало интересно узнать о противнике и я углубился в чтение"
            nvl clear
            nvlc "*ПЕРВОЕ СТОЛКНОВЕНИЕ С ИНФЕРНО*"
            nvlc "2037 год, Июль. Происходит извержение вулкана Тейде — на Канарских островах. Все населённые пункты были уничтожены извержением, но это официальная версия.  Вулканологи утверждают, что если бы действительно произошло извержение, то было бы настолько мощное цунами, что смыло бы прибрежные города Западной Европы.  Но острова действительно покрыты пеплом и застывшей лавой. Но распределение этой лавы выглядит так, будто бы извержение происходило избирательно с целью уничтожить всё живое.  Европой была отправлена группа исследователей. Результаты их экспедиции шокировали правительство: были обнаружены записи с уцелевших камер наблюдения. Существа, размерами с девятиэтажные дома, покрытые лавой, перемещаясь с невероятной скоростью разрушают всё на своём пути. Спустя день было решено создать организацию по борьбе с этой угрозой. "
            menu:
                "Читать до конца":
                    $ spyPoints += 1
                    nvl clear
                    nvlc  "...следующий год прошёл спокойно, будто бы эти существа просто предупредили. Или готовились к чему-то более масштабному. Никто не понимал, откуда ждать удара. Особо пристальное влияние уделялось вулканам, что было крайне ошибочным."

                    nvlc "Ровно через год в одном из оживлённых кварталов неизвестный расстрелял из автомата толпу прохожих. Выжившие утверждали, что неизвестный появился из ниоткуда и был одет как иностранец. Всё произошло мгновенно, а затем он испарился в воздухе."

                    nvlc "Тем временем, наша организация провела масштабные исследования инцидента на Канарских островах. Учёные пришли к выводу, что вражеские города расположены на глубине от 5 до 50 км, в зависимости от толщины земной коры. Большинство городов расположено под дном Атлантического океана. Для нахождения их точного местоположения, а также их структуры, были снаряжены экспедиции — плавучие платформы со специальным оборудованием. Так как всё держалось в секрете, платформы маскировались под нефтедобывающие. Одной из экспедиций был обнаружен город на глубине 7 километров около берегов Северной Африки.  Станция пыталась просканировать его точные размеры и найти какие-то туннели или иные связующие пути с другими городами. Естественно, нефтедобывающая платформа, зависшая на несколько дней там, где её не должно быть, вызвала подозрение у Инферно, и они поспешили от неё избавиться. Поэтому, со дна океана были отправлены существа, которые и потопили платформу. "
                    nvl clear
                    nvlc "После этого инцидента было решено оснащать станции охраной. Причём, охраной технологически передовой. Охрана была расположена как и над водой, так и под. Так как враг располагает искусственными существами, то не исключено, что у него есть и такие существа, которые идеальны для ведения боя под водой."
                    nvlc "Обычные подводные лодки бы просто не смогли вовремя отреагировать и успеть вступить в бой. Поэтому, простые подводные лодки были заменены более адаптированными и манёвренными аналогами. Синергия лучших мировых учёных позволила создать новый интерфейс взаимодействия человека с техникой — искусственная нервная система. Пилот чувствовал технику продолжением своего тела. "
                    nvl clear
                    nvlc "Это увеличивало скорость реакции на несколько порядков. Однако, далеко не каждый человек мог стать таким пилотом, у обычного человека нервная система не способна развиваться после того, как она полностью сформируется. И лишь в одном из миллионов случаев, человек был открыт к таким модификациям нервной системы. И чем человек старше, тем больше шанс, что его нервная система уже закрыта. По этому среди людей возраста до 25 лет было проведено массовое исследование, с целью, якобы, всеобщей проверки на новый вид вируса приобретённого иммунодефицита, который, якобы, распространился примерно 20 лет назад, и находится в спящей форме.  С теми людьми, которые подходили на роль пилотов, связывались военные и вербовали на службу. "
                "Смотреть презентацию":
                    $ gunPoints += 1
                    scene bg educlass titan
                    "Занятие напомнило мне школьный урок биологии, там нам показывали картинки животных и рассказывали как они живут и что едят."
                    "Однако тут было небольшое отличие - про каждое существо нам подробно объясняли как его убить."
                    "Хоть я и отвлёкся на листовку, но я быстро вник в суть."
                    "Арсенал живой силы противника пугал своим разнообразием, нам объяснили, что это специально созданные животные для уничтожения людей." 
            hide nvl
            # инфа про противника из файла на гитхабе про Инферно
        "Смотреть презентацию":
            $ gunPoints += 2
            scene bg educlass titan
            # картинки или на листовке или проектор
            # тут будет слайдшоу из 2-3 набросков существ противника и текст. На картинках можно написать название противника и слабое место.
            # В руте солдата во время боя перед тобой появится одно из этих существ и будет выбор, в какую часть тела противника стрельнуть (как VATS в FALLOUT)
            # от выбора куда выстрелишь будет зависить убьёшь ты существо или ранишь. если не убьёшь, то оно убьёт кого то из друзей. Или тебя :) 
            "Занятие напомнило мне школьный урок биологии, там нам показывали картинки животных и рассказывали как они живут и что едят."
            "Однако тут было небольшое отличие - про каждое существо нам подробно объясняли как его убить."
            "Арсенал живой силы противника пугал своим разнообразием, нам объяснили, что это специально созданные животные для уничтожения людей." 
    scene bg educlass titan
    co "Сами же Инферно в боях открыто не участвуют, чаще всего сражаться придётся с перечисленными существами."
    co  "Ну из слайдов вы знаете их слабые места, так что это не должно вызвать проблем"
    if gunPoints == 0:
            "Чёрт, кажется я всё прослушал"
    "Занятие шло около 3 часов и голова уже шла кругом, но наконец пришло время обеда"
    scene bg diner with dissolve
    "Нам дали полчаса чтобы поесть, а потом все вместе мы пошли практиковаться в полученных знаниях - мы пошли в... Тир"
    scene bg poligon guns
    play music "music/E6M7 - Welcome to Eight Seven!.mp3"
    show slava laughing at right with dissolve
    sl "— Тир? Я бы назвал это место полигоном"
    pav0 "— Скоро сюда завезут новые пушки. Тогда точно станет полигоном."
    "Людей здесь было много, а оружия - ещё больше, как на чёрном рынке."
    "Кругом ходили крутые мужики из блокбастеров с футуристическими пушками наперевес и картина в целом заставляла поверить меня, что я попал в фильм. "
    scene bg poligon door
    "Но нас провели мимо этого тира к двери с загадочной надписью Neuro VR."
    "Внутри нас ждали какие-то необычные кресла."
    co "Это симуляторы боевых действий. Тут заложены программы реальных боёв и ситуаций, давайте рассаживайтесь и запускайте, нам нужно многое успеть."
    "Экранов у этих симуляторов не было, но как только я сел, то понял, что экраны и не нужны. {w}Нейроинтерфейс. {w}Настоящая виртуальная реальность."
    "Чувства были необычными - я всё ещё видел, что происходило вокруг, но понемногу поверх этого начала прорисовываться другая картинка, а моё тело будто проваливалось во что то вязкое, в какой-то кисель."
    "Я попробовал пошевелить рукой и увидел, как из неё появилась виртуальная рука и выполнила все мои движения, в то время как моя настоящая конечность лишь слабо дёрнулась, всё ещё пытаясь сохранить связь с мозгом."
    "И после этого симуляция окончательно заменила реальный мир."
        # это место в симуляции, эту фотку можно заблурить или чё то там в фотошопе сделать, будет выглядеть нарисовано
        # https://www.google.com/maps/@28.2561213,-16.6231004,3a,90y,316.74h,86.33t/data=!3m6!1e1!3m4!1s2S_rXLaJ6F-rl9GbUGAKFg!2e0!7i13312!8i6656?hl=ru
    "Я сидел в таком же кресле посреди парковки. Первое что бросилось мне в глаза был вулкан.{w} И он извергался."
    "Парковка была посреди его склона и лава уже достигала её, справа виднелся горящий дом."
    "Для меня всё это оставалось лишь симуляцией и я решил поглазеть по сторонам, наслаждаясь видом."
    "Восхищаться ощущениями я мог бы долго, но из-за холма вдруг материализовалось некое существо и, подскочив, снесло мне голову." 
    "Я вздрогнул и обнаружил себя сидящим в кресле и пялящимся в стену."
    co "— Что, уже всё? Меньше 30 секунд! Ты мужик или кто, давай мочи эту тварь! Пошёл!"
    "И я снова нырнул в виртуальный мир"
    if gunPoints >= 1:
        "В этот раз я уже знал, чего ожидать. Тварь была мне знакома из первого урока и я знал, как её убить."
        "На поясе у меня было обычное оружие - пистолет, но этого было достаточно и я быстро справился со своим первым врагом."
        "В лучших традициях шутеров, тело поверженного монстра исчезло, оставив после себя какой-то предмет.{w} Им оказался навигатор с отмеченной точкой \"пункт сбора команды\""
        "Значит, симулятор командный и я могу встретить здесь остальных своих одногруппников."
        "Ну выбора нет, нужно идти к ним."
        "По пути я уничтожил ещё пару противников, подобрав с них несколько гранат. Точка сбора уже близко. *треск*"


    if gunPoints == 0:
        "Встречаться с этой тварью ещё раз желания у меня не было, да и из оружия у меня был всего лишь пистолет, что казалось мне просто издевательством."
        "Хотя, возможно нас испытывают. Но гнаться за результатами я не стал и решил просто сбежать." 
        "Убежав вниз по дороге, я увидел море. Значит, карта ограничена водой и далеко уйти не получится."
        "Этот симулятор вроде основан на реальных событиях, значит это всё где-то произошло."
        "Вулкан.{w} Море.{w} Точно!"
        "Я читал об этом сегодня, кажется, это было нападение на Канарские острова."
        "Там было что-то про лавовых монстров *треск*"

    with vpunch
    "Я повернулся на шум и увидел его. Огромный горящий монстр."
    "Он окинул меня взглядом..."
    # bulka: Мб  с двумя очками убийства он справится и убьёт? А с двумя шпионства свалит.
    # pomis: хз хз
    # TODO: Запилить тут условия
    "Несколько секунд спустя я опять сидел в кресле симулятора и любовался бетонной стеной."
    co "Ну, в этот раз уже получше, но до точки сбора никто так и не добрался. Сейчас я зайду с вами и покажу, как нужно действовать с таким монстром."
    "Мы снова зашли в симуляцию. Вместо привычного склона я появился сразу в точке сбора, вся остальная группа тоже была здесь."
    "Чуть поодаль на земле лежало здоровое противотанковое ружьё. Или что-то очень похожее на него."
    with vpunch
    "Раздался знакомый треск и в нескольких сотнях метров от нас появился огненный титан"
    co "Показываю один раз!"
    "Жорик подбежал к пушке, перезарядил, крикнул \"Вспышка прямо!\" и сразу же выстрелил"
    with vpunch
    "Прогремевший выстрел казался пшиком в сравнении с последующим взрывом"
    "Вспышка обожгла глаза, а потом меня отбросило метров на десять, хотя этого я уже не увидел."
    "Глаза я открыл уже сидя в кресле симулятора.{w} Судя по ошарашеным лицам товарищей, взрывная волна убила всю команду."
    "Зато Жорик казался довольным."
    co "— Я же сказал, что вспышка прямо. Вас в школе не учили, что нужно лечь головой в сторону от вспышки?"
    "Координатор буквально за несколько секунд справился с монстром. Я был в шоке." 
    menu:
        "Восхититься":
             $ gunPoints += 1
             "— Вот это был взрыв! Что это за пушка?"
             co "— Тут дело не в пушке. {w}Это цезиевый патрон, при реакции с лавой он... Ну вы сами всё видели."
             co "— Будьте осторожнее, если капсула патрона лопнет, то вас уже ничего не спасёт. Перерыв!" 

        "— Это было не честно":    
             $ spyPoints += 1
             "— У нас не было такого оружия во время симуляции, это не честно. Да и стрелять из такой штуки без подготовки... можешь и сам не выжить"
             co "— Ладно, фиг с вами. Зато теперь будете знать что такое цезиевый патрон."
             "Он хохотнул и отпустил команду отдыхать."

    # тут можно сделать выбор куда пойти отдохнуть или какой эвент

    "После отдыха мы сделали ещё несколько заходов, а ближе к вечеру пошли на курсы по выживанию. "
    "Сами курсы были ни чем иным как смесь общей физ-подготовки с применением всякого снаряжения выживальщика."
    scene bg coridor newbies with dissolve
    "Словом, ничего особенного. Но к себе в комнату я возвращался уставшим, как собака."
    if inferno == False:
        show yuming at left with dissolve
        "По пути встретил Юминг."
        yu "— Привет, солдат! Куда путь держишь?"
        menu:
            "— Спать собирался.":
                yu "— Устал наверное с тренировки?"
                "— Есть такое."
                yu "— Ну и иди спи."
                "Какая-то неразговорчивая сегодня, ладно."

            # соврать
            # TODO: в солдат руте на этом моменте тяжко получить этот поинт, исправить
            "— Тебя искал, кстати.":
                if liePoints>0 or renpy.random.randint(1, 3)>1:
                    $ liePoints+=1
                    yu "— Ого, зачем?"
                    "— В гости зайти!"
                    if visitedYumingRoom:
                        yu "— Прости, не сегодня..."
                    else:
                        yu "— Хорошо, я как раз туда иду."
                        if knowYumingRoom == False:
                            yu "— Кстати, интересуешься политикой?"
                            "— Есть немного."
                            yu "— У меня там свежий доклад по Инферно. Может, тебе будет интересно."
                        "Юминг провела меня в свою комнату, жестом указала на стул рядом со столом."
                        call inYumingRoom
                else:
                    yu "— В корпусе новобранцев? На ходу выдумываешь?"
                    yu "— Устал наверное с тренировки?"
                    "— Есть такое."
                    yu "— Ну и иди спи."
                    "Какая-то неразговорчивая она сегодня, ладно."
    scene bg room mine
    "Ещё целых 6 дней...{w} И нахер мне это всё?"
    scene black with closing 
    jump ch3day2








