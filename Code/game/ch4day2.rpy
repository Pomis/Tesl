label ch4day2:
    # pomis: ГГ не уплыл с Марией в Америку, не уплыл в Инферно с Павлом, не встретил Энлиль.
    # pomis: ГГ возможно замутил с Минори, а, возможно, нет.
    # bulka: Минори Шрёдингера?
    # pomis: ГГ Шрёдингера. Мы же не знаем, каких делов он натворил, перед тем, как попал в этот момент
    # pomis: Юминг жива, а Мария уплыла в Америку. 
    if celebratedVictory:
        "О боже, только не утро..." with opening
        call flashback5
        sl "— Вставай, ленивый кусок! Пора вершить великие дела!"
        "А, вот оно что... Но всё же, странно."
        "— Какие ещё дела? У тебя есть вода?"
        if slavaPoints>1:
            sl "— Для тебя всегда найдётся... Слава достал из сумки бутылку газировки и протянул мне."
            "— Благодарю."
        else:
            sl "— В кране есть вода. Вставай!"
            "— Да чего такой настойчивый?"
    else:
        "Вот и утро настало... {w}Похоже, Слава не смог доползти до кровати. Что же вчера произошло?"
    "Пойду, умоюсь..."
    "Когда я вернулся в комнату, Слава делал зарядку."
    if celebratedVictory==False:
        sl "— Зря вчера не пошёл с нами. Весело было!"
        "— Что-то сомневаюсь."
    if stoodForIscra:
        "Интересно, он злится на меня? Я заступился за его врага. {w}Или не помнит?"
        "Думаю, помнит. Не так уж и много мы выпили."
        "Да и хрен с ним, честно."
    "— Что будет сегодня?"
    sl "— А кто его знает..."
    # pomis: вот пока вообще хз куда направлять сюжет