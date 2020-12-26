# Задание № 1. Наследование
# Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс
# студентов (вы можете взять этот код за основу или написать свой). Студентов пока
# оставим без изменения, а вот преподаватели бывают разные, поэтому теперь класс
# Mentor должен стать родительским классом, а от него нужно реализовать наследование
# классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания).
# Очевидно, имя, фамилия и список закрепленных курсов логично реализовать на уровне
# родительского класса. А чем же будут специфичны дочерние классы? Об этом в
# следующих заданиях.
#
# Задание № 2. Атрибуты и взаимодействие классов.
# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки
# за домашние задания. Теперь это могут делать только Reviewers (реализуйте такой
# метод)! А что могут делать лекторы? Получать оценки за лекции от студентов :)
# Реализуйте метод выставления оценок лекторам у класса Student (оценки по
# 10-балльной шкале, хранятся в атрибуте-списке). Лектор при этом должен быть
# закреплен за тем курсом, на который записан студент.
#
# Задание № 3. Полиморфизм и магические методы
# Перегрузите магический метод __str__ у всех классов.
#
# У проверяющих он должен выводить информацию в следующем виде:
#
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
#
# У лекторов:
#
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9
#
# А у студентов так:
#
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование
#
# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов
# по средней оценке за лекции и студентов по средней оценке за домашние задания.
#
# Задание № 4. Полевые испытания
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также
# реализуйте две функции:
#
# для подсчета средней оценки за домашние задания по всем студентам в рамках
# конкретного курса (в качестве аргументов принимаем список лекторо и название курса);
# для посдчета средней оценки за лекции всех лекторов в рамках конкретного курса
# (в качестве аргументов принимаем список студентов и название курса).
# #
# Задание № 4. Полевые испытания
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
#
# для подсчета средней оценки за домашние задания по всем студентам в рамках
# конкретного курса (в качестве аргументов принимаем список студентов и название курса);
# для подсчета средней оценки за лекции всех лекторов в рамках конкретного курса
# (в качестве аргументов принимаем список лекторов и название курса).

courses=['Python-22','Python-23','Python-24','Python-35','Python-36','C-22','C-23',
         'C-24','C++-22','C++-23','C++-24', 'Java-15','Java-16','Java-17','Javascript-1', 'Javascript-2',
         'NodeJs-2','NodeJs-3','React-3','React-4','Html&Css-1','Html&Css-2','Html&Css-3'] #Список курсов
students=[] #список всех студенгтов
reviewers =[] #проверяют задания
lectures =[] #Читают лекции

# students_with_grade=[]  #список всех студенгтов с баллом/оценкой
# students_without_grade=[] #список всех студенгтов без баллом/оценкой

lectures_with_grade=[]
lectures_without_grade=[]


class Students:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_rank = 0

    def descriptive_student(self):
        """Выводим описание стуента"""
        print("Имя :\t", self.name)
        print("Фамилия :\t", self.surname)
        print("Средняя оценка за домашние задания:\t", acount_average(self.grades))
        print("Курсы в процессе изучения:\t",(', '.join(self.courses_in_progress)))
        print("Завершенные курсы:\t", (', '.join(self.finished_courses)))

    def __repr__(self):
        return repr((self.name, self.grades_rank))

    def __lt__(self, other):
        return self.grades_rank < other.grades_rank

    def accounting_rank(self):
        self.grades_rank=acount_average(self.grades)

    def __str__(self):
        """Выводим описание стуента по объект класса """
        info_st=""
        info_st +="\nИмя :\t" + self.name
        info_st +="\nФамилия :\t" +self.surname
        info_st +="\nСредняя оценка за домашние задания:\t" + str(acount_average(self.grades))
        info_st +="\nКурсы в процессе изучения:\t" + (', '.join(self.courses_in_progress))
        info_st +="\nЗавершенные курсы:\t" + (', '.join(self.finished_courses))
        info_st +="\nОценки за курсы: "
        for key, value in self.grades.items():
            # info_st +="\n"+key+": "+(', '.join(str(value)))
            info_st += "\n\t" + key + ": " + "\t"+(str(value))
        return info_st

    def adding_course_in_progress(self,course):
        self.courses_in_progress.append(course)

    # Удаление курса из текущих
    def deleting_course(self, course):
        self.courses_in_progress.remove(course)

    # Перевод курса в законченные
    def adding_to_finished_course(self, course):
        self.courses_in_progress.remove(course)
        self.finished_courses.append(course)



    def rate_hw(self, lector, course, grade):

        # Студент ставит оценку Лектору
        if isinstance(lector, Lectures) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:

                lector.grades[course] += [grade]

            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'



