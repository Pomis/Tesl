# глава 3 примерный план и эвенты

#каждый рут:
#    чувак проходит регистрацию и медобследование и попадает в группу новичков, которых собрали со всего мира, потом их раскидывают по комнатам и со следующего дня в течении некоторого времени они тренируются с технологиями нейроинтерфейса и оружием на этой базе. в конце каждого определяют на службу в конкретные типы сил. ты едешь туда, куда тебя определили и там месиво

#    новичков не много, 8 человек. Детально до 5


#    день 1
#    новичкам сообщают общую инфу об их подготовке
#    каждый из них не является солдатом, но их способности очень нужны в бою. за неделю солдат не сделаешь, поэтому их научат использовать на максимум их способности. курс такой:
#     первые 3 дня
#      в первой половине дня - теория по использованию и применениям нейроинтов, вторая половина дня - физ подготовка и обучение по выжыванию в чрезвычайнах условиях ("способные" очень ценны и должны уметь выжить в любой ситуации и вернутся в строй)
#    дни 4 - 6 - практика по нейроинтам и выживаниям 
#    день 7 - экзамен на полигоне и распределение исходя из результатов


#    Нейроинты используют в боевой технике, оружии и иследовательско-шпионском оборудовании  - отсуда 3 рута как для инферно, так и для солдата:
#    пилот, спецотряд и разведка/наука
#    на эти руты попадаем по результатам выходного экзамена, а сами результаты от предпочтений и выборов во время учёбы. Вместе с тобой идут и некоторые новички с которыми подружился/стал врагом/нейтрально

#    на каждом варианте своё спецзадание, которое не подразумевает большой риск, но что-то идёт не так и мясо кровь трупы новичков 


init:
    define co = Character('Координатор', color="#c8ffc8")
    define nn2 = Character('NoName2', color="#c8ffc8")
    define mi = Character('Минори', color="#fbc072")
    define man = Character('Чувак', color="#c8ffc8")
    define sl = Character('Слава', color="#c8ffc8")

    define nvlc = Character('', kind=nvl)

    image coordinator serious = "images/coord-serious.png"
    image coordinator smile = "images/coord-smile.jpg"
    image minori = "images/minori.png"

    image bg educlass left = 'images/class-left.png'
    image bg educlass right = 'images/class-right.png'
    image bg educlass center = 'images/class-center.png'
    image bg educlass center titan = 'images/class-center-titan.png'
    image bg poligon = 'images/poligon.png'
    image bg door neurovr = 'images/neurovr-door.png'


