import random

amount_players = 0
while True:
    try:
    
        amount_players = int(input("Сколько игроков в игре?: "))
        break
            
    except:
        print("Упс! Введены неправильные символы.  Пробуйте снова...")

#Сколько игроков и ролей

#mafia = int(input("Сколько мафий в игре?: "))

#Создание списка игроков и перемещивание их
players = list(range(1, amount_players + 1))
random.shuffle(players)

#Выбор мафии
#mafia = [players.pop() for x in range(mafia)]
#Выбор доктора 
doctor = players.pop()
#Выбор детектива
#Выбор игрока с новой(ыми) ролями







""""Игра"""




















class Citizen(object):
    """Представляет гражданина."""
    def __init__(self, number, karma=0, city='', vote=0, checked=0):
        self.number = number
        self.karma = karma
        self.city = city_name
        self.vote = vote
        self.checked = checked
    karma_type = ['мирный', 'мафия', 'доктор']

    def __str__(self):
        return 'Гражданин #%s [%s]' % (self.number, Citizen.karma_type[self.karma])

class City(object):
    """Представляет собой город."""
    def __init__(self, name=''):
        self.citizens = []
        self.name = city_name
        mafia_count = 0
        import random
        for i in range(amount_players):
            citizen = Citizen(i+1)
            if mafia_count < 1:
                citizen.karma = random.randint(0, 1)
                if citizen.karma:
                    mafia_count = mafia_count + 1
            citizen.city = self.name
            self.citizens.append(citizen)
        self.mafia = [citizen for citizen in self.citizens if citizen.karma]
   
        
                
    def __str__(self):
        city = []
        for citizen in self.citizens:
            city.append(str(citizen))
        return 'Граждане of %s:\n' % (self.name) + '\n'.join(city)

    def city_life(self):
        """Управляет мафией, дежурством в комиссариате и ежедневным голосованием"""
       #Запускает операцию до тех пор, пока вся мафия или все мирные граждане не будут мертвы.
       #регулятор количества мафии в городе
        while len(self.citizens) - len(self.mafia) > 1 and len(self.mafia) != 0:
            print('Наступила ночь в', self.name,'City.')
            self.kill()
            skip = self.check()
            print('Наступил день, в', self.name,'City.')
            if skip:
                print('Никакого голосования на сегодня!\n')
                continue
            self.vote([i.number for i in self.citizens])
        #Выводит результат игры
        if len(self.mafia) == 0:
            print('Вся мафия была уничтожена! Вы выполнили свой долг комиссара.')
        else:
            self.kill()
            print('Мафия победила. Удачи в следующий раз!')

    def check(self):
        """Проверяет, является ли конкретный гражданин мирным или мафиози"""
        skip = False
        print('Время проверить! Доступные варианты проверки:\n')
        [print('Гражданин #'+str(i.number)) for i in self.citizens if not i.checked]
        print('\nДо сих пор вы проверяли:')
        [print(i) for i in self.citizens if i.checked]
        vote_user = int(input('\nПожалуйста, введите номер гражданина, которого вы хотите проверить.\n'))
        for i in self.citizens:
            if i.number == vote_user:
                print(str(i)+'\n')
                i.checked=True
                if i in self.mafia:
                    print('Поздравляю! Вы нашли мафиози.')
                    print('Завтрашний судебный процесс будет пропущен.\n')
                    for j in range(len(self.citizens)):
                        if self.citizens[j].number == i.number:
                            print(self.citizens.pop(j),'был казнен по праву.\n')
                            self.mafia.remove(i)
                            break
                    skip = True
        return skip

    def kill(self):
        """Случайным образом "убивает" мирного жителя"""
        import random
        killed = False
        while not killed:
            victim_num = random.randrange(len(self.citizens))
            if self.citizens[victim_num] not in self.mafia:
                print(self.citizens.pop(victim_num),'был убит мафией сегодня ночью.\n')
                killed = True

    def vote(self, vote_range):
        """Имитирует голосование за то, кто является мафией"""
        print('Время голосовать! Доступные варианты голосования:\n')
        [print('Гражданин #'+str(i)) for i in vote_range]
        print('\nДо сих пор вы проверяли:')
        [print(i) for i in self.citizens if i.checked]
        vote_user = int(input('\nПожалуйста, введите номер гражданина, за которого вы голосуете.\n'))
        import random
        for citizen in self.citizens:
            voted = False
            #Голос пользователя записан
            if citizen.number == vote_user:
                citizen.vote = citizen.vote + 1
            #Мафия голосует только за случайного мирного жителя
            if citizen.karma:
                while not voted:
                    vote_num = random.choice(vote_range)
                    if citizen.number != vote_num:
                        for votee in self.citizens:
                            if votee.number == vote_num and not votee.karma:
                                votee.vote = votee.vote + 1
                                voted = True
                                break
            #Мирные граждане случайным образом голосуют за тех, кто не был проверен
            else:
                while not voted:
                    vote_num = random.choice(vote_range)
                    if citizen.number != vote_num:
                        for votee in self.citizens:
                            if votee.number == vote_num and not votee.checked:
                                votee.vote = votee.vote + 1
                                voted = True
                                break
        #Вычисляет максимальное количество голосов и выдает результат (исполнение)
        self.maxVote()
        
    def maxVote(self):
        """Находит гражданина с наибольшим количеством голосов и казнит его"""
        max_vote = -1
        for citizen in self.citizens:
            if max_vote == citizen.vote:
                vote_range_local.append(citizen.number)
            if max_vote < citizen.vote:
                max_vote = citizen.vote
                vote_range_local = [citizen.number]
                global votee
                votee = citizen
        self.clearVotes()
        #Повторно инициирует голосование, если более одного гражданина набрали наибольшее количество голосов
        if len(vote_range_local) > 1:
            print('За нескольких граждан проголосовали одинаково. Повторное голосование!\n')
            self.vote(vote_range_local)
        #'Justfully' executes the unfortunate peaceful citizen or mafia member
        for i in range(len(self.citizens)):
                if self.citizens[i].number == votee.number:
                    print(self.citizens.pop(i),'был казнён по решению суда.\n')
                    if votee in self.mafia:
                        self.mafia.remove(votee)
                    break

    def clearVotes(self):
        """Отменяет предыдущее голосование"""
        for citizen in self.citizens:
            citizen.vote = 0
            
def printCity():
    """Выводит список граждан и их карму текущего города"""
    print(city_cur)

def game():
    """Давайте поиграем в мафию!"""
    global city_name
    while True:
        print('Привет! Вы - комиссар, которого перевели в город, коррумпированный мафией. Ваша задача внедриться в коррумпированную группировку и разврушить её из нутри.\n')
        city_name = str(input('Пожалуйста, введите название города.\n'))
        city_cur = City(city_name)
        city_cur.city_life()
        reply = str(input('Хотите поиграть еще раз? Y/N\n'))
        if reply == 'Y':
            break
game()
#Чтобы работала после вывода всех данных
time = input()

