label ch5enlil:
    "Просторное помещение. На потолке огромная круглая конструкция."
    "Внизу собралось несколько десятков человек."
    ush "— Докладываю итоги операции. Военная база людей не уничтожена. Манипулятор сознания утерян. Потери персонала — трое."
    alil "— Однако, нам удалось наполовину разрушить базу..."
    "Уш разочарованно вздохнул"
    ush "— Тебе кто-то слово давал?"
    noname "— А тебе, Уш, никто не давал право его затыкать. Ещё и после такого провала. {w}Продолжайте."
    "Уш сверлил его злобным взглядом. Толпа оживлённо зашепталась."
    noname "— Продолжайте доклад."
    alil "— База будет неспособна нормально функционировать. Объём повреждений таков, что им будет проще построить новую базу. Фактически, она уничтожена."
    noname "— Вот только самые укреплённые части базы остались неповреждёнными. А их уничтожение и было целью операции. Они просто проведут эвакуацию персонала и оборудования и переедут. Судя по информации от нашего источника, именно на этой базе производились исследования, которые позволят каждому человеку управлять нейронтами." # На самом деле, нет, это выдумал Павел, чтобы спровоцировать нападение
    # bulka: Так она неспособна функционировать или главные места всё же целы?
    # bulka: Да и зачем провоцировать атаку на базу? Тем более, что он там сам находится. Бредово.
    # pomis: Он её оперативно покинет
    noname "— Вы понимаете, что это значит?"
    alil "— Да, старший."
    ush "— Кстати, хочу сообщить о потенциальном стороннике. Он не стал в меня стрелять, пытался заговорить."
    noname "— Но ты до сих пор не удосужился выучить хотя бы один земной язык! Да, забыл сказать, что ты понижен на три ранга."
    "Уш едва сдерживал злость, но продолжал докладывать."
    if stolenFlash:
        ush "— А ещё он передал мне это."
        "Уш показал флешку, которую ему швырнул [playerName]."
        noname "— Это людское запоминающее устройство. Может хранить огромное количество информации. Полезная технология, но абсолютно несовместима с нашими вычислительными машинами."
        alil "— У нас же есть образцы человеческих вычислительных машин?"
        noname "— Конечно есть. Поручаю тебе изучить содержимое и организовать операцию слежки за тем человеком."
        alil "— Вас понял, старший!"
        noname "— На этом всё."
        "Толпа разошлась. Алилум направился в центр исследования человеческих технологий."
    else:
        ush "— Зачем нам знать язык врага? Мы можем их просто убивать! Ладно.{w} Тот человек... Думаю, за ним нужно организовать слежку, он может быть нам полезен."
        noname "— Да ты сам себе противоречишь. Как нам его переманить на нашу сторону не разговаривая с ним на одном языке? Может, ему выучить язык Инферно?"
        "Судя по выражению лица Уша, он был готов убить его прямо сейчас."
        noname "— Алилум, поручаю организовать наблюдение."
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
    alil0 "— Тут срочное поручение от сената."
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
            alil0 "— Ну и чем ты занимаешься?"

            show alil bored onlayer middle:
                xpos 0.23 ypos 0.89 xanchor 0.5 yanchor 1.0 zoom 0.83 
                ease 1.0 xpos 0.31 ypos 1.03 xanchor 0.5 yanchor 1.0 zoom 0.97 
            "Алилум подошёл поближе и стал рассматривать вещи на моём столе."
            "— Я пытаюсь починить ящик-разогревашку! Кто-то решил, что это телепорт, и пытался отправить бананы в Ниппур."
            alil0 "— И что, это важнее поручения сената? Серьёзно? Ящик-разогревашка?"
            "Да что может быть важнее? Я кушать хочу между прочим... Недоверчиво смотрю на незваного гостя"
            if stolenFlash:
                alil0 "— Можешь посмотреть содержимое этого носителя?"
                "Гость вручил мне небольшой пластмассовый предмет."
                "— Хм... Кажется, я знаю, куда вставляется эта штука, я уже видела нечто подобное!"
                "Так. Где же он? {w}Ага."
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
    "— За человеком? Конечно я возьму это задание!"
    "Алил вручил мне небольшую бумажку."
    "— Ого, тоже перешёл на бумагу?"
    alil0 "— Да, это гораздо удобнее наших пластин, которые даже в карман не положить. Думаю, скоро весь Инферно перейдёт на бумагу."
    nvlc "*ПОТЕНЦИАЛЬНЫЙ СТОРОННИК №172*"
    # Фон — рисунок гг от руки 
    # TODO: расписать
    nvlc "Имя [playerName], земного происхождения, страна Россия. Старость организма примерно треть. Примерное местоположение — (тут название города, куда их отправят после миссии)"
    hide nvl
    alil0 "— Ну ладно, я пойду."
    "— Спасибо. Наконец-то увижу как там..."

    show alil bored onlayer middle:
        xpos 0.31 ypos 1.03 xanchor 0.5 yanchor 1.0 zoom 0.97  alpha 1
        ease 0.71 alpha 0.0  xpos 0.67
    "Ушёл даже не дослушав!"

    "{w=10}Дальше пока ничего нет"