label ch3day1:
    "Проснулся я от грохота распахнувшейся настеж двери и громогласного \"РОТА ПОДЬЁМ!\". В дверях стоял крепкий паренёк" # типа булата из акаме, даёшь яой в массы лол
    show coordinator serious with vpunch
    play music "music/E6M7_-_Dobrogo_utra.ogg"
    co "-Просыпаемся ребятки, одеваемся и идём за мной!"
    "на столе под окном уже лежали 4 комплекта формы и наборы для личной гигиены."
    co "-А да, я координатор вашей группы, меня зовут Жорик, но вы можете называть меня Братуха или Красавчик!" #ещё бы красавела, как в старом анекдоте...
    #Переименуйте его пожалуйста! Слишком узнаваемо и слишком слизано выходит. Я хотя бы свою Юфимию переименовал. Да и думаю характер ей поменять.
    co "У вас 3 минуты, время пошло!"
    "Вскоре мы уже шагали по коридору в направлении умывальников, а после нас привели в небольшую столовую."
    "Координатор объяснил, где находится учебный класс, в котором он будет нас ждать и удалился."
    hide coordinator serious with fade
    scene bg educlass center
    "Я огляделся."
    "До сих пор мы всё делали впопыхах и я даже не мог как следует рассмотреть своих товарищей."  
    "Всего нас 8, по 4 парней и девушек. Все были одеты в одинаковую форму" # (описание формы?). 
    "Среди нас были ниггеры, пару реднеков, азиаты, европейцы, словом - пролетарии всех стран.{w} Я даже не уверен, что некоторые из них говорят по русски."
    "Поели мы молча и отправились в класс в довольно отчуждённой обстановке." 

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
    "Как человеку не общительному мне было не просто познакомиться с кем-то в обычной жизни, а тут нужно было провести чуть ли не опрос."
    "Но взглянув на координатора я вздохнул - приказ есть приказ. Такому человеку не откажешь."
    # Я бы его нахуй послал с таким приказом. Точнее бы афк посидел. Можно такой вариант зафигачить.
    menu:
        "Посмотреть направо":
            scene bg educlass right
            show minori at center2
            "Я повернул голову и встретился глазами с девушкой. На вид азиатка."
            "Хм... А она точно боец? Хотя, здесь смотрят только на наличие способности управлять нейронтами..."
            "Девушка смущённо смотрела в пол. Ладно, так и быть..."
            "— Привет...{w} Я [playerName]. А ты?"
            mi "— М-меня зовут Минори."
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
                        "— Да, страшновато немного... Да и мне терять нечего. Мои родители погибли при кораблекрушении, которое, кстати, было по вине армии."
                mi "— Как это? А почему ты решил вступить в неё?"
                "Так, стоп, не нужно разбрасываться такими репликами. Хотя, эта девочка не особо умная... Да и доверчивая. Вроде бы..."
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
            #Почему бы и нет? Мы же даём за разговор с конкретной девушкий +1 именно к ней же, не? Хотя можно делать выбор реплик в диалоге. Потом достижение
            #дать одинокому игроку. Хотя выбор из двух вариантов убог\ Тут точно никак их кол-во не увеличить?
            # просто за разговор +1 нельзя. Надо за какие-то удачные реплики или действия. Тут например девушка любит решительность, когда её защищают.
            # Количество, конечно, можно увеличить, вот только что добавить? 
            # И, вроде бы, решили, что с ней можно замутить только в Инферно-сценарии, значит плюсики нельзя получить в диалогах, уникальных для солдатского рута.

        "Посмотреть налево":
            scene bg educlass left
            "я посмотрел налево и увидел парня европейской наружности, который повернулся в мою сторону"
            #знакомимся с чуваком, с которыми будем пиздить мобов в рейдах в светлом будущем. Этот чувк - Слава

    "Поболтав ещё немного мы принялись знакомиться с другими ребятами. На моё удивление почти все они говорили по русски без акцента."
    "Моё напряжение быстро спало и вскоре мы уже просто болтали одной большой компанией, рассказывая что-то о себе и слушая других."

        # тут ещё немного текста про ребят, кто откуда и общие фразы
    scene bg educlass center
    co "-Ладно, судя по тому, как вы галдите, познакомиться вы уже успели. Давайте начнём"
    hide coordinator smile
    show coordinator serious
    co "Думаю, вам уже объяснили, почему вы здесь и что происходит, но я всё же уточню"
    co "В настоящее время мир находится в стадии скрытной войны. Наш враг - Инферно, некая раса существ, о существовании которых мы узнали недавно."
    co "Они похожи на людей, но их методы борьбы жестоки и хладнокровны, а оружие и технологии много превосходят наши."
    co "Нам удалось получить образцы их оружия и мы открыли удивительную технологию нейроинтерфейса, благодаря которой появилась возможность создавать сложнейшее и эффективное в борьбе с врагом оружие."
    co "Однако совместимы лишь некоторые люди. Все вы подходите для использования нейроинтов, поэтому вы здесь."
    co "Каждый из вас станет оператором определённого типа вооружений и будет выполнять специальные задания."
    co "Борьба, на удивление, идёт не очень активно и боевые действия происходят не так часто, что позволяет скрыть сам факт войны от мирного населения. "
    co "Мы пока не понимаем, почему противник не пытается провести крупномасштабную атаку, из опыта первых столкновений следует, что они на это способны. "
    co "Мы не знаем солько у нас времени, поэтому мы должны использовать его максимально эффективно и быть готовыми ко всему."

    co "ваш краткий курс рассчитан на 7 дней."
    co " В следующие 6 дней я буду рассказывать вам о нашем противнике и оружии, а также о правилах и вашей роли в боевых действиях."
    co "Это будет происходить утром, днём вы будете тренироваться на практике применять это оружие."
    co " Вечером вы будете проходить курсы самообороны и выживания в чрезвычайных ситуациях."
    co "Как видите, график плотный, но даже так мы не сможем сделать из вас бойцов за 6 дней. Этот курс - всего лишь базовая подготовка. "
    co "В конце курса - на 7 день - будет нечто вроде экзамена, вас распределят в определённые отряды, где вы будете служить и продолжать свои тренировки уже на конкретном типе вооружений. "
    co "Есть вопросы?"

    # Вопросов вроде как не оказалось и наш названный Братуха Жорик начал свой ликбез, предварительно раздав листовки
    
    menu:
        "Почитать листовку":
            $ spyPoints += 1
            "мне стало интересно узнать о противнике и я углубился в чтение"
            
            nvlc "*ПЕРВОЕ СТОЛКНОВЕНИЕ С ИНФЕРНО*"
            nvlc "2037 год, Июль. Происходит извержение вулкана Тейде — на Канарских островах. Все населённые пункты были уничтожены извержением, но это официальная версия. 
            Вулканологи утверждают, что если бы действительно произошло извержение, то было бы настолько мощное цунами, что смыло бы прибрежные города Западной Европы. 
            Но острова действительно покрыты пеплом и застывшей лавой. Но распределение этой лавы выглядит так, будто бы извержение происходило избирательно с целью уничтожить всё живое. 
            Европой была отправлена группа исследователей. Результаты их экспедиции шокировали правительство: были обнаружены записи с уцелевших камер наблюдения. Существа, размерами с девятиэтажные дома, покрытые лавой, перемещаясь с невероятной скоростью разрушают всё на своём пути.
            Спустя день было решено создать организацию по борьбе с этой угрозой. "
            menu:
                "Читать до конца":
                    $ spyPoints += 1
                    nvl clear
                    nvlc  "...следующий год прошёл спокойно, будто бы эти существа просто предупредили. Или готовились к чему-то более масштабному. Никто не понимал, откуда ждать удара. Особо пристальное влияние уделялось вулканам, что было крайне ошибочным."

                    nvlc "Ровно через год в одном из оживлённых кварталов неизвестный расстрелял из автомата толпу прохожих. Выжившие утверждали, что неизвестный появился из ниоткуда и был одет как иностранец. Всё произошло мгновенно, а затем он испарился в воздухе."

                    nvlc "Тем временем, наша организация провела масштабные исследования инцидента на Канарских островах. Учёные пришли к выводу, что вражеские города расположены на глубине от 5 до 50 км, в зависимости от толщины земной коры. Большинство городов расположено под дном Атлантического океана. Для нахождения их
                    точного местоположения, а также их структуры, были снаряжены экспедиции — плавучие платформы со специальным оборудованием. Так как всё держалось в секрете, платформы маскировались под нефтедобывающие. Одной из экспедиций был обнаружен город на глубине 7 километров около берегов Северной Африки. 
                    Станция пыталась просканировать его точные размеры и найти какие-то туннели или иные связующие пути с другими городами. Естественно, нефтедобывающая платформа, зависшая на несколько дней там, где её не должно быть, вызвала подозрение у Инферно, и они поспешили от неё избавиться. Поэтому, со дна океана были отправлены существа, которые и потопили платформу. "
                    nvl clear
                    nvlc "После этого инцидента было решено оснащать станции охраной. При чём, охраной, технологически передовой. Охрана была расположена как и над водой, так и под. Так как враг располагает искусственными существами, то не исключено, что у него есть и такие существа, которые идеальны для ведения боя под водой."
                    nvlc "Обычные подводные лодки бы просто не смогли вовремя отреагировать и успеть вступить в бой. Поэтому, простые подводные лодки были заменены более адаптированными и манёвренными аналогами. Синергия лучших мировых учёных позволила создать новый интерфейс взаимодействия человека с техникой — искусственная нервная система. Пилот чувствовал технику продолжением своего тела. "
                    nvl clear
                    nvlc "Это увеличивало скорость реакции на несколько порядков. Однако, далеко не каждый человек мог стать таким пилотом, у обычного человека нервная система не способна развиваться после того, как она полностью сформируется. И лишь в одном из миллионов случаев, человек был открыт к таким модификациям нервной системы. И чем человек старше, тем больше шанс, что его нервная система уже закрыта. По этому среди людей возраста до 25 лет было проведено массовое исследование, с целью, якобы, всеобщей проверки на новый вид вируса приобретённого иммунодефицита, который, якобы, распространился примерно 20 лет назад, и находится в спящей форме. 
                    С теми людьми, которые подходили на роль пилотов, связывались военные и вербовали на службу. "
                "Смотреть презентацию":
                    $ killPoints += 1
                    scene bg educlass center titan
                    "Занятие напомнило мне школьный урок биологии, там нам показывали картинки животных и рассказывали как они живут и что едят."
                    "Однако тут было небольшое отличие - про каждое существо нам подробно объясняли как его убить."
                    "Хоть я и отвлёкся на листовку, но я быстро вник в суть."
                    "Арсенал живой силы противника пугал своим разнообразием, нам объяснили, что это специально созданные животные для уничтожения людей." 
            hide nvl
            # инфа про противника из файла на гитхабе про инферно
        "Смотреть презентацию":
            $ killPoints += 2
            scene bg educlass center titan
            # картинки или на листовке или проектор
            # тут будет слайдшоу из 2-3 набросков существ противника и текст. На картинках можно написать название противника и слабое место.
            # В руте солдата во время боя перед тобой появится одно из этих существ и будет выбор, в какую часть тела противника стрельнуть (как VATS в FALLOUT)
            # от выбора куда выстрелишь будет зависить убьёшь ты существо или ранишь. если не убьёшь, то оно убьёт кого то из друзей. Или тебя :) 
            "Занятие напомнило мне школьный урок биологии, там нам показывали картинки животных и рассказывали как они живут и что едят."
            "Однако тут было небольшое отличие - про каждое существо нам подробно объясняли как его убить."
            "Арсенал живой силы противника пугал своим разнообразием, нам объяснили, что это специально созданные животные для уничтожения людей." 
    scene bg educlass center titan
    co "Сами же Инферно в боях открыто не участвуют, чаще всего сражаться придётся с перечисленными существами."
    co  "Ну из слайдов вы знаете их слабые места, так что это не должно вызвать проблем"
    if killPoints == 0:
            "Чёрт, кажется я всё прослушал"
    "Занятие шло около 3 часов и голова уже шла кругом, но наконец пришло время обеда"
    "Нам дали пол часа чтобы поесть, а потом все вместе мы пошли практиковаться в полученных знаниях - мы пошли в ... тир"
    scene bg poligon
    sl "Тир? Я бы назвал это место полигоном"
    "Людей здесь было много, а оружия - ещё больше, как на чёрном рынке."
    "Кругом ходили крутые мужики из блокбастеров с футуристическими пушками наперевес и картина в целом заставляла поверить меня, что я попал в фильм. "
    scene bg door neurovr
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
    co "Что, уже всё? Меньше 30 секунд! Ты мужик или кто, давай мочи эту тварь! Пошёл!"
    "И я снова нырнул в виртуальный мир"
    if killPoints >= 1:
        "В этот раз я уже знал, чего ожидать. Тварь была мне знакома из первого урока и я знал, как её убить."
        "На поясе у меня было обычное оружие - пистолет, но этого было достаточно и я быстро справился со своим первым врагом."
        "В лучших традициях шутеров, тело поверженного монстра исчезло, оставив после себя какой-то предмет.{w} Им оказался навигатор с отмеченной точкой \"пункт сбора команды\""
        "Значит, симулятор командный и я могу встретить здесь остальных своих одногруппников."
        "Ну выбора нет, нужно идти к ним."
        "По пути я уничтожил ещё пару противников, подобрав с них несколько гранат. Точка сбора уже близко. *треск*"


    if killPoints == 0:
        "Встречаться с этой тварью ещё раз желания у меня не было, да и из оружия у меня был всего лишь пистолет, что казалось мне просто издевательством."
        "Хотя, возможно нас испытывают. Но гнаться за результатами я не стал и решил просто сбежать." 
        "Убежав вниз по дороге, я увидел море. Значит, карта ограничена водой и далеко уйти не получится."
        "Этот симулятор вроде основан на реальных событиях, значит это всё где-то произошло."
        "Вулкан.{w} Море.{w} Точно!"
        "Я читал об этом сегодня, кажется, это было нападение на Канарские острова."
        "Там было что-то про лавовых монстров *треск*"

    with vpunch
    "Я повернулся на шум и увидел его. Огромный горящий монстр."
    "Он окинул меня взглядом ..."
    "несколько секунд спустя я опять сидел в кресле симулятора и любовался бетонной стеной."
    co "Ну, в этот раз уже получше, но до точки сбора никто так и не добрался. Сейчас я зайду с вами и покажу, как нужно действовать с таким монстром."
    "Координатор буквально за несколько секунд справился с монстром. Я был в шоке." 
    menu:
                "Восхититься":
                     $ killPoints += 1
                     "Мне показалось будто я попал в фильм - настолько виртуозно он сражался с этим монстром. У противника просто не было шансов. Я тоже хочу так уметь!"
                "Огорчиться":    
                     $ spyPoints += 1
                     "Вряд ли я когда-нибудь стану таким. Открытое противостояние всегда было моим слабым местом. Даже в школе я предпочитал действовать и мстить обидчикам исподтишка, нежели в открытую. Надо постараться узнать побольше узнать о том, как избегать этих чудовищ."
    "Ну что, поняли, салаги, как надо действовать в таких случаях? Теперь вперёд - на барикады!"
    #####Я чуток сонный, так что немножко запутался в синтаксисе, операторах и тд. Как я понял продолжение в обоих случаях мы делаем сосалити? Если так, то у меня всё так и должно быть, а если нет, то я уже сонный и не помню, что должно быть по-другому. Дальше если очков убийства два, то сосалити делает монстр, если очков шпионства два, то мы изи убегаем, а если игрок даун и выбрал по одному очку, то я хз что делать дальше. Придумаем короч. Сосалити во второй раз не очень вариант. Мб он с трудом справится или еле-еле свалит. Должен же быть билд со сбалансированной раскачкой. 
    #####З.ы. Скорее всего, я накосячил с синтаксисом, ибо долго не работал с этой хренью. Кто шарит - тот исправит.








