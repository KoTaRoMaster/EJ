import pymysql
import config
from datetime import datetime


class Connect:
    def __init__(self):
        self.connection = None
        self.attempts = 0
        self.connect()

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=config.host,
                user=config.user,
                password=config.password,
                database=config.db_name
            )
            self.cursor = self.connection.cursor()
            print('Succses connect..')
        except Exception as ex:
            print('Connect refused..')
            print(ex)
            # if self.attempts > 3:
            #     print("Can't connect to server..")
            #     print("Leaving...")
            #     return 'off'
            #
            # for i in range(3, 0, -1):
            #     print(f'Reconnect after {i}')
            #     sleep(1)
            # else:
            #     self.attempts += 1
            #     print('Try to connect..')
            #     self.connect()

    def get_users(self):
        try:
            query = "SELECT * FROM `users`"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_users

    def get_user(self, email):
        try:
            query = ("SELECT * FROM `users`"
                     f"WHERE `email`='{email}'")
            self.cursor.execute(query)
            row = self.cursor.fetchone()
            # print(row)
            return row
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_user(email)

    def registration_user(self, email, password):
        try:
            query = (f"UPDATE `users` as u SET u.password = '{password}' WHERE u.email = '{email}'")
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_user(email)

    def insert_users(self):
        try:
            insert_students_query = ("INSERT INTO `users` (`email`,`type`) "
                                     "SELECT `email`,`type` "
                                     "FROM `students` as s "
                                     "WHERE NOT EXISTS(SELECT * FROM `users` as u  WHERE s.email = u.email) "
                                     "AND s.email IS NOT NULL")
            self.cursor.execute(insert_students_query)
            self.connection.commit()

            insert_teachers_query = ("INSERT INTO `users` (`email`,`type`) "
                                     "SELECT `email`,`type` "
                                     "FROM `teachers` as t "
                                     "WHERE NOT EXISTS(SELECT * FROM `users` as u  WHERE t.email = u.email) "
                                     "AND t.email IS NOT NULL")
            self.cursor.execute(insert_teachers_query)

            self.connection.commit()
            print('Insert users complete')
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_users

    def get_students_all(self):
        try:
            query = ("SELECT * FROM `students`")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #   print(row)
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_students_all()

    def get_students_group(self, group):
        try:
            query = ("SELECT s.first_name, s.name, s.second_name "
                     "FROM `students` as s "
                     f"WHERE s.group_id = (SELECT g.id FROM `groups` as g WHERE g.group = '{group}')")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_students_group(group)

    def get_student(self, email):
        try:
            query = ("SELECT s.name, s.first_name, s.second_name, s.email, g.group FROM `students` as s "
                     "JOIN `groups` as g ON g.id = s.group_id "
                     f"WHERE s.email = '{email}'")
            self.cursor.execute(query)
            row = self.cursor.fetchone()
            # print(row)
            return row
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_student(email)

    def get_teachers(self):
        try:
            query = "SELECT * FROM `teachers`"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #      print(row)
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_teachers()

    def get_teacher(self, email):
        try:
            query = ("SELECT * FROM `teachers`"
                     f"WHERE `email`='{email}'")
            self.cursor.execute(query)
            row = self.cursor.fetchone()
            # print(row)
            return row
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_teacher(email)

    def get_admins(self):
        try:
            query = "SELECT * FROM `admins`"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #   print(row)
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_admins()

    def get_admin(self, email):
        try:
            query = ("SELECT * FROM `admins`"
                     f"WHERE `email`='{email}'")
            self.cursor.execute(query)
            row = self.cursor.fetchone()
            # print(row)
            return row
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_admin(email)

    def get_lessons_student(self, email):
        try:
            query = ("SELECT l.id, l.lesson "
                     "FROM `lessons` as l "
                     "JOIN `group_lessons` as g_l ON l.id = g_l.lesson_id "
                     "JOIN `students` as s ON s.group_id = g_l.group_id "
                     f"WHERE s.email = '{email}'"
                     "ORDER BY l.lesson")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #      print(row)
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_lessons_student(email)

    def get_date_rating_student(self, group):
        try:
            query = ("SELECT DISTINCT sch.date "
                     "FROM `schedule` as sch "
                     "JOIN `groups` as g ON g.id = sch.group_id "
                     f"WHERE g.group = '{group}'"
                     "ORDER BY sch.date")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            rows_ = []
            for row in rows:
                rows_.append(row[0])
            return rows_
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_date_rating_student(group)

    def get_assessment_rating_student(self, email):
        try:
            query = ("SELECT l.lesson, r.assessment, r.date "
                     "FROM `rating` as r "
                     f"JOIN `students` as s ON s.id = r.student_id and s.email = '{email}' "
                     "JOIN `lessons` as l On l.id = r.lesson_id "
                     "ORDER BY r.date, l.lesson")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #      print(row)
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_assessment_rating_student(email)

    def get_lessons_teacher(self, email):
        try:
            query = ("SELECT l.lesson, l.index "
                     "FROM `lessons` as l "
                     "JOIN `teacher_lessons` as t_l ON l.id = t_l.lesson_id "
                     "JOIN `teachers` as t ON t.id = t_l.teacher_id "
                     f"WHERE t.email = '{email}'")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #      print(row)
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_lessons_teacher(email)

    def get_groups_lesson(self, lesson):
        try:
            query = ("SELECT DISTINCT g.group "
                     "FROM `group_lessons` as g_l "
                     "JOIN `groups` as g ON g.id = g_l.group_id "
                     "JOIN `lessons` as l ON l.id = g_l.lesson_id "
                     f"WHERE l.lesson = '{lesson}'")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            rows_ = []
            for row in rows:
                rows_.append(row[0])
            return rows_
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_groups_lesson(lesson)

    def get_groups_date_lesson(self, group, lesson):
        try:
            query = ("SELECT DISTINCT sch.date "
                     "FROM `schedule` as sch "
                     "JOIN `lessons` as l ON l.id = sch.lesson_id "
                     "JOIN `groups` as g ON g.id = sch.group_id "
                     f"WHERE g.group = '{group}' "
                     f"AND l.lesson = '{lesson}' "
                     f"ORDER BY sch.date")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            rows_ = []
            for row in rows:
                rows_.append(row[0])
            return rows_
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_groups_date_lesson(group, lesson)

    def get_groups_rating_lesson(self, group, lesson):
        try:
            query = ("SELECT s.first_name, s.name, s.second_name, r.assessment, r.date "
                     "FROM `rating` as r "
                     "JOIN `lessons` as l ON r.lesson_id = l.id "
                     "JOIN `students` as s ON s.id = r.student_id "
                     "JOIN `groups` as g ON g.id = s.group_id "
                     f"WHERE g.group = '{group}' "
                     f"AND l.lesson = '{lesson}' "
                     "ORDER BY r.date")

            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #     print(row)
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_groups_rating_lesson(group, lesson)

    def update_rating_group(self, assessments, date, name, group, lesson):
        try:

            name_ = name.split(' ')
            sName = name_[1]
            sFirstName = name_[0]
            sSecondName = name_[2]
            date_ = '2024.' + date

            query = ("DELETE r FROM `rating` as r "
                     "JOIN `students` as s ON s.id = r.student_id "
                     "JOIN `lessons` as l ON l.id = r.lesson_id "
                     "JOIN `groups` as g ON g.id = s.group_id "
                     f"WHERE g.group = '{group}' "
                     f"AND l.lesson = '{lesson}' "
                     f"AND r.date = '{date_}' "
                     f"AND s.name = '{sName}' "
                     f"AND s.first_name = '{sFirstName}' "
                     f"AND s.second_name = '{sSecondName}'")
            self.cursor.execute(query)
            self.connection.commit()

            if len(assessments) == 0:
                return

            for i in range(len(assessments)):
                query = ("INSERT INTO `rating` (`student_id`, `lesson_id`, `assessment`, `count_id`, `date`) VALUES("
                         f"(SELECT s.id FROM `students` as s "
                         f"JOIN `groups` as g ON g.id = s.group_id "
                         f"WHERE s.name = '{sName}' AND s.first_name = '{sFirstName}' AND s.second_name = '{sSecondName}' AND g.group = '{group}' ), "
                         f"(SELECT l.id FROM `lessons` as l WHERE l.lesson = '{lesson}'), "
                         f"{assessments[i]}, "
                         f"{i}, "
                         f"'{date_}')")
                self.cursor.execute(query)
                self.connection.commit()

        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.update_rating_group(assessments, date, name, group, lesson)

    def get_schedule_admin(self, date):
        try:
            query = ("SELECT l.lesson, l.index, g.group, sch.id_count, sch.date "
                     "FROM `schedule` as sch "
                     "JOIN `lessons` as l ON l.id = sch.lesson_id "
                     "JOIN `groups` as g ON g.id = sch.group_id "
                     f"WHERE sch.date = '{date}' "
                     "ORDER BY g.group, sch.id_count")

            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #     print(row)
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_schedule_admin(date)

    def get_all_groups(self):
        try:
            query = ("SELECT `group` "
                     "FROM `groups` "
                     "ORDER BY `group`")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            rows_ = []
            for row in rows:
                rows_.append(row[0])
            return rows_
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_all_groups()

    def get_lessons_group(self, group):
        try:
            query = ("SELECT DISTINCT l.lesson, l.index, t.name, t.first_name, t.second_name, g.group "
                     "FROM `lessons` AS l "
                     "JOIN `group_lessons` AS g_l ON g_l.lesson_id = l.id "
                     "JOIN `teacher_lessons` AS t_l ON t_l.lesson_id = l.id "
                     "JOIN `teachers` AS t ON t.id = t_l.teacher_id "
                     "JOIN `groups` AS g ON g.id = g_l.group_id "
                     f"WHERE g.group = '{group}'")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #     print(row)
            # print('*'*20)
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_lessons_group(group)

    def get_schedule_group(self, date, group, id_count):
        try:
            query = ("SELECT l.lesson, g.group, sch.id_count, sch.date "
                     "FROM `schedule` as sch "
                     "JOIN `lessons` as l ON sch.lesson_id = l.id "
                     "JOIN `groups` as g ON g.id = sch.group_id "
                     f"WHERE sch.date = '{date}' "
                     f"AND g.group = '{group}' "
                     f"AND sch.id_count = '{id_count}'")
            self.cursor.execute(query)
            row = self.cursor.fetchone()
            # print(row)
            return row
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_schedule_group(date, group, id_count)

    def insert_schedule(self, date, group, lesson, id_count):
        try:
            query = ("INSERT INTO `schedule` (`lesson_id`, `group_id`, `id_count`, `date`) VALUES("
                     f"(SELECT l.id FROM lessons as l WHERE l.lesson = '{lesson}'), "
                     f"(SELECT g.id FROM `groups` as g WHERE g.group = '{group}'), "
                     f"{id_count}, "
                     f"'{date}' )")
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.insert_schedule(date, group, lesson, id_count)

    def update_schedule(self, date, group, lesson, id_count):
        try:
            query = ("UPDATE `schedule` as sch SET sch.lesson_id = ("
                     "SELECT `id` FROM `lessons` "
                     f"WHERE `lesson` = '{lesson}') "
                     f"WHERE sch.group_id = (SELECT g.id FROM `groups` as g WHERE g.group = '{group}') "
                     f"AND sch.id_count = '{id_count}' "
                     f"AND sch.date = '{date}'")
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.update_schedule(date, group, lesson, id_count)

    def delete_schedule(self, date, group, id_count):
        try:
            query = ("DELETE sch FROM `schedule` as sch "
                     "JOIN `groups` as g ON g.id = sch.group_id "
                     f"WHERE g.group = '{group}' "
                     f"AND sch.id_count = '{id_count}' "
                     f"AND sch.date = '{date}'")
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.delete_schedule(date, group, id_count)

    def insert_student(self, name, email, group):
        try:
            name_ = name.split(' ')
            sName = name_[1]
            sFirstName = name_[0]
            sSecondName = ''
            if len(name_) == 3:
                sSecondName = name_[2]
            insert_students_query = ("INSERT INTO `students` (`name`, `first_name`, `second_name`, `email`, `group_id`)"
                                     f"VALUES('{sName}','{sFirstName}','{sSecondName}','{email}',(SELECT g.id FROM `groups` as g WHERE g.group = '{group}'))")
            self.cursor.execute(insert_students_query)

            insert_students_user_query = (f"INSERT INTO `users` (`email`, `type`) VALUES('{email}','student')")
            self.cursor.execute(insert_students_user_query)
            self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.insert_student(name, email, group)

    def delete_student(self, email):
        try:
            query = (f"SELECT s.id FROM `students` as s WHERE s.email = '{email}'")
            self.cursor.execute(query)
            student_id = self.cursor.fetchone()[0]

            delete_student_query = (f"DELETE s FROM `students` as s WHERE s.id = '{student_id}'")
            self.cursor.execute(delete_student_query)

            delete_student_rating_query = (f"DELETE r FROM `rating` as r WHERE r.student_id = '{student_id}'")
            self.cursor.execute(delete_student_rating_query)

            delete_student_user_query = (f"DELETE u FROM `users` as u WHERE u.email = '{email}'")
            self.cursor.execute(delete_student_user_query)

            self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.delete_student(email)

    def update_student(self, name, email, group, prevName, prevEmail, prevGroup):
        try:
            name_ = name.split(' ')
            sName = name_[1]
            sFirstName = name_[0]
            sSecondName = name_[2]

            prevName_ = prevName.split(' ')
            pName = prevName_[1]
            pFirstName = prevName_[0]
            pSecondName = prevName_[2]

            emailQuery = (f"AND `email` IS NULL ")
            if prevEmail:
                emailQuery = (f"AND `email` = '{prevEmail}' ")

            query = (f"UPDATE `students` as s SET s.name = '{sName}', "
                     f"s.first_name = '{sFirstName}', "
                     f"s.second_name = '{sSecondName}', "
                     f"s.email = '{email}', "
                     f"s.group_id = (SELECT g.id FROM `groups` as g WHERE g.group = '{group}') "
                     f"WHERE s.name = '{pName}' "
                     f"AND s.first_name = '{pFirstName}' "
                     f"AND s.second_name = '{pSecondName}' "
                     f"{emailQuery}")
            self.cursor.execute(query)

            # update_user_query = (f"UPDATE u FROM `users` as u SET s.email = '{email}' WHERE u.email = '{prevEmail}'")
            # self.cursor.execute(update_user_query)
            self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.update_student(name, email, group, prevName, prevEmail, prevGroup)

    def get_group_teacher(self, email):
        try:
            query = ("SELECT `group` "
                     "FROM `groups` AS g "
                     "JOIN `group_teachers` as g_t ON g_t.group_id = g.id "
                     "JOIN `teachers` as t On g_t.teacher_id = t.id "
                     f"WHERE t.email = '{email}'")
            self.cursor.execute(query)
            row = self.cursor.fetchone()
            if not row:
                return ''
            return row[0]
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_group_teacher(email)

    def get_all_lessons(self):
        try:
            query = ("SELECT `lesson`, `index` "
                     "FROM `lessons` "
                     "ORDER BY `lesson`")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_all_lessons()

    def insert_teacher(self, name, email, lessons, group):
        try:

            name_ = name.split(' ')
            sName = name_[1]
            sFirstName = name_[0]
            sSecondName = ''
            if len(name_) == 3:
                sSecondName = name_[2]

            insert_teacher_query = ("INSERT INTO `teachers` (`name`, `first_name`, `second_name`, `email`) "
                                    f"VALUES('{sName}','{sFirstName}','{sSecondName}','{email}')")
            self.cursor.execute(insert_teacher_query)

            insert_group_teacher_query = ("INSERT INTO `group_teachers` (`group_id`, `teacher_id`) "
                                          f"VALUES((SELECT g.id FROM `groups` as g WHERE g.group = '{group}'), "
                                          f"(SELECT t.id FROM `teachers` as t WHERE t.name = '{sName}' AND t.first_name = '{sFirstName}' AND t.second_name = '{sSecondName}'))")
            self.cursor.execute(insert_group_teacher_query)

            for lesson in lessons:
                insert_teacher_lesson_query = ("INSERT INTO `teacher_lessons` (`teacher_id`, `lesson_id`) "
                                               f"VALUES((SELECT t.id FROM `teachers` as t WHERE t.name = '{sName}' AND t.first_name = '{sFirstName}' AND t.second_name = '{sSecondName}'),"
                                               f"(SELECT l.id FROM `lessons` as l WHERE l.lesson = '{lesson}'))")
                self.cursor.execute(insert_teacher_lesson_query)

            insert_teacher_user_query = (f"INSERT INTO `users` (`email`, `type`) VALUES('{email}','teacher')")
            self.cursor.execute(insert_teacher_user_query)
            self.connection.commit()
            self.insert_users()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.insert_teacher(name, email, lessons, group)

    def delete_teacher(self, email):
        try:
            query = (f"SELECT t.id FROM `teachers` as t WHERE t.email = '{email}'")
            self.cursor.execute(query)
            teacher_id = self.cursor.fetchone()[0]

            delete_teacher_query = (f"DELETE FROM `teachers` WHERE `id` = '{teacher_id}'")
            self.cursor.execute(delete_teacher_query)

            delete_group_teacher_query = (f"DELETE FROM `group_teachers` WHERE `teacher_id` = '{teacher_id}'")
            self.cursor.execute(delete_group_teacher_query)

            delete_teacher_lesson_query = (f"DELETE FROM `teacher_lessons` WHERE `teacher_id` = '{teacher_id}'")
            self.cursor.execute(delete_teacher_lesson_query)

            delete_teacher_user_query = (f"DELETE FROM `users` WHERE `email` = '{email}'")
            self.cursor.execute(delete_teacher_user_query)
            self.connection.commit()

            # return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.delete_teacher(email)

    def update_teacher(self, name, email, lessons, group, prevEmail):
        try:
            name_ = name.split(' ')
            sName = name_[1]
            sFirstName = name_[0]
            sSecondName = ''

            if len(name_) == 3:
                sSecondName = name_[2]

            query = (f"SELECT t.id FROM `teachers` as t WHERE t.email = '{prevEmail}'")
            self.cursor.execute(query)
            teacher_id = self.cursor.fetchone()[0]

            update_teacher_query = (f"UPDATE `teachers` as t SET t.name = '{sName}', "
                                    f"t.first_name = '{sFirstName}', "
                                    f"t.second_name = '{sSecondName}', "
                                    f"`email` = '{prevEmail}' "
                                    f"WHERE t.id = '{teacher_id}'")
            self.cursor.execute(update_teacher_query)

            update_group_teacher = (f"UPDATE `group_teachers` as g_t SET g_t.group_id = "
                                    f"(SELECT g.id FROM `groups` as g WHERE g.group = '{group}') "
                                    f"WHERE g_t.teacher_id = '{teacher_id}'")
            self.cursor.execute(update_group_teacher)

            query = (f"DELETE t_l FROM `teacher_lessons` as t_l WHERE t_l.teacher_id = '{teacher_id}'")
            self.cursor.execute(query)
            self.connection.commit()

            for lesson in lessons:
                lesson_ = ' '.join(lesson.split()[:-1])

                insert_teacher_lessons_query = (
                    f"INSERT INTO `teacher_lessons` (`teacher_id`, `lesson_id`) VALUES('{teacher_id}', "
                    f"(SELECT l.id FROM `lessons` as l WHERE l.lesson = '{lesson_}'))")
                self.cursor.execute(insert_teacher_lessons_query)
            self.connection.commit()
            self.insert_users()

        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.update_teacher(name, email, lessons, group, prevEmail)

    def get_group_id(self, group):
        try:
            query = ("SELECT g.id "
                     "FROM `groups` as g "
                     f"WHERE g.group = '{group}'")
            self.cursor.execute(query)
            row = self.cursor.fetchone()
            return row
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_group_id(group)

    def insert_group(self, group, lessons):
        try:
            insert_group_query = (f"INSERT INTO `groups` (`group`) VALUES('{group}')")
            self.cursor.execute(insert_group_query)

            lessons_ = lessons.split('\n')
            for lesson in lessons_:
                lesson_ = ' '.join(lesson.split()[:-1])

                insert_group_lessons_query = (
                    f"INSERT INTO `group_lessons` (`group_id`, `lesson_id`) VALUES((SELECT g.id FROM `groups` as g WHERE g.group = '{group}'), "
                    f"(SELECT l.id FROM `lessons` as l WHERE l.lesson = '{lesson_}'))")
                self.cursor.execute(insert_group_lessons_query)

            self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.insert_group(group, lessons)

    def delete_group(self, group):
        try:
            query = (f"SELECT g.id FROM `groups` as g WHERE g.group = '{group}'")
            self.cursor.execute(query)
            group_id = self.cursor.fetchone()[0]

            delete_group_query = (f"DELETE g FROM `groups` as g WHERE g.id = '{group_id}'")
            self.cursor.execute(delete_group_query)

            delete_group_teachers_query = (f"DELETE g_t FROM `group_teachers` as g_t WHERE g_t.group_id = '{group_id}'")
            self.cursor.execute(delete_group_teachers_query)

            delete_group_lessons_query = (f"DELETE g_l FROM `group_lessons` as g_l WHERE g_l.group_id = '{group_id}'")
            self.cursor.execute(delete_group_lessons_query)

            delete_group_from_schedule_query = (f"DELETE sch FROM `schedule` as sch WHERE sch.group_id = '{group_id}'")
            self.cursor.execute(delete_group_from_schedule_query)

            update_students_group = (f"UPDATE `students` as s SET s.group_id = '{0}' WHERE s.group_id = '{group_id}'")
            self.cursor.execute(update_students_group)

            self.connection.commit()


        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.delete_group(group)

    def get_group(self, id):
        try:
            query = ("SELECT g.group "
                     "FROM `groups` as g "
                     f"WHERE g.id= '{id}'")
            self.cursor.execute(query)
            row = self.cursor.fetchone()
            if row:
                row = row[0]
            return row
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_group(id)

    def update_group(self, group, lessons, prevGroup):
        try:
            query = (f"SELECT g.id FROM `groups` as g WHERE g.group = '{prevGroup}'")
            self.cursor.execute(query)
            group_id = self.cursor.fetchone()[0]

            update_group_query = (f"UPDATE `groups` as g SET g.group = '{group}' WHERE g.id = '{group_id}'")
            self.cursor.execute(update_group_query)

            delete_group_lessons_query = (f"DELETE g_l FROM `group_lessons` as g_l WHERE g_l.group_id = '{group_id}'")
            self.cursor.execute(delete_group_lessons_query)
            self.connection.commit()
            for lesson in lessons:
                lesson_ = ' '.join(lesson.split()[:-1])

                insert_group_lessons_query = (
                    f"INSERT INTO `group_lessons` (`group_id`, `lesson_id`) VALUES('{group_id}', "
                    f"(SELECT l.id FROM `lessons` as l WHERE l.lesson = '{lesson_}'))")
                self.cursor.execute(insert_group_lessons_query)

            self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.update_group(group, lessons, prevGroup)

    def get_lesson_id(self, lesson):
        try:
            query = (f"SELECT l.id FROM `lessons` as l WHERE l.lesson = '{lesson}'")
            self.cursor.execute(query)
            row = self.cursor.fetchone()
            return row
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_lesson_id(lesson)

    def insert_lesson(self, lesson, index):
        try:
            insert_lesson_query = (f"INSERT INTO `lessons` (`lesson`, `index`) VALUES('{lesson}', '{index}')")
            self.cursor.execute(insert_lesson_query)
            self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.insert_lesson(lesson, index)

    def update_lesson(self, lesson, index, prevLesson, prevIndex):
        try:
            query = (f"SELECT l.id FROM `lessons` as l WHERE l.lesson = '{prevLesson}' AND l.index = '{prevIndex}'")
            self.cursor.execute(query)
            lesson_id = self.cursor.fetchone()[0]

            insert_lesson_query = (
                f"UPDATE `lessons` as l SET l.lesson = '{lesson}', l.index = '{index}' WHERE l.id = '{lesson_id}'")
            self.cursor.execute(insert_lesson_query)
            self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.update_lesson(lesson, index, prevLesson, prevIndex)

    def delete_lesson(self, lesson, index):
        try:
            query = (f"SELECT l.id FROM `lessons` as l WHERE l.lesson = '{lesson}' AND l.index = '{index}'")
            self.cursor.execute(query)
            lesson_id = self.cursor.fetchone()[0]

            delete_lesson_query = (f"DELETE l FROM `lessons` as l WHERE l.id = '{lesson_id}'")
            self.cursor.execute(delete_lesson_query)

            delete_group_lessons_query = (f"DELETE g_l FROM `group_lessons` as g_l WHERE g_l.lesson_id = '{lesson_id}'")
            self.cursor.execute(delete_group_lessons_query)

            delete_teacher_lessons_query = (
                f"DELETE t_l FROM `teacher_lessons` as t_l WHERE t_l.lesson_id = '{lesson_id}'")
            self.cursor.execute(delete_teacher_lessons_query)

            delete_lesson_from_rating_query = (f"DELETE r FROM `rating` as r WHERE r.lesson_id = '{lesson_id}'")
            self.cursor.execute(delete_lesson_from_rating_query)

            delete_lesson_from_schedule_query = (
                f"DELETE sch FROM `schedule` as sch WHERE sch.lesson_id = '{lesson_id}'")
            self.cursor.execute(delete_lesson_from_schedule_query)

            self.connection.commit()

        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.update_lesson(lesson, index)
