init:
    define ra = Character('Голос из рации', color="#e4e4e4")
    define pi = Character('Пилот', color="#e1e4e1")
    image bg entrace = "images/entrace.jpg"
    image bg mountains = "images/mountains.jpg"
    image bg mountains middle = "images/mountains-mid.png"
    image bg mountains forward = "images/mountains-front.png"
label warBase:
    scene bg mountains onlayer background
    show bg mountains forward onlayer forward at center
    show bg mountains middle onlayer middle
    $ camera_move(0, -2000, 0, 0, 0)
    $ camera_move(0, -2000, 1000, 0, 10, "easein")
    "Мы подлетали к небольшой горе и постепенно снижали скорость"
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
        