def acount_average(grades):
    """Выводит по студентус/Лектору реднюю оценку за домашки/предметы по всем курсам."""
    if grades:
    # grades={'Python':[10,10,10], 'C':[10],'java':[10,20]}
        n=0
        sum=0
        for value in grades.values():
            for elem in value:
                n +=1
                sum +=elem
        a=sum/n
        a=round(a, 1)
        return a
    else:
       a= "Нет оценки"
       return a

def acount_average_course(course, students):
    """Выводит по студентус/Лектору реднюю оценку за домашки/предметы по всем курсам."""

    # grades={'Python':[10,10,10], 'C':[10],'java':[10,20]}
    # student1.grades = {'Python-22': [10, 10, 10], 'C++-23': [10], 'Javascript-2': [10, 6]}
    n=0
    sum=0
    for student in students:
        if student.grades:
            if course in student.grades:
                # print("Курс: ",course)
                values=student.grades[course]
                # print("Список оценок", values)
                for value in values:
                    # print ("Значение:",value)
                    n +=1
                    sum +=value
    if sum==0:
        # print("Оценок по данному курсу нет")
        a = 0
        return a
    else:
        a=sum/n
        a=round(a, 1)
        return a



# grades={'Python':[10,10,10], 'C':[10],'java':[10,20]}
# # grades={}
# a=acount_average_st(grades)
# print(a)






class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] # К каким курса прикреплен

    def accounting_rank(self):
        self.grades_rank=acount_average(self.grades)

    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #
    #             student.grades[course] +=[grade]
    #
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'

class Reviewers(Mentor):
    """Reviewers - ставят оценки за домашик студентов"""
    def __init__(self, name, surname):
        self.courses_attached = []
        """Инициализирует атрубуты класса родителя"""
        super().__init__(name, surname)

    def __str__(self):
        info_st = ""
        info_st += "\nИмя :\t" + self.name
        info_st += "\nФамилия :\t" + self.surname
        info_st += "\nКурирует курсы:\t" + (', '.join(self.courses_attached))

        return info_st


    def rate_hw(self, student, course, grade):
        #Ставит оценку студенту за курс
        if isinstance(student, Students) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:

                student.grades[course] +=[grade]

            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def adding_to_in_progress_course(self, course):
        self.courses_attached.append(course)

class Lectures(Mentor):
    """Lectures - ставят оценки за домашик студентов"""

    def __init__(self, name, surname):
        """Инициализирует атрубуты класса родителя"""
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []
        self.grades_rank = 0

    def accounting_rank(self):
        self.grades_rank=acount_average(self.grades)
    def __repr__(self):
        return repr((self.name, self.grades_rank))

    def __lt__(self, other):
        return self.grades_rank < other.grades_rank

    def __str__(self):
        info_st = ""
        info_st += "\nИмя :\t" + self.name
        info_st += "\nФамилия :\t" + self.surname
        info_st += "\nСредняя оценка за лекции:\t" + str(acount_average(self.grades))
        info_st += "\nЧитает курсы:\t" + (', '.join(self.courses_attached))
        info_st += "\nОценки за лекции: "
        for key, value in self.grades.items():
            # info_st +="\n"+key+": "+(', '.join(str(value)))
            info_st += "\n\t" + key + ": " + "\t" + (str(value))
        return info_st

    def adding_to_in_progress_course(self, course):
        self.courses_attached.append(course)


# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9


# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки
# за домашние задания. Теперь это могут делать только Reviewers (реализуйте такой
# метод)!
# У лекторов:
#
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9
#
# А у студентов так:
#
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

