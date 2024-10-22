import time


class User:
    ''' nickname (имя пользователя, строка)
        password (в хэшированном виде, число)
        age (возраст, число)
    '''

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    ''' title (заголовок, строка)
        duration (продолжительность, секунды)
        time_now (секунда остановки, изначально 0)
        adult_mode (ограничение по возрасту, bool, False по умолчанию)
    '''

    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    ''' users (список объектов User)
        videos (список объектов Video)
        current_user (текущий пользователь, User)
    '''

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for us in self.users:
            if us.nickname == nickname and us.password == password:
                self.current_user = us

    def register(self, nickname, password, age):
        for us in self.users:
            if us.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for i in videos:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, search_word):
        search_word_lower = search_word.lower()
        result = [video.title for video in self.videos if search_word_lower in video.title.lower()]
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Начинается просмотр видео: {video.title}")
                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=' ', flush=True)
                    time.sleep(1)
                video.time_now = 0
                print("Конец видео")
                return

        print(f"Видео с названием {title} не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')