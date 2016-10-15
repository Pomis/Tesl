init:
    # Характеристики Энлиль
    $ enlilRude = 0 # Грубые ответы увеличивают
    $ enlilSpy = 0 # Навыки шпионства. За листовку-то должны что-то дать.

    # Отношения с персонажами
    $ portPoints = 0 # портальщик. Если с ним нормально общаться, рассказывает, как не выдать себя в городе людей.

    # Вещи
    $ hasExtensionCord = False; # Удлинитель
    $ yenBalance = 0
    $ rurBalance = 0

label ch5enlil:
    # pomis: Параллельно идёт день ch4day0
    # bulka: А почему бы не назвать тогда ch4enlil?
    # pomis: По повествованию это будет после 4 главы. А по времени параллельно.
    "Просторное помещение. На потолке огромная круглая конструкция."
    "Внизу собралось несколько десятков человек."
    ush "— Докладываю итоги операции. Военная база людей не уничтожена. Манипулятор сознания утерян. Потери персонала — трое."
    alil "— Однако, нам удалось наполовину разрушить базу..."
    "Уш разочарованно вздохнул"
    ush "— Тебе кто-то слово давал?"
    sa "— А тебе, Уш, никто не давал право его затыкать. Ещё и после такого провала.{w} Продолжайте."
    "Уш сверлил его злобным взглядом. Толпа оживлённо зашепталась."
    sa "— Продолжайте доклад."
    alil "— База будет неспособна нормально функционировать. Объём повреждений таков, что им будет проще построить новую базу. Фактически, она уничтожена."
    sa "— Вот только самые укреплённые части базы остались неповреждёнными. А их уничтожение и было целью операции. Они просто проведут эвакуацию персонала и оборудования и переедут. Судя по информации от нашего источника, именно на этой базе производились исследования, которые позволят каждому человеку управлять нейронтами."

    # На самом деле, нет, это выдумал Павел, чтобы спровоцировать нападение
    # bulka: Так она неспособна функционировать или главные места всё же целы?
    # bulka: Да и зачем провоцировать атаку на базу? Тем более, что он там сам находится. Бредово.
    # pomis: Он её оперативно покинет
    sa "— Вы понимаете, что это значит?"
    alil "— Да, старший."
    # no2 "— Ничего не добились! Надо было мне дать это сделать!"
    # bulka: Этот чувак одержим местью за свою семью, погибшую в первом городе (у него, кстати, есть название?). Он не будет говорить ну и позорище. Он просто сильнее разозлится. Кроме гнева и злости, вряд ли, что он будет что-то показывать. Да и хз, зачем он тут. Вот первого можно. Он, вроде, серьёзный парень. Более хладнокровный, возможно лидер. Но они оба разведка/контрразведка. Они скорее исполнители, вряд ли они могут тут находиться. 
    # pomis: ok
    ush "— Кстати, хочу сообщить о потенциальном стороннике. Он не стал в меня стрелять, пытался заговорить."
    sa "— Но ты до сих пор не удосужился выучить хотя бы один земной язык! Да, забыл сказать, что ты понижен на два ранга."
    # bulka: Не слишком ли на 3 ранга? Фактически, на 3 звания же. В гиассе помнится, это чуть ли не рядовым сделало очень важную шишку. (апельсинчик)
    # pomis: А кто его знает, насколько у них ранги отличаются. Может, их всего 5? Или 50? Ну пусть будет понижен на два
    "Уш едва сдерживал злость, но продолжал докладывать."
    if stolenFlash:
        ush "— А ещё он передал мне это."
        "Уш показал флешку, которую ему швырнул [playerName]."
        sa "— Это людское запоминающее устройство. Может хранить огромное количество информации. Полезная технология, но абсолютно несовместима с нашими вычислительными машинами."
        alil "— У нас же есть образцы человеческих вычислительных машин?"
        sa "— Конечно есть. Поручаю тебе изучить содержимое и организовать операцию слежки за тем человеком."
        alil "— Вас понял, старший!"
        sa "— На этом всё."
        "Толпа разошлась. Алилум направился в центр исследования человеческих технологий."
    else:
        ush "— Зачем нам знать язык врага? Мы можем их просто убивать!{w} Ладно.{w} Тот человек... Думаю, за ним нужно организовать слежку, он может быть нам полезен."
        sa "— Да ты сам себе противоречишь. Как нам его переманить на нашу сторону не разговаривая с ним на одном языке? Может, ему выучить язык Инферно?"
        "Судя по выражению лица Уша, он был готов убить его прямо сейчас."
        sa "— Алилум, поручаю организовать наблюдение."
    scene black with dissolve
    # сцена какой-нибудь коридор
    # переход, сцена — центр исследований человеческих технологий, везде куча образцов техники
    $ camera_reset()
    show bg inferno lab onlayer background
    show bg inferno front onlayer forward
    alil "— Есть тут кто вообще?"
    show enlil onlayer middle:
        xpos 0.11 ypos 1.0 xanchor 0.5 yanchor 0.72 zoom 0.6 
        easein 1.0 xpos 0.11 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.6 
        pause 0.2
        easein 0.5 xpos 0.11 ypos 0.87 xanchor 0.5 yanchor 1.0 zoom 0.6 
    "Из под стола вылезло существо, всем своим видом выражающее, что его оторвали от чего-то очень интересного"
    en "— Чего так поздно пришёл? Мы уже не работаем."
    # Анимация перемещения наблюдателя
    alil "— Тут срочное поручение от сената."
    show black onlayer forward:
        alpha 0.0
        ease 1.0 alpha 1.0
    $ camera_move(-6000, -953, 1579, -4, duration=1.0) 
    $ renpy.pause(1)
    $ camera_reset()
    hide enlil onlayer middle
    hide bg onlayer background
    hide bg onlayer forward
    hide black onlayer forward
    show bg inferno lab2 onlayer background
    show bg inferno front2 onlayer forward
    show alil bored onlayer middle:
        xpos 0.23 ypos 0.89 xanchor 0.5 yanchor 1.0 zoom 0.83 
    show black onlayer forward:
        alpha 1.0
        ease 1.0 alpha 0.0

    $ all_moves(camera_check_points={'x': [(904, 0, 'easein'), (0, 0.45, 'easein')], 'z': [(205, 0, 'easein'), (0, 0.45, 'easein')]})
    menu:
        "— У меня дела поважнее":
            $ enlilRude += 1 
            alil0 "— Ну и чем ты занимаешься?"

            show alil bored onlayer middle:
                xpos 0.23 ypos 0.89 xanchor 0.5 yanchor 1.0 zoom 0.83 
                ease 1.0 xpos 0.31 ypos 1.03 xanchor 0.5 yanchor 1.0 zoom 0.97 
            "Гость подошёл поближе и стал рассматривать вещи на моём столе."
            "— Я пытаюсь починить ящик-разогревашку! Кто-то решил, что это телепорт, и пытался отправить бананы в Ниппур."
            alil0 "— И что, это важнее поручения сената? Серьёзно? Ящик-разогревашка?"
            "Да что может быть важнее? Я кушать хочу между прочим... Недоверчиво смотрю на незваного гостя"
            if stolenFlash:
                alil0 "— Можешь посмотреть содержимое этого носителя?"
                "Гость вручил мне небольшой пластмассовый предмет."
                "— Хм... Кажется, я знаю, куда вставляется эта штука, я уже видела нечто подобное!"
                "Так. Где же он?{w} Ага."
                # сцена с компом
                "— Что такое Ubuntu?"
                # pomis: ну серьёзно, кто вообще хранит важную инфу на флешках. Было бы нереалистично
                alil0 "— Понятия не имею. Что-нибудь важное там есть или нет?"
                "— Не знаю, всё очень сложно. Оставлю это другим исследователям."
                alil0 "— Ну и ладно, одной проблемой меньше. Я, знаете ли, хочу командовать армией, а не распределять тупые поручения сената."
                "— А я на поверхность хочу."
                alil0 "— О, кстати, да. Можешь взять задание. Нужно следить за каким-то там человеком. Ерунда, сомневаюсь, что это вообще важно. Думаю, даже ты справишься."
                jump mission
            else:
                "— Так что за поручение?"
                alil0 "— Да на самом деле... Я сюда зашёл только потому что это здание возле моего дома. По-хорошему, надо бы отдать это поручение кому-то более ответственному."
                "— Ну и зачем ты тогда меня отвлёк! Я бы уже починила всё и покушала!"
                alil0 "— Вам всем лишь бы покушать. Ладно, мне всё равно не хочется кого-то искать, подбирать для задания. В общем, нужно проследить за каким-то там человеком."
                jump mission
            

        "— Ну, выкладывай":
            alil0 "— Да на самом деле... Я сюда зашёл только потому что это здание возле моего дома. Поручение не особо важное, нужно проследить за каким-то там человеком."
            jump mission