def starting_condition():
    # courses = ['Python-22', 'Python-23', 'Python-24', 'Python-35', 'Python-36', 'C-22', 'C-23',
    #            'C-24', 'C++-22', 'C++-23', 'C++-24', 'Java-15', 'Java-16', 'Java-17', 'Javascript-1',
    #            'Javascript-2','NodeJs-2', 'NodeJs-3', 'React-3', 'React-4', 'Html&Css-1', 'Html&Css-2',
    #            'Html&Css-3']
    #

    #Добавляем студентов
    student1=Students("Ruoy", "Eman", "Мужской")
    student1.finished_courses = ['Python-22','C++-23']
    student1.courses_in_progress = ["Javascript-2"]
    student1.grades = {'Python-22':[1,1,3], 'C++-23':[10],'Javascript-2':[10,6]}

    student2 = Students("Павел", "Астахальцев", "Мужской")
    student2.finished_courses = ['Javascript-2', 'C-24']
    student2.courses_in_progress = ["React-3"]
    student2.grades = {'Javascript-2': [5,5], 'C-24': [10]}

    student3 = Students("Ирина", "Петрова", "Женский")
    student3.finished_courses = ['Python-22']
    student3.courses_in_progress = ["Python-36"]
    student3.grades = {'Python-22':[5,5,10]}

    students.append(student1)
    students.append(student2)
    students.append(student3)

    #Добавляем Проверяющих Reviewers
    reviewer1=Reviewers("Анна", "Михайлова")
    reviewer1.courses_attached=['Python-22', 'Python-23', 'Python-24', 'Python-35', 'Python-36', 'Javascript-2']

    reviewer2 = Reviewers("Оксана", "Троегурова")
    reviewer2.courses_attached = ['C-22', 'C-23','C-24', 'C++-22', 'C++-23', 'C++-24']

    reviewer3 = Reviewers("Вадим", "Петров")
    reviewer3.courses_attached = ['Java-15', 'Java-16', 'Java-17', 'Javascript-1', 'Javascript-2']

    reviewer4 = Reviewers("Николай", "Метлов")
    reviewer4.courses_attached = ['NodeJs-2', 'NodeJs-3', 'React-3', 'React-4', 'Html&Css-1', 'Html&Css-2', 'Html&Css-3']

    reviewers.append(reviewer1)
    reviewers.append(reviewer2)
    reviewers.append(reviewer3)
    reviewers.append(reviewer4)

    # Добавляем Лекторов
    lector1 = Lectures("Олег", "Самосвалов")
    lector1.courses_attached = ['Python-22', 'Python-23', 'Python-24', 'Python-35', 'Python-36']
    lector1.grades = {'Python-22': [4,5,3,2,7], 'Python-23': [10,10,10],'Python-24': [10,10,10],'Python-35': [10,10,10],
                      'Python-36': [9,7] }

    lector2 = Lectures("Диана", "Тверская")
    lector2.courses_attached = ['Python-22','C-22', 'C-23', 'C-24', 'C++-22', 'C++-23', 'C++-24']
    lector2.grades = {'Python-22': [1,1,1,1,10],'C-22': [4, 5, 3, ],'C-23': [4, 5, 3, 2, 7, 9,2,6], 'C-24': [10, 10, 10,5,2], 'C++-22': [10, 10, 10],
                      'C++-23': [10, 10, 10], 'C++-24': [9, 7]}

    lector3 = Lectures("Ян", "Непомнящий")
    lector3.courses_attached = ['Java-15', 'Java-16', 'Java-17', 'Javascript-1', 'Javascript-2']
    lector3.grades = {'Java-15': [4, 5, 3,2,1,7 ], 'Java-16': [7, 9, 2, 6], 'Java-17': [10, 5, 2],
                      'Javascript-1': [10], 'Javascript-2': [10, 10, 10,7,4]}

    lector4 = Lectures("Диана", "Гурская")
    lector4.courses_attached = ['NodeJs-2', 'NodeJs-3', 'React-3', 'React-4', 'Html&Css-1', 'Html&Css-2',
                                  'Html&Css-3']
    lector4.grades = {'NodeJs-2': [4, 5, 3, 2, 1, 7], 'NodeJs-3': [7, 9, 2, 6], 'React-3': [10, 5, 2],
                      'React-4': [10], 'Html&Css-1': [10, 10, 10, 7, 4],'Html&Css-2': [10, 10, 10, 7, 4],'Html&Css-3': [10, 7, 4,1,2]}

    lectures.append(lector1)
    lectures.append(lector2)
    lectures.append(lector3)
    lectures.append(lector4)


    # courses = ['Python-22', 'Python-23', 'Python-24', 'Python-35', 'Python-36', 'C-22', 'C-23',
    #            'C-24', 'C++-22', 'C++-23', 'C++-24', 'Java-15', 'Java-16', 'Java-17', 'Javascript-1', 'Javascript-2',
    #            'NodeJs-2', 'NodeJs-3', 'React-3', 'React-4', 'Html&Css-1', 'Html&Css-2', 'Html&Css-3']

# A = ['red', 'green', 'blue']
# print(' '.join(A))
# print(''.join(A))
# print('***'.join(A))
# print(', '.join(A))


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
# best_student.courses_in_progress += ['с']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# cool_mentor.courses_attached += ['с']
#

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'с', 10)
#
# print(best_student.grades)

def is_digit(string):
    """Проверка ввода цифр"""
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def adding_first_last_name():
    name=[]

    check_first_name = True
    while check_first_name:
        name_first = input("\tВведите имя : ")
        if name_first == '':
            continue
        else:
            name.append(name_first)
            break

    check_last_name = True
    while check_last_name:
        name_last = input("\tВведите фамилию : ")
        if name_last == '':
            continue
        else:
            name.append(name_last)
            break
    return name


