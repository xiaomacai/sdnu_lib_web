# coding: utf-8
import sqlite3
import os
basedir = os.path.abspath(os.path.dirname(__name__))


class Select(object):
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(basedir, 'occupy_desk.sqlite'))
        self.cur = self.conn.cursor()

    @property
    def select_start_time(self):
        sql = '''select real_start_time from occupy order by real_start_time desc;'''
        res = self.cur.execute(sql).fetchall()

        res_dict = {}
        if res:
            for item in res:
                if res_dict.has_key(item[0]):
                    res_dict[item[0]] += 1
                else:
                    res_dict[item[0]] = 1
            return sorted(res_dict.iteritems(), key=lambda asd:asd[0])

    @property
    def select_end_time(self):
        sql = '''select real_end_time from occupy order by real_end_time desc;'''
        res = self.cur.execute(sql).fetchall()

        res_dict = {}
        if res:
            for item in res:
                if res_dict.has_key(item[0]):
                    res_dict[item[0]] += 1
                else:
                    res_dict[item[0]] = 1
            return sorted(res_dict.iteritems(), key=lambda asd:asd[0])


    @property
    def select_sum_times(self):
        sql = '''select count(*) as num from occupy GROUP BY student_id;'''
        res = self.cur.execute(sql).fetchall()

        res_dict = {}
        if res:
            for item in res:
                if res_dict.has_key(item[0]):
                    res_dict[item[0]] += 1
                else:
                    res_dict[item[0]] = 1
            return res_dict

    @property
    def select_time_minus(self):
        sql = '''select julianday(time(real_end_time))*1440 - julianday(time(real_start_time))*1440 as cha from occupy;'''
        res = self.cur.execute(sql).fetchall()

        res_dict = {}
        if res:
            for item in res:
                tmp = int(round(item[0], 0))
                if res_dict.has_key(tmp):
                    res_dict[tmp] += 1
                else:
                    res_dict[tmp] = 1
            return res_dict

    



if __name__ == '__main__':

    # print Select().select_start_time
    # print Select().select_end_time
    print Select().select_sum_times
