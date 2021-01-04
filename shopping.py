#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Controller
import pymysql


def dbconnect():  # 패스워드는 꼭 자기 DB 패스워드로! db 이름도 잘 확인할 것!
    conn = pymysql.connect(host='127.0.0.1', user='root',
                           password='12341234', db='shopping', charset='utf8')
    return conn


class UserController:
    def __init__(self):
        self.conn = dbconnect()
        self.userDAO = UserDAO(self.conn)

#  Users by user_id
    def InsertUser(self, user_id, user_name, sign_up_date):
        row = self.userDAO.InsertUser(
            user_id, user_name, sign_up_date, user_check)
        self.conn.commit()
        return row;

    def SelectUser(self, user_id):
            row = self.userDAO.SelectUser(user_id)
            return row;

#  Items by item_id
    def InsertItem(self, item_id, item_price, item_name):
        row = self.userDAO.InsertItem(item_id, item_pric, item_name)
        self.conn.commit()}
        return row;

    def SelectItemAll(self):
        row = self.userDAO.SelectItemAll()
        return row;

#  order by order_id
    def InsertOrder(self, order_id):
        row = self.userDAO.InsertItem(
            item_id, item_pric, item_stock, item_name)
        self.conn.commit()
        return row;

    def SelectItemAll(self, item_id):
        row=self.userDAO.SelectItemAll()
        return row;

#  order_list

    def SelectOrderList(self, item_id, order_id):
        row=self.userDAO.SelectOrderList()
        return row;



# In[2]:


# model
# todo  

'''
join 

SELECT ut.user_id, ot.order_id, item_name, order_list_num
FROM user_tabl ut
JOIN Order_tbl ot ON ut.user_id = ot.user_id
JOIN Order_list_tbl olt ON ot.order_id = olt.order_id
JOIN item_tbl it ON olt.item_id = it.item_id;
'''

# User  테이블의 데이터를 조회, 갱신, 저장, 삭제 등의 메소드를 포함. (User Data Access Object)
class UserDAO:
    def __init__(self, conn):
        self.conn=conn

# write & read & delete users
    def InsertUser(self, user_id, user_name):
        cur=self.conn.cursor()
        cur.execute("INSERT INTO user_tbl VALUES ('{}','{}',NOW())".format(
            user_id, user_name, sign_up_date))
        row=cur.fetchone()
        return row
    def SelectUser(self, user_id):
        cur=self.conn.cursor()
        cur.execute(
            "SELECT * FROM user_tbl WHERE user_id = '{}'".format(user_id))
        row=cur.fetchall()
        return row
    def DeleteUser(conn):
        userId=input("put the user ID to delete")
        cur=conn.cursor()
        cur.execute("DELETE * FROM user_tbl WHERE user_id = '" + userId + "'")

# write & read & delete items
    def InsertItem(self, item_id, item_name, item_price):
        cur=self.conn.cursor()
        cur.execute("INSERT INTO item_tbl VALUES ('{}','{}','{}')".format(
            item_id, item_name, item_price))
        row=cur.fetchone()
        return row
    def SelectItem(self, item_id, item_name, item_price):
        cur=self.conn.cursor()
        cur.execute(
            "SELECT * FROM item_tbl WHERE item_id = '{}'".format(item_id))
        row=cur.fetchone()
        return row
    def DeleteItem(conn):
        itemId=input("put the item ID to delete")
        cur=conn.cursor()
        cur.execute("DELETE * FROM item_tbl WHERE item_id = '" + item_id+"'")

# write & delete order_list
        orderId=input("put the order ID to delete")
        cur=conn.cursor()
        cur.execute("SELECT * FROM Order_tbl WHERE order_id = '" + order_id+"'")

# write & read & delete order_list
    def SelectOrderList(self, item_id, item_name, item_price):
        cur=self.conn.cursor()
        cur.execute(
            "SELECT * FROM item_tbl WHERE item_id = '{}'".format(item_id))
        row=cur.fetchone()
        return row



# In[3]:


# View
# to-do


def signUp(uc):
    print("Sign up page")
    user_id=input("Your ID: ")
    if uc.SelectUser(user_id) is no user_id:
        print("This User ID is already taken")
        return

    user_name=input("Your name: ")
    uc.InsertUser(user_name)
    print("Successfully signed up.")
    row=uc.SelectUser(user_id)
    printUser(row)

def main():
    uc=UserController()

    while True:
        print("""<Welcome to Encore Shopping mall.>
               pick an option. """)
        choice=input("""
                          1. Sign Up
                          2. Shopping
                          3. Shopping Cart
                          4. Admin
                          5. Exit
                          >>> Please, provide us with number : """)

        if choice == "1": signUp(uc)
        elif choice == "2": shopping(uc)
        elif choice == "3": orderList(uc)
        elif choice == "4": admin(uc)
        elif choice == "5": break
        else: print("Wrong number Try agian.")
    uc.conn.close()

if __name__ == '__main__': main()


# In[ ]:
