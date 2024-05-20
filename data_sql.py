import builtins
from datetime import datetime
from time import sleep

import pymysql
import config
from random import randint
import pandas as pd
import re

names = []


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
            # for row in rows:
            #   print(row)
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

    def update_users(self):
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
            print('Update users complete')
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_users

    def get_students_all(self):
        try:
            query = "SELECT * FROM `students`"
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
                     f"WHERE s.group = '{group}'")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #     print(row)
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_students_group(group)

    def get_student(self, email):
        try:
            query = ("SELECT * FROM `students`"
                     f"WHERE `email`='{email}'")
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
                     "JOIN `students` as s ON s.group = g_l.group "
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

    def get_date_rating_student(self, email):
        try:
            query = ("SELECT DISTINCT r.date "
                     "FROM `rating` as r "
                     f"JOIN `students` as s ON s.id = r.student_id and s.email = '{email}' "
                     "JOIN `lessons` as l On l.id = r.lesson_id "
                     "ORDER BY r.date")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #     print(row[0])
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_date_rating_student(email)

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
            query = ("SELECT DISTINCT g_l.group FROM `group_lessons` as g_l "
                     "JOIN `lessons` as l ON l.id = g_l.lesson_id "
                     f"WHERE l.lesson = '{lesson}'")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #     print(row)
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_groups_lesson(lesson)

    def get_groups_date_lesson(self, group, lesson):
        try:
            query = ("SELECT DISTINCT sch.date "
                     "FROM `schedule` as sch "
                     "JOIN `lessons` as l ON l.id = sch.lesson_id "
                     f"WHERE sch.group = '{group}' "
                     f"AND l.lesson = '{lesson}' "
                     f"ORDER BY sch.date")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #     print(row)
            return rows
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
                     f"WHERE s.group = '{group}' AND l.lesson = '{lesson}' "
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
                     f"WHERE s.group = '{group}' "
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
                query = ("INSERT INTO `rating` (`student_id`, `lesson_id`, `assessment`, `count_id`, `date`) "
                         f"SELECT s.id, l.id, {assessments[i]}, {i},'{date_}' "
                         "FROM `group_lessons` as g_l "
                         "JOIN `students` as s ON s.group = g_l.group "
                         "JOIN `lessons` as l ON l.id = g_l.lesson_id "
                         f"WHERE s.group = '{group}' "
                         f"AND l.lesson = '{lesson}' "
                         f"AND s.name = '{sName}' "
                         f"AND s.first_name = '{sFirstName}' "
                         f"AND s.second_name = '{sSecondName}'")
                self.cursor.execute(query)
                self.connection.commit()

        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.update_rating_group(assessments, date, name, group, lesson)

    def get_schedule_admin(self, date):
        try:
            query = ("SELECT l.lesson, l.index, sc.group, sc.id_count, sc.date "
                     "FROM `schedule` as sc "
                     "JOIN `lessons` as l ON l.id = sc.lesson_id "
                     f"WHERE sc.date = '{date}'"
                     "ORDER BY sc.group, sc.id_count")
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            # for row in rows:
            #     print(row)
            return rows
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.get_schedule_admin(date)

    def get_groups(self):
        try:
            query = ("SELECT DISTINCT `group` "
                     "FROM `students` "
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
            return self.get_groups()

    def get_lessons_group(self, group):
        try:
            query = ("SELECT DISTINCT l.lesson, l.index, t.name, t.first_name, t.second_name, g_l.group "
                     "FROM `lessons` as l "
                     "JOIN `group_lessons` as g_l ON g_l.lesson_id = l.id "
                     "JOIN `teacher_lessons` as t_l ON t_l.lesson_id = l.id "
                     "JOIN `teachers` as t ON t.id = t_l.teacher_id "
                     f"WHERE g_l.group = '{group}'")
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
            query = ("SELECT l.lesson, sch.group, sch.id_count, sch.date "
                     "FROM `schedule` as sch "
                     "JOIN `lessons` as l ON sch.lesson_id = l.id "
                     f"WHERE `date` = '{date}' "
                     f"AND `group` = '{group}' "
                     f"AND `id_count` = '{id_count}'")
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
            query = ("INSERT INTO `schedule` (`lesson_id`, `group`, `id_count`, `date`) "
                     f"SELECT l.id, '{group}', {id_count}, '{date}' "
                     f"FROM lessons as l WHERE l.lesson = '{lesson}'")
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
                     f"WHERE sch.group = '{group}' "
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
            query = ("DELETE FROM `schedule` "
                     f"WHERE `group` = '{group}' "
                     f"AND `id_count` = '{id_count}' "
                     f"AND `date` = '{date}'")
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}, Time: {datetime.now()}')
            self.connect()
            return self.delete_schedule(date, group, id_count)
