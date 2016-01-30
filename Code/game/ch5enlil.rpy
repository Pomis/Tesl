label ch5enlil:
    "Просторное помещение. На потолке огромная круглая конструкция."
    "Внизу собралось несколько десятков человек."
    ush "— Докладываю итоги операции. Военная база людей не уничтожена. Манипулятор сознания утерян. Потери персонала — трое."
    alil "— Однако, нам удалось наполовину разрушить базу..."
    "Уш разочарованно вздохнул"
    ush "— Тебе кто-то слово давал?"
    noname "— А тебе, Уш, никто не давал право его затыкать. Ты же понимаешь, что после такого провала ты больше не будешь руководителем боевых операций?"
    "Уш сверлил его злобным взглядом. Толпа оживлённо зашепталась."
    noname "— Продолжайте доклад."
    alil "— База будет неспособна функционировать. Объём повреждений таков, что им будет проще построить новую базу. Фактически, она уничтожена."
    noname "— Вот только самые укреплённые части базы остались неповреждёнными. А их уничтожение и было целью операции. Судя по информации от нашего источника, именно на этой базе производятся исследования, которые позволят каждому человеку управлять нейронтами." # На самом деле, нет, это выдумал Павел, чтобы спровоцировать нападение
    # bulka: Так она неспособна функционировать или главные места всё же целы?
    # bulka: Да и зачем провоцировать атаку на базу? Тем более, что он там сам находится. Бредово.
    noname "— Вы понимаете, что это значит?"
    alil "— Да, старший."
    ush "— Кстати, хочу сообщить о потенциальном стороннике. Он не стал в меня стрелять, пытался заговорить."
    noname "— Но ты до сих пор не удосужился выучить хотя бы один земной язык!"
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
        ush "— Не хочу тратить на это время."
        noname "— Конечно, для чего рядовому бойцу саморазвиваться?"
        "Судя по выражению лица Уша, он был готов убить его прямо сейчас."