def adding_student():
    new_student=[]
    name=adding_first_last_name()
    print("name ", name)
    new_student.append(name[0])
    new_student.append(name[1])


    #Функция спрашивания имя, фамилию, пол , курс на который записывется студент.

    # Спрашивем пол
    sex = None
    while sex not in ("м", 'ж'):
        sex = input("Укажите пол (м/ж)").lower()


    new_student.append(sex)

    return new_student

#Функция добавления в класс Студентов  - нового студента
def adding_student_to_Students(first_name,last_name, sex):

    student_new=Students(first_name,last_name, sex )
    print(student_new)

    students.append(student_new)

#Функция добавления в класс Лекторов  - нового лектора
def adding_to_Lectors(first_name,last_name):

    lector_new=Lectures(first_name,last_name)
    print(lector_new)

    # lectures.append(lector_new)
    return lector_new

#Функция добавления в класс Проверяющего ДЗ  - нового revierws
def adding_to_Reviewers(first_name,last_name):

    reviewer_new=Reviewers(first_name,last_name)
    print(reviewer_new)

    # reviewers.append(reviewer_new)
    return reviewer_new

def descriprive_courses(cours):
    # Вывод курсов с порядковыми номерами по порядку
    if cours !=[]:
        n=0
        for cour in cours:
            n=n+1
            print(str(n),":","\tКурс:  ", cour)
    else:
        print("Список курсов пуст")



def descriprive_people(peoples):
    # Вывод людей по имени с порядковыми номерами по порядку
    if peoples != []:
        n = 0
        for people in peoples:
            n = n + 1
            print(str(n), ":", "\tИмя:  ", people.name," Фамилия: ", people.surname)
    else:
        print("Список курсов пуст")

def descriprive_people2(peoples, course):
    n = 0
    n_list=[]
    for people in peoples:
        n = n+1
        if course in people.courses_attached:
            print(str(n), ":", "\tИмя:  ", people.name, " Фамилия: ", people.surname)
            n_list.append(n)
    return n_list


    # courses_attached

#Функция спршиваем номер курса
def asking_num_course(courses):
    active = True
    while active:
        num_course = input("Введите номер курса: ")
        if is_digit(num_course) == True:
            if num_course.count('.') == 0:
                num_course = int(num_course)
            else:
                continue
            if (num_course > (len(courses))) or (num_course<=0):
                print("Такого номера нет, введите заново.")
                continue
            return num_course

#Функция спршиваем номер сткдента
def asking_num_student(students):
    active2 = True
    while active2:
        num_student = input("Введите номер студента: ")
        if is_digit(num_student) == True:
            if num_student.count('.') == 0:
                num_student = int(num_student)
            else:
                continue
            if (num_student > (len(students))) or (num_student <= 0):
                print("Такого номера нет, введите заново.")
                continue
            return num_student

def asking_num_lectures(lectures):
    active2 = True
    while active2:
        num_lector = input("Введите номер лектора: ")
        if is_digit(num_lector) == True:
            if num_lector.count('.') == 0:
                num_lector = int(num_lector)
            else:
                continue
            if (num_lector > (len(lectures))) or (num_lector <= 0):
                print("Такого номера нет, введите заново.")
                continue
            return num_lector

#Спрашиваем номер лектора или проверяюещего
def asking_num_mentor(question, mentors):
    active2 = True
    while active2:
        num_mentor = input(question)
        if is_digit(num_mentor) == True:
            if num_mentor.count('.') == 0:
                num_mentor = int(num_mentor)
            else:
                continue
            if (num_mentor > (len(mentors))) or (num_mentor <= 0):
                print("Такого номера нет, введите заново.")
                continue
            return num_mentor

#Функция спршиваем номер проверяющего
def asking_num_reviewers(reviewers):

    num_reviewer=None
    while num_reviewer not in reviewers:
        num_reviewer=input("Введите номер проверяющего: ")
        if is_digit(num_reviewer) == True:
            if num_reviewer.count('.') == 0:
                num_reviewer = int(num_reviewer)
            else:
                continue
    return num_reviewer



def ask_grade(question, low, high):
    active = True
    while active:
        grade = input(question)
        if is_digit(grade) == True:
            if grade.count('.') == 0:
                grade = int(grade)
                if grade==0:
                    break
                elif grade<0 or grade>high:
                    continue
                elif grade>=low or grade>=high:
                    return grade




            else:
                continue
    # grade=None
    # while grade not in range(low, high):
    #     grade = int(input(question))

    return grade

def adding_course(question1, question2):
    active=True

    while active:
        num_reviewer=input(question1)
        if num_reviewer=="":
            print(question2)
            continue

        else:
            return num_reviewer

