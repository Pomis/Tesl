﻿# Вы можете расположить сценарий своей игры в этом файле. 

# Объявляйте изображения здесь, используя оператор image.
# например, image eileen happy = "eileen_happy.png"

# Определение сцен
image bg ocean = "images/ocean.jpg"
image bg sky = "images/sky.jpg"

# Определение персонажей игры.
define yu = Character('Юминг', color="#c8ffc8")
image yuming happy = "images/yuming.png"


# Игра начинается здесь.
label start:

    scene bg sky
    with fade
    "Я открыл глаза. Всего лишь небо и больше ничего. Слепяще белые облака. Ярко голубое пространство, простирающееся на миллиарды километров ввысь."
    "И звук ветра, затихающий и еле заметный. Я мог бы долго так лежать и любоваться красотой бесконечного космического океана, если бы не одна любопытная мысль, прешедшая мне в голову. "
    "\"А где я?\""
    
    "Хотя впрочем, мысль я особо развивать не стал."
    "Кругом так безмятежно, тихо и спокойно, что глаза сами закрылись. Ничего не мешает поспать ещё часок, разве что солнце припекает, да и покачивает меня почему-то.. опять качнуло. И вдруг я вспомнил."
    with vpunch
    "Так резко вскакивать всё же не стоило: я запутался в каких-то вещах и чуть не упал за борт. "
    scene bg ocean 
    with dissolve
    "Удержав равновесие, я поднял глаза и увидел океан. Впереди, слева, сзади -- кругом вода. Всё ещё не доконца соображая, я оглядел поверхность на котрой стою. "
    "Похоже это лодка. Большая рыжая резиновая лодка. В фильмах на таких спасаются люди, когда тонут корабли. Наш похоже как раз затонул. "
    
    "В голове начили вспыхивать образы прошедших событий: мельтешение людей, крики, большой круизный лайнер, накренившийся и обьятый огнём, яркие звёзды над головой и холодный ветер."
    "Картинки в моей голове сложились в целое и безысходность начала наполнять мою душу. "
    "\" Этого не может быть. нет-нет, это сон или всё что угодно, но это не реальность и происходит не со мной\""
    "Но внезапная волна, окатившая меня с головы до ног, смыла все мои мысли и пробудила от оцепенения. Надо что-то делать. Ведь я всё ещё жив."
    
    "Один я. Один океан. Кто кого? Я отбросил эти мысли и решил осмотреться."
    "Меня немного удивило, что лодка была завалена всяким барахлом, и при этом на ней был только я."
    "\"Обычно спасают людей, а не ценный груз. Но мне же лучше, может найду что поесть\"."
    "Однако надеждам моим не суждено было сбыться, на лодке были несколько кейсов с кодовыми замками, которые никак не открыть, валялась всякая одежда, какая-то странная конструкция, видимо являющаяся навесом для лодки и парочка спасательных жилетов."
    "Никакой аптечки, никаких пайков. Словом, ничего, что могло бы пригодиться в экстремальной ситуации. Как-будто этот плот вообще не расчитан на спасение людей." 
    "Ну и зачем он тогда? Я даже был немного возмущён, хотя, конечно, просто пытался таким образом подавить возросшую панику. "
    "Шансы на выживание таяли. Нет даже ракетницы, меня не заметят, если будут искать."
    "Прохаживаясь по палубе своего, похоже, последнего корабля, я задел что-то ногой. Из-под навеса торчал странный согнутый предмет, похожий на сапог." 
    "Я наклонился и попытался вытащить его, как вдруг понял, что это чья-то нога. Я не один."
    
    "Нога торчала из кучи барахла, состоящего из чемоданов, кейсов и прочего бесполезного в моей ситуации мусора."
    "Я начал раскидывать эту гору хлама, чтобы спасти того, кто был под ней. Спустя минуту упорного труда, я смог увидеть владельца ноги, точнее то, во что он был одет."
    "Это был странного вида скафандр, будто бы попавший сюда из какого-то фильма про пришельцев. "
    "Он был зелёного цвета, а шлем имел отражающую поверхность, что мешало увидеть лицо владельца этого странного костюма. "
    "Вдоль всего тела были странные твёрдые трубки, соединённые между собой гибкими трубками потоньше. Кажется, я видел в интернете что-то похожее."
    "Точно! Это называется экзоскелет. На да ладно, бог с этим экзоскелетом - что с человеком внутри. "
    "По идее, шлем в таких костюмах закрепляется либо электромагнитами, либо механически с помощью вращательного движения. "
    "В первом случае я не имел шансов его снять, но если же он закреплен вручную, то проблем быть не должно. Одно движение, щелчок и готово - шлем отделился от остального костюма. "
    "Я начал потихоньку снимать шлем и через несколько секунд передо мной предстало лицо молодой девкушки, на вид лет 16.\""
    show yuming happy
    with dissolve
    "Любопытство мнгновенно заглушило все мои страхи, я откинул навес и удивлённо уставился на того, кто был под ним."
    "Это определённо был человек, судя по комплекции даже наверно ребёнок, но вот одежда.. Вернее, одеждой это не назовёшь. Какой-то чёрный водолазный костюм с красивыми зелёными узорами и вставками. "
    "Но что это за шлем? Нет, это точно не водолазный костюм, слишком он странный, да и зачем дайверам сапоги?"
    "Я перевёл взгляд и с удивлением обнаружил что сзади из-под шлема выпадает прядь волос. Девушка?"

    "Я так увлёкся, разглядывая костюм, что не сразу подумал, что, возможно, ей нужна помощь. Что я могу сделать? Наверно, нужно снять с неё шлем. "
    "Это я и решил попробовать, но как только я протянул руки к шлему, девушка вдруг метнулась в сторону и мнгновение спустя я лежал и смотрел как хрупкое создание вдруг превратилось в доминирующий вид и на нашем плоту произошла маленькая революция."
    "Направленный на меня предмет я заметил не сразу, но в том что это оружие я не сомневался. Я посмотрел бы ей в глаза но мешал непрозрачный шлем. На несколько секунд наступило мёртвое молчание."
                                                                                                                                                                                                                

    return
