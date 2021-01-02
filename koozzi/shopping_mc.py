import pymysql
from random import randint


def dbconnect():
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        db = 'ShoppingMall',
        charset = 'utf8'
    )

    return conn


class User:
    def __init__(self):
        self.conn = dbconnect()
    
    def select_by_id(self, user_id):
        cur = self.conn.cursor()
        sql = "select * from usertbl where user_id = %s"
        cur.execute(sql, (user_id))
        return cur.fetchall()
        
    def register_new_user(self, user_id, user_name):
        cur = self.conn.cursor()
        sql = "insert usertbl value(%s, %s, NOW(), 0)"
        cur.execute(sql, (user_id, user_name))
        self.conn.commit()

    def register_admin_user(self, user_id, user_name):
        cur = self.conn.cursor()
        sql = "insert usertbl value(%s, %s, NOW(), 1)"
        cur.execute(sql, (user_id, user_name))
        self.conn.commit()


class Item:
    def __init__(self):
        self.conn = dbconnect()

    def select_all(self):
        cur = self.conn.cursor()
        sql = "select * from item"
        cur.execute(sql)
        return cur.fetchall()

    def register_item(self, item_name, item_price, item_stock):
        cur = self.conn.cursor()
        item_id = randint(10000, 99999)

        while True:
            item_id = randint(10000, 99999)
            sql = "select * from item where item_id = '{0}'".format(item_id)
            cur.execute(sql)
            if not cur.fetchall():
                break
        
        sql = "insert item value({0}, '{1}', {2}, {3})".format(item_id, item_name, item_price, item_stock)
        cur.execute(sql)
        self.conn.commit()


class Order:
    def __init__(self):
        self.conn = dbconnect()
    
    def make_order(self, total_price, user_id):
        cur = self.conn.cursor()
        random_id = randint(10000, 99999)
        sql = "insert Ordertbl value({0}, '{1}', {2}, NOW())".format(random_id, user_id, total_price)
        # random_id가 이미 사용중인지 Check 는 귀찮다 ^^ 
        cur.execute(sql)
        self.conn.commit()    
        return random_id 

    def select_by_user(self, user_id):
        cur = self.conn.cursor()
        sql = "select * from Ordertbl order by order_date desc"
        cur.execute(sql)
        return cur.fetchall()


class OrderList:
    def __init__(self):
        self.conn = dbconnect()
    
    # 회원 전체 결제 내역
    def make_order(self, order_id, basket, user_id):
        cur = self.conn.cursor()

        # dictionary로 중복된 item_id 값들을 처리
        # dictionary_example = {
        #     ...
        #     item_id: [item이름, item갯수],
        #     ...
        # }
        basket_dic = {}
        for item in basket:
            if item[0] in basket_dic:
                basket_dic[item[0]][1] += 1
            else:
                basket_dic[item[0]] = [item[1], 1]

        # dictionary안에서 for문을 돌려서 값들을 각각 DB에 저장한다.
        for key, val in basket_dic.items():
            order_id = order_id  
            user_id = user_id
            item_id = key
            item_name = val[0]
            order_list_num = val[1]
            
            sql = "insert Order_list value({0},'{1}',{2},'{3}',{4})".format(order_id, user_id, item_id, item_name, order_list_num)
            cur.execute(sql)
            self.conn.commit()

    # 회원의 세부 결제 내역
    def select_by_order(self, order_id):
        cur = self.conn.cursor()
        sql = "select * from Order_list where order_id = {0}".format(order_id)
        cur.execute(sql)
        return cur.fetchall()