def forming_grade(students):
    students_with_grade=[]
    students_without_grade=[]
    students_grade=[]
    for student in students:
        student.accounting_rank()
        # print(student.grades_rank)
        if type(student.grades_rank) == int or type(student.grades_rank)==float :

            students_with_grade.append(student)
        else:

            students_without_grade.append(student)
    students_grade.append(students_with_grade)
    students_grade.append(students_without_grade)
    return students_grade



def forming_grade_lectures(lectures):
    lectures_with_grade=[]
    lectures_without_grade=[]
    lectures_grade = []
    for lecture in lectures:
        lecture.accounting_rank()
        # print(lecture.grades_rank)
        if type(lecture.grades_rank) == int or type(lecture.grades_rank)==float :

            lectures_with_grade.append(lecture)
        else:

            lectures_without_grade.append(lecture)
    lectures_grade.append(lectures_with_grade)
    lectures_grade.append(lectures_without_grade)
    return lectures_grade

def main():
    starting_condition()

    choice=True
    while choice :
        print \
            ("""
                    Университет Нетологии.
            Введите команду 0-7:
                0 - Выйти
                1 - Вывести статус всех студентов
                2 - Вывести статус всех Лекторов
                3 - Вывести статус всех Rewiers (Проверяющие ДЗ)
                4 - Добавить студента 
                5 - Добавить новый курс студенту, 
                6 - Поставить оценку студенту за курс
                7 - Перевести курс студента в список законченных
                8 - Добавить новый курс и Вывести список всех курсов
                9 - Добавить новый курс Лектору и Проверяющему
                10 - Добавить/удалить Лектора и Добавить/удалить Rewiers
                11 - Поставить оценку Лектору за курс
                12 - подсчета средней оценки студентов и лекторов
                13 - Сравнить двух студентов по оценке (через магические методы).
                
                

            """)

        choice=input("Ваш выбор: ")
        print()
        #выход
        if choice =="0":
            print("До свидания.")
            break
        # 1 - общее кол-во животных
        elif choice =="1":
            print("Статус студентов:")
            for student in students:
                print(student)

        elif choice =="2":
            print("Статус Лекторов:")
            for lector in lectures:
                print(lector)

        elif choice =="3":
            print("Статус Проверяющих (Reviewers):")
            for reviewer in reviewers:
                print(reviewer)

        # 2 - состояние животных (mood)
        elif choice =="4":
            print("Добавляем студента, введите Имя, Фамилию и выберите пол:")
            name_st=adding_student()
            # print("name_st",name_st )
            adding_student_to_Students(name_st[0], name_st[1], name_st[2])

        elif choice == "5":


            choice5 = True
            while choice5:
                print \
                    ("""
                    Добавляем студенту новый курс в прогресс
                        0 - Вернуться назад
                        1 - Добавить студенту новый курс 
                        2 - Удалить курс из прогресса студента (если по ошибке добавили)
                        """)
                choice5 = input("Ваш выбор: ")
                print()
                # выход
                if choice5 == "0":
                    break
                elif choice5 == "1":
                    #Вывод списка студентов с номерами
                    #Вывод списка курсов с номерам
                    # Проверка  - нет ли у студента этого курса в Progress

                    #Добавление курса в прогресс
                    print("Добавление студенту нового курса.")
                    print("Список курсов:")
                    if courses:
                        descriprive_courses(courses)
                        num_course=asking_num_course(courses)
                        if students:
                            descriprive_people(students)
                            num_student=asking_num_student(students)

                            if courses[num_course-1] in students[num_student-1].courses_in_progress:
                                print("У студента уже стоит курс ",courses[num_course-1],"  в прогрессе")
                                break
                            else:
                                #Функция добавления
                                students[num_student-1].adding_course_in_progress(courses[num_course-1])
                                print("Курс  ",courses[num_course-1],"  добавили")
                                print(students[num_student-1])
                            break

                        else:
                            print("Список студентов пуст, создайте список")
                            break
                    else:
                        print("Список курсов пуст, создайте список")
                        break
                elif choice5 == "2":
                    if students:
                        descriprive_people(students)
                        num_student = asking_num_student(students)
                        # print("Выберите студента для удаления у него курса:")
                        if students[num_student-1].courses_in_progress:
                            descriprive_courses(students[num_student-1].courses_in_progress)


                            num_course = asking_num_course(students[num_student-1].courses_in_progress)
                            if students[num_student-1].courses_in_progress[num_course-1] in students[num_student-1].grades:
                                print("Нельзя удалить данный курс, по курсу получены оценки")
                            else:
                                students[num_student-1].deleting_course(students[num_student-1].courses_in_progress[num_course-1])
                                print(students[num_student-1])


                        else:
                            print("У данного студента нет курсовв в прогрессе")
                            # break
                    else:
                        print("Список студентов пуст, создайте список")
                        # break

                    #Удаление курса из списка курсов
                #Курс должен быть в списке текущих курсов
                # По курсу не долдно быть выставлено оценок



                else:
                    print("Извините, в меню нет пункта")
                    continue

        elif choice == "6":
            print("Выставление оценки студентов Reviewers")
            print("Выберите студента из списка по номеру:")
            #Выбор студента
            if students:
                descriprive_people(students)
                num_student = asking_num_student(students)
                #Выбор курса
                if students[num_student-1].courses_in_progress:
                    descriprive_courses(students[num_student-1].courses_in_progress)
                    num_course = asking_num_course(students[num_student-1].courses_in_progress)

                    num_course_2=students[num_student-1].courses_in_progress[num_course-1]
                    #Получили список проверющих данного курса
                    num_reviewers=descriprive_people2(reviewers, num_course_2)
                    if num_reviewers:
                    # Выбор reviewer из списка
                        num_reviewer=asking_num_reviewers(num_reviewers)


                        #Ставим оценку
                        grade=ask_grade("Введите оценку студенту от 1 до 10, 0 - чтобы вернуться обратно: ", 1, 10)
                        reviewers[num_reviewer-1].rate_hw(students[num_student-1], num_course_2, grade)
                        print (students[num_student-1])


                    else:
                        print("У курса нет проверяюих задание")


                else:
                    print("У студента нет текущих курсов")

            else:
                print("Список студентов пуст, создайте список")
        elif choice == "7":
            print("Перевести курс студента в список завершенных")
            if students:
                descriprive_people(students)
                num_student = asking_num_student(students)
                #Выбор курса
                if students[num_student-1].courses_in_progress:
                    descriprive_courses(students[num_student-1].courses_in_progress)
                    num_course = asking_num_course(students[num_student-1].courses_in_progress)

                    #Выбрали конкретный курс
                    num_course_2=students[num_student-1].courses_in_progress[num_course-1]
                    if num_course_2 in students[num_student-1].grades:
                        #Проверка  -  есть ли хотя бы одна оценка за курс
                        students[num_student - 1].adding_to_finished_course(num_course_2)
                        print("Курс ", num_course_2," переведен в список завершенных.")
                        print(students[num_student - 1])
                    else:
                        print("У студента этот курс не закончен, не получен ни одной оценки.")
                else:
                    print("У студнта нет текущих курсов.")

            else:
                print("Список студентов пуст, создайте список")


            # adding_course(courses)
        elif choice == "8":
            choice8 = True
            while choice8:
                print \
                    ("""
                    Добавляем новый курс в список курсов
                        0 - Вернуться назад
                        1 - Вывести списко всех курсов
                        2 - Добавляем новый курс в список курсов
                        """)
                choice8 = input("Ваш выбор: ")
                print()
                # выход
                if choice8 == "0":
                    break
                elif choice8 == "1":
                    print("Выводим список всех курсов")
                    descriprive_courses(courses)
                elif choice8 == "2":
                    print("Добавляем новый курс в список курсов")

                    if courses:
                        descriprive_courses(courses)
                        choice81=True
                        while choice81:

                            new_course=adding_course("Введите название нового курса: ","Название курса не может быть пустым.")
                            if new_course in courses:
                                print("Такой курс уже есть в списке курсов. Введите другой курс!")
                                continue
                            else:

                                courses.append(new_course)
                                break


                    else:
                        print("Список курсов пуст, создайте список")



        elif choice == "9":
            choice9 = True
            while choice9:
                print \
                    ("""
                        Добавляем новый курс лектру и проверяющему
                            0 - Вернуться назад
                            1 - Добавить новый курс Лекору
                            2 - Добавляем новый курс Проверяющему
                            """)
                choice9 = input("Ваш выбор: ")
                print()
                # выход
                if choice9 == "0":
                    break
                elif choice9 == "1":
                    print("Добавить новый курс Лектору")
                    if courses:

                        descriprive_courses(courses)
                        #Выбор курса
                        num_course = asking_num_course(courses)
                        num_course=courses[num_course-1]
                        # print("num_course", num_course)


                        # Выбор лектора из списка
                        if lectures:
                            descriprive_people(lectures)
                            num_reviewer = asking_num_mentor("Введите номер лектора: ", lectures)
                            # print("num_reviewe",num_reviewer )
                            if num_course in lectures[num_reviewer-1].courses_attached:
                                print("К сожалению у лектора уже есть данный курс.")
                            else:
                                lectures[num_reviewer-1].adding_to_in_progress_course(num_course)
                                print(lectures[num_reviewer-1])

                        else:
                            print("Список Лекторов пуст, создайте список лектров")
                    else:
                        print("Список курсов пуст, создайте список")


                elif choice9 == "2":
                    print("Добавить новый курс Ментору")
                    if courses:

                        descriprive_courses(courses)
                        #Выбор курса
                        num_course = asking_num_course(courses)
                        num_course=courses[num_course-1]

                        # Выбор лектора из списка
                        if reviewers:
                            descriprive_people(reviewers)
                            num_reviewer = asking_num_mentor("Введите номер проверяющего: ", reviewers)
                            if num_course in reviewers[num_reviewer-1].courses_attached:
                                print("К сожалению у проверяющего уже есть данный курс.")
                            else:
                                reviewers[num_reviewer-1].adding_to_in_progress_course(num_course)
                                print(reviewers[num_reviewer-1])

                        else:
                            print("Список Проверяющих пуст, создайте список проверяющих ДЗ")
                    else:
                        print("Список курсов пуст, создайте список")
        elif choice == "10":
            choice10 = True
            while choice10:
                print \
                    ("""
                        Добавляем нового лектора и проверяющего и удаляем их:
                            0 - Вернуться назад
                            1 - Добавить нового лектора
                            2 - Добавить нового Проверяющего дом.задания
                            3 - Удалить Лектора
                            4 - Удалить проверяющего  дом.задания
                            """)
                choice10 = input("Ваш выбор: ")
                print()
                # выход
                if choice10 == "0":
                    break
                elif choice10 == "1":
                    print("Добавить нового лектора")
                    name=adding_first_last_name()
                    lector_new=adding_to_Lectors(name[0], name[1])
                    lectures.append(lector_new)
                elif choice10 == "2":
                    print("Добавить нового проверяющего ДЗ")
                    name=adding_first_last_name()
                    reviewer_new=adding_to_Reviewers(name[0], name[1])
                    reviewers.append(reviewer_new)
                elif choice10 == "3":
                    print("Удалить Лектора:")
                    if lectures:
                        descriprive_people(lectures)
                        num_reviewer = asking_num_mentor("Введите номер лектора: ", lectures)
                        print("Удалили этого лектора: ")
                        print(lectures[num_reviewer-1])
                        lectures.remove(lectures[num_reviewer-1])
                    else:
                        print("Список Лекторов пуст, создайте список лектров")
                elif choice10 == "4":
                    print("Удалить проверяющего ДЗ:")
                    if reviewers:
                        descriprive_people(reviewers)
                        num_reviewer = asking_num_mentor("Введите номер лектора: ", reviewers)
                        print("Удалили этого проверяющего ДЗ: ")
                        print(reviewers[num_reviewer - 1])
                        reviewers.remove(reviewers[num_reviewer - 1])
                    else:
                        print("Список Проверяющих пуст, создайте список проверяющих ДЗ")

        elif choice == "11":
            choice11 = True
            while choice11:
                print \
                    ("""
                        Поставить оценку лектору:
                            0 - Вернуться назад
                            1 - Поставить оценку лектору
                            """)
                choice11 = input("Ваш выбор: ")
                print()
                # выход
                if choice11 == "0":
                    break
                elif choice11 == "1":
                    print("Поставить оценку лектору")

                    print("Выберите студента из списка по номеру:")
                    # Выбор студента
                    if students:
                        descriprive_people(students)
                        num_student = asking_num_student(students)
                        # Выбор курса
                        if students[num_student - 1].courses_in_progress:
                            descriprive_courses(students[num_student - 1].courses_in_progress)
                            num_course = asking_num_course(students[num_student - 1].courses_in_progress)

                            num_course_2 = students[num_student - 1].courses_in_progress[num_course - 1]
                            # Получили список проверющих данного курса
                            num_reviewers = descriprive_people2(lectures, num_course_2)
                            if num_reviewers:
                                # Выбор reviewer из списка
                                num_reviewer = asking_num_reviewers(num_reviewers)

                                # Ставим оценку

                                grade = ask_grade("Введите оценку лектору от 1 до 10, 0 - чтобы вернуться обратно: ",
                                                  1, 10)
                                print("Студент", students[num_student - 1])
                                print("лектор", lectures[num_reviewer - 1])
                                print("Курс", num_course_2)
                                print("Оценка", grade)
                                students[num_student - 1].rate_hw(lectures[num_reviewer - 1], num_course_2, grade)
                                print(lectures[num_reviewer - 1])


                            else:
                                print("У курса нет проверяюих задание")


                        else:
                            print("У студента нет текущих курсов, он не может ставить оценку лектору")

                    else:
                        print("Список студентов пуст, создайте список")
        elif choice == "12":
            choice12 = True
            while choice12:
                print \
                    ("""
                        Вывести средние оценки:
                            0 - Веруться обратно
                            1 - Студентов по выбранному курсу
                            2 - Лектров по конкретному курсу
                            """)
                choice12 = input("Ваш выбор: ")
                print()
                # выход
                if choice12 == "0":
                    break
                elif choice12 == "1":
                    print("Вывести средние оценки Студентов по выбранному курсу")
                    if courses:

                        descriprive_courses(courses)
                        #Выбор курса
                        num_course = asking_num_course(courses)
                        num_course=courses[num_course-1]
                        averag_value=acount_average_course(num_course, students)
                        if averag_value==0:
                            print("Оценок по данному курсу нет!")

                        else:
                            print("Средняя оценка всех студегнтов по курсу ",num_course, ": ",  averag_value)

                    else:
                        print("Список курсов пуст, создайте список")
                elif choice12 == "2":
                    print("Вывести средние оценки лекторов по выбранному курсу")
                    if courses:

                        descriprive_courses(courses)
                        #Выбор курса
                        num_course = asking_num_course(courses)
                        num_course=courses[num_course-1]
                        averag_value=acount_average_course(num_course, lectures)
                        if averag_value==0:
                            print("Оценок лекторов по данному курсу нет!")

                        else:
                            print("Средняя оценка всех лекторов по курсу ",num_course, ": ",  averag_value)

                    else:
                        print("Список курсов пуст, создайте список")
        elif choice == "13":
            choice13 = True
            while choice13:
                print \
                    ("""
                        Вывести средние оценки:
                            0 - Вернуться обратно
                            1 - Выбрать двух студентов для сравнения
                            2 - Выбрать двух лекторов для сравнения
                            """)
                choice13 = input("Ваш выбор: ")
                print()
                # выход
                if choice13 == "0":
                    break
                elif choice13 == "1":
                      # список всех студенгтов без баллом/оценкой

                    students_grade=forming_grade(students)
                    print("Выбрать двух студентов c оценками для сравнения")
                    students_with_grade=students_grade[0]

                    if len(students_with_grade)>1:
                        descriprive_people(students_with_grade)
                        print("Введите номер двух студентов для сравнения:")
                        print("Введите номер первого студента:")
                        num_student1 = asking_num_student(students_with_grade)
                        print("Введите номер второго студента:")
                        active=True
                        while active:
                            num_student2 = asking_num_student(students_with_grade)
                            if num_student2==num_student1:
                                continue
                            else:
                                break

                        if (students_with_grade[num_student1-1] > students_with_grade[num_student2-1]):
                            print("Оценка первого студента больше второго",students_with_grade[num_student1-1].grades_rank,">",students_with_grade[num_student2-1].grades_rank)
                        elif (students_with_grade[num_student1 - 1] < students_with_grade[num_student2 - 1]):
                                print("Оценка первого студента меньше второго", students_with_grade[num_student1 - 1].grades_rank, "<",
                                      students_with_grade[num_student2 - 1].grades_rank)
                        else:
                            print("Оценка первого студента равна оценке второго", students_with_grade[num_student1 - 1].grades_rank, "=",
                                  students_with_grade[num_student2 - 1].grades_rank)

                    else:
                        print("Список студентов пуст, создайте список")
                elif choice13 == "2":

                    lectures_grade=forming_grade_lectures(lectures)
                    print("Выбрать двух Лекторов c оценками для сравнения")
                    lectures_with_grade = lectures_grade[0]

                    if len(lectures_with_grade)>1:
                        descriprive_people(lectures_with_grade)
                        print("Введите номер двух лекторов для сравнения:")
                        print("Введите номер первого лектора:")
                        num_lector1 = asking_num_lectures(lectures_with_grade)
                        print("Введите номер второго лектора:")
                        active=True
                        while active:
                            num_lector2 = asking_num_lectures(lectures_with_grade)
                            if num_lector2==num_lector1:
                                continue
                            else:
                                break

                        if (lectures_with_grade[num_lector1-1] > lectures_with_grade[num_lector2-1]):
                            print("Оценка первого лектора больше второго",lectures_with_grade[num_lector1-1].grades_rank,">",lectures_with_grade[num_lector2-1].grades_rank)
                        elif (lectures_with_grade[num_lector1 - 1] < lectures_with_grade[num_lector2 - 1]):
                                print("Оценка первого лектора меньше второго", lectures_with_grade[num_lector1 - 1].grades_rank, "<",
                                      lectures_with_grade[num_lector2 - 1].grades_rank)
                        else:
                            print("Оценка первого студента равна оценке второго", lectures_with_grade[num_lector1 - 1].grades_rank, "=",
                                  lectures_with_grade[num_lector2 - 1].grades_rank)

                    else:
                        print("Список лекторов пуст или меньше 1 , создайте список")
        # # 6 - Поставить  оценку  студенту   за   курс
        else:
            print("Извините, в меню нет пункта")
main()