label mission:
    "А вот это уже интересно!"
    "— За человеком? Конечно я возьму это задание!"
    "Алил вручил мне небольшую бумажку."
    "— Ого, тоже перешёл на бумагу?"
    alil0 "— Да, это гораздо удобнее наших пластин, которые даже в карман не положить. Думаю, скоро весь Инферно перейдёт на бумагу."
    # HYXYH: пластин? цивилизация превосходящая человечество использует пластины? серьёзно?))
    # наверное, стоит обыграть причину не в пластинах, а в том, что инферно пытаются писать от руки в целях практики человеческого языка
    # bulka: Они живут под землёй. Офк они более ограничены в органических ресурсах, нежели люди. Я бы даже сказал, что бумага для них будет раритетом. Вполне логично, что основную информации они держат в электронном виде, но записки им приходится писать на пластинах и тд. Культура и повседневная жизнь наций/цивилизаций сильно зависит от наличия тех или иных ресурсов. Просто сравни восток и запад.
    nvl clear
    nvlc "*ПОТЕНЦИАЛЬНЫЙ СТОРОННИК №172*"
    # Фон — рисунок гг от руки 
    # TODO: расписать
    nvlc "Имя [playerName], земного происхождения, страна Россия. Старость организма примерно треть. Примерное местоположение — [cityName]. Является солдатом армии людей. При себе имеет оружие."
    nvlc "Ценную информацию отправлять Алилуму по номеру +666 101010110,1011 "
    hide nvl
    "— А кто Алилум?"
    alil "— Я.{w} Значит, берёшься? Можешь приступать. Как тебя зовут, кстати?"
    "— Энлиль."
    alil "— Значит так, Энлиль, если будет что-то важное, сообщай мне. Ах да, держи пропуск в портал на поверхность в одну сторону."
    alil "— Ну ладно, я пойду."
    "— Спасибо. Наконец-то увижу как там..."

    show alil bored onlayer middle:
        xpos 0.31 ypos 1.03 xanchor 0.5 yanchor 1.0 zoom 0.97  alpha 1
        ease 0.71 alpha 0.0  xpos 0.67
    "Ушёл даже не дослушав!"
    "Я выучила два земных языка, прочитала много статей, и работаю в центре по изучению их технологий. Но до сих пор не видела человека вживую..."
    hide bg onlayer background
    hide black onlayer forward
    hide bg onlayer forward
    scene bg inferno city view with dissolve
    "Пора домой. Поздно уже..."
    # Сцена — дом
    "Какой стрёмный пропуск всё-таки! Могли бы что-то по круче сделать. Да и не важно. Спать!"
    scene black with closing
    "..."
    # Сон для того, чтобы ещё раз усилить контраст ожидание\реальность
    "Мне снилось небо. Глубокое как бесконечность.{w} Я летала по этому небу, а потом приземлилась на траву. Зелёную, как на картинке. "
    "..."
    jump ch5enlil_day1
    