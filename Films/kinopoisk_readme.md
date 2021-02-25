Получение информации о фильме по ID
Для поиска фильма по ID необходимо отсылать следующие параметры:

Для поиска фильма /movies/
Для поиска сериала /tv-series/
Id с кинопоиска фильма который ищите - /1143242/
Для работы апи необходимо указывать токен /token/<enteryour token>


Готовый пример запроса для получения информации о фильме "Джентельмены" https://api.kinopoisk.cloud/movies/1143242/token/<enter your token>


Получение всех фильмов и сериалов
Если вам нужен не какой-то конкретный фильм, а весь список фильмов базы (например вывести на своем сайте), то на этот случай есть постраничная плагинация

Для получения фильмов необходимо отсылать следующие параметры:

Для поиска фильма /movies/
Для поиска сериала /tv-series/
Номер страницы - all/page/1/
Для работы апи необходимо указывать токен /token/<enter your token>





Kinopoisk API returns data in JSON:

{
"id_kinopoisk": 915196,
"type": "tv-series",
"title": "Очень странные дела",
"title_alternative": "Stranger Things",
"poster": "https://cdn.kinopoisk.cloud/images/posters/tv-series/poster_id_915196.jpg",
"directors": [
	"Мэтт Даффер",
	"Росс Даффер",
	"Шон Леви"
],
"actors": [
	"Дэвид Харбор",
	"Финн Вулфард",
	"Милли Бобби Браун",
	"Гейтен Матараццо",
	"Наталия Дайер",
	"Чарли Хитон",
	"Джо Кири",
	"Вайнона Райдер",
	"Калеб Маклафлин",
	"Кара Буоно",
	"Денис Беспалый",
	"Тихон Ефименко",
	"Алиса Ефименко",
	"Прохор Тесленко",
	"Лина Иванова"
],
"screenwriters": [
	"Мэтт Даффер",
	"Росс Даффер",
	"Пол Дихтер"
],
"producers": [
	"Дэн Коэн",
	"Мэтт Даффер",
	"Росс Даффер"
],
"operators": [
	"Тим Айвз",
	"Тод Кэмпбелл",
	"Лачлан Милн"
],
"composers": [
	"Кайл Диксон",
	"Майкл Стейн"
],
"painters": [
	"Крис Трухильо",
	"Шон Бреннан",
	"Уильям Дж. Дэвис"
],
"editors": [
	"Дин Зиммерман",
	"Кевин Д. Росс",
	"Нэт Фуллер"
],
"genres": [
	"Ужасы",
	"Фантастика",
	"Фэнтези",
	"Триллер",
	"Драма",
	"Детектив"
],
"countries": [
	"США"
],
"year": 2016,
"description": "1980-е годы, тихий провинциальный американский городок. Благоприятное течение местной жизни нарушает загадочное исчезновение подростка по имени Уилл. Выяснить обстоятельства дела полны решимости родные мальчика и местный шериф, также события затрагивают лучшего друга Уилла  Майка. Он начинает собственное расследование. Майк уверен, что близок к разгадке, и теперь ему предстоит оказаться в эпицентре ожесточенной битвы потусторонних сил.",
"tagline": "«The world is turning upside down»",
"age": null,
"budget": null,
"rating_kinopoisk": "8.457",
"kinopoisk_votes": "108829",
"rating_imdb": "8.80",
"imdb_votes": "708933",
"fees_world": null,
"fees_russia": null,
"premiere_world": "11 июля 2016",
"premiere_russia": null,
"frames": [
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413471.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413470.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413469.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413468.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413467.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413466.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413465.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413464.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413463.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413462.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413461.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413460.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413459.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413458.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413457.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413456.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413455.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413454.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413453.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413452.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413451.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413450.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413449.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413448.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413447.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413446.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413445.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413444.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413443.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413442.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413441.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413440.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413439.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413438.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413437.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413436.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413435.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413434.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413433.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413432.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413431.jpg",
	"https://st.kp.yandex.net/im/kadr/3/4/1/kinopoisk.ru-Stranger-Things-3413430.jpg"
],
"screenshots": [
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3216821.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3216820.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3216819.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3216818.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3216817.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067658.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067657.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067656.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067655.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067654.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067653.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067652.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067651.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067650.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067649.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067648.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067647.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067646.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067645.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067644.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067643.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067642.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067641.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067640.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067639.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067638.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067637.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-3067636.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819159.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819158.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819157.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819156.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819155.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819154.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819153.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819152.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819151.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819150.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819149.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819148.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819147.jpg",
	"https://st.kp.yandex.net/im/kadr/3/2/1/kinopoisk.ru-Stranger-Things-2819146.jpg"
],
"seasons": "4"
}