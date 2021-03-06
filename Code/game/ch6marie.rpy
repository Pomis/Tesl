# Тут ГГ поймёт что Саргон из Инферно, или наоборот. Исходя из этого, будет выход на плохую и хорошую концовку.
# TODO: изучить все диалоги и menu с Марией, и на их основе сделать общение более связным. Чтобы персонаж играл так, будто он помнит действия игрока.

label ch6marie:
    call goodMorning
    call meetSargon
    call ch6revolve

label goodMorning:
    "Проснулся от звуков непонятной природы..."
    "Мне стоило огромного труда открыть глаза и встать с кровати. Тем временем, Мария запускала в полёт из окна небольшие жужжащие устройства. Настенные часы показывали 6 часов утра."
    "— Боже... Что ты делаешь?"
    "Мария от неожиданности выронила одно, не успев включить, и слегка вскрикнула. Судя по последующему звуку, это устройство больше и не включится.{w} Остальные же жужжали вдалеке."
    ma "— Как же ты меня напугал!{w} Я одолжила эти маленькие коптеры у коллег."
    "— Кто-то работал ночью?"
    ma "— Нет, они лежали в шкафу. Думаю, если мы сможем сделать нечто, способное уничтожать нейронты, то нам пригодятся средства доставки."
    "— Выглядит так, будто тебе просто захотелось поиграться с этими штуками, пока не начался рабочий день."
    ma "— Хех, будто ты всё понимаешь. Ладно, ты прав, надо вернуть их на место, пока никто не заметил."
    if needPasscard:
        "— Кстати, у тебя есть какой-нибудь электронный пропуск от этой базы?"
        ma "— Ах да, надо бы их забрать. Совсем забыла. У нас вот всё работало по отпечаткам пальцев!"
        "— Ну да. Что-то не особо помогло."
        ma "— У тебя, кстати, будет минимальный уровень доступа. Продолжишь играть роль простого человека?"
        "Хм. Снова стать солдатом? Или продолжать играть роль?"
        call choiceSoldier
    else:
        ma "— Ты, кстати, не передумал играть роль?"
        "— К чему ты клонишь? Хочешь, чтобы я стал твоим мужем по-настоящему?"
        "Мария резко покраснела."
        ma "— Д-да нет же, я не об этом. Не хочешь снова стать солдатом?"
        call choiceSoldier
    return

label choiceSoldier:
    menu:
            "— Хочу снова воевать.":
                $ choseToBeSoldier += 1
                ma "— Совсем жизнь свою не ценишь?"
                "— Не сказал бы, что мне есть что терять."
                "Мария слегка обиженно посмотрела на меня, но быстро вернула себе привычное выражение лица."
                ma "— Умереть всегда успеешь. Выбор-то конечно за тобой."
                # pomis: По сути, эти выборы будут влиять только на последующие диалоги с Саргоном и на отношения с Марией
                ma "— Ну хотя бы сегодня не уходи, а то мне скучно будет."
                "— Как скажешь... А не будет ли это странным, что я скрываю свои способности?"
                ma "— Скажешь, что случайно обнаружил, когда возился с моим оборудованием."
            "— Продолжу играть роль.":
                $ mariePoints += 1
                ma "— Хех, ну и отлично."
                "Лёгкая напряжённость Марии сразу же пропала, она явно давно хотела задать этот вопрос."
    return


label meetSargon:
    ma "— А теперь пошли пройдёмся до лаборатории. Нужно вернуть образцы этой неведомой летающей фигни."
    "В лаборатории уже был Саргон, вдумчиво изучающий содержимое ящиков на полке."
    ma "— Ого, так рано?"
    sa "— Чего-то не спалось. Так вот куда делись коптеры?"
    ma "— Да, стало интересно, можно ли их использовать как средства доставки."
    "Ага, просто стырила поиграться."
    sa "— А ты, [playerName], чего такой нерадостный?"
    "— Хм. Мой сон прервали взлётно-посадочные испытания."
    ma "— Посадочными они стали только после твоего вмешательства!"
    sa "— "
    return

label ch6revolve:
    "В комнату заходило всё больше людей. Судя по металлическому стуку, сопровождавшему их движения, многие были вооружены."
    "Мы сидели с Марией, спрятавшись под столом и пытаясь не издать ни звука."
    sa "– Ну всё, все ключевые узлы базы полностью под нашим контролем."
    sa "— Устранить всех, чья верность Инферно вызывает сомнения!"
    "Толпа в разнобой выразила возгласы одобрения."
    "Сердце стучало, как бешеное от страха быть замеченными, казалось, что его даже можно услышать."
    "Мария сжалась в комочек и закрыла лицо ладонями. Даже не знаю, за кого я переживаю больше..."
    "Так, значит, этот Саргон — какая-то большая шишка в Инферно? Если его убить, то моя месть будет считаться свершённой? Вряд ли всё так просто. Его место просто займёт кто-то другой."
    # pomis: вот только это лишь одно из управляемых тел Саргона.

    return