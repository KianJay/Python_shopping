from shopping_mc import *
from datetime import datetime
import pymysql

def register():
    
    while True:
        print("회원가입 페이지입니다.")
        user_name = input("이름을 입력해주세요.")
        user_id = input("아이디를 입력해주세요.")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        user = User()
        exist_user = user.select_by_id(user_id)

        if exist_user:
            print("\n이미 존재하는 아이디입니다. 다시 입력해주세요.\n")
            continue

        # 해당 정보 DB에 저장
        user.register_new_user(user_id, user_name)
        print("\n{0}님! 가입 되었습니다. 로그인(1) 후 이용해 주세요".format(user_id))
        break

    return

def order(user_id):
    print("\n{0}님의 구매내역\n".format(user_id))

    _order = Order()
    _result = _order.select_by_user(user_id)

    while True:
       # 회원의 전체 구매내역 출력
        print("No.\t주문번호\t\t회원아이디\t\t결제금액\t\t결제시간")
        for idx, res in enumerate(_result):
            print("{4}\t{0}\t\t\t{1}\t\t\t{2}\t\t\t{3}".format(res[0], res[1],res[2],res[3], idx+1))

        print("\n세부 구매내역을 조회하시려면 주문번호(5자리)를 입력해 주세요!")
        print("뒤로가기(0)\n")
        order_id = int(input(">>> "))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        # 회원의 세부 구매 내역 출력
        if order_id == 0: break
        else:
            order_list = OrderList()
            result = order_list.select_by_order(order_id)
            for res in result:
                print(res[2], res[3], res[4])
        
def profile(current_user):
    print("\n반갑습니다. {0}님".format(current_user[0][0]))

    print("이름\t\t\t아이디\t\t\t가입날짜\t\t\tSTAFF")
    print("{0}\t\t\t{1}\t\t\t{2}\t\t{3}".format(current_user[0][1], current_user[0][0], current_user[0][2], current_user[0][3]))

    while True:
        print("\n0. 뒤로가기")
        print("1. 구매내역 확인")
        print("번호를 입력해주세요.\n")
        answer = int(input(">>> "))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        if answer == 1: order(current_user[0][0])
        elif answer == 0: return
        else: print("0,1 중 하나만 입력해 주세요~")

def shop(current_user):
    basket = []
    total_price = 0
    while True:
        print("\n돈쓰는 건 항상 즐거워 ^^\n")
        print("0. 뒤로가기")
        print("1. 장바구니") 
        print("2. 결제하기")

        item = Item()
        items = item.select_all()
        print("------------------------------------------------------------------------------------------")
        print("상품 번호\t\t상품 이름\t\t\t가격\t\t\t잔여량")
        for idx, cloth in enumerate(items):
            print(idx+3, end=".\t\t\t")
            print(cloth[1], end="\t\t\t")
            print(cloth[2], end="\t\t\t")
            print('무한^^')
        print("------------------------------------------------------------------------------------------")
    
        print("상품번호(3~) 혹은 (0~2)번호를 입력해주세요.\n")
        category_num = int(input(">>> "))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        if category_num == 0: return
        if category_num == 1:
            print("\n현재 장바구니 목록입니다.")
            for item in basket:
                print(item)
            print("총 가격 : ", total_price)
            continue
        if category_num == 2:
            if not basket:
                print("장바구니가 비어있습니다.")
                print("아이템을 담아주세요.")
                continue
            print("\n결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제\n")

            print("현재 장바구니")
            for item in basket:
                print(item)
            print("총 가격 : ", total_price)
            print("\n결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제결제\n")

            print("결제하시겠습니까? (Y/N) \n")
            
            answer = input(">>> ")
            if answer == 'Y' or answer == 'y':
                order = Order()
                order_list = OrderList()

                order_id = order.make_order(total_price, current_user[0][0])
                order_list.make_order(order_id, basket, current_user[0][0])

                print("결제가 완료되었습니다 !!")
                print("감사합니다.")
                return
            else:
                print("결제가 취소되었습니다.")
                print("장바구니는 그대로 유지됩니다.")
                continue
            
            continue
        print("{0}번 아이템을 장바구니에 넣었습니다.".format(category_num))
        basket.append(items[category_num-3])
        total_price += items[category_num-3][2]

def admin_item():
    print("상품관리 페이지입니다.")

    while True:
        print("0. 뒤로가기")
        print("1. 새로운 상품 등록")
        print("2. 상품 업데이트")
        print("3. 상품 삭제")
        answer = int(input(">>> "))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        if answer == 0: return
        elif answer == 1:
            print("새로운 상품 이름을 입력하세요.")
            item_name = input(">>> ")
            print("상품의 가격을 입력하세요.")
            item_price = input(">>> ")
            print("상품의 개수를 입력하세요.")
            item_stock = int(input(">>> "))

            item = Item()
            item.register_item(item_name, item_price, item_stock)
            print("상품이 등록되었습니다!")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        elif answer == 2:
            pass

        elif answer == 3:
            pass

def admin_user():
    print("회원 관리 페이지입니다.")

    while True:
        print("0. 뒤로가기")
        print("1. 관리자 등록하기")
        print("2. 일반 회원 관리")
        answer = int(input(">>> "))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")    

        if answer == 0: return
        elif answer == 1:
            user = User()
            print("새로운 관리자의 ID를 입력하세요.")
            user_id = input(">>> ")
            print("새로운 관리자의 이름을 입력하세요.")
            user_name = input(">>> ")
            
            user.register_admin_user(user_id, user_name)

        elif answer== 2:
            pass

def admin_main():
    print("관리자 페이지입니다.")
    print("관리자 ID를 입력해주세요!")
    user_id = input(">>> ")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    
    user = User()
    exist_user = user.select_by_id(user_id)

    if not exist_user:
        print("!!!!!해당 아이디에 대한 정보가 없습니다.!!!!!\n")
        return

    if exist_user[0][3] == 0:
        print("해당 아이디는 관리자 전용 ID가 아닙니다.")
        return

    while True:
        print(exist_user[0][0], "님 환영합니다.")
        print("0. 로그아웃")
        print("1. 회원관리")
        print("2. 상품관리")
        answer = int(input(">>> "))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        if answer == 0:
            print("로그아웃합니다.")
            return
        elif answer == 1:
            admin_user()
        elif answer == 2:
            admin_item()

def logged_in(current_user):
    while True:
        print("\n{0}님 환영합니다.\n".format(current_user[0][0]))
        print("1. 회원정보 조회")
        print("2. 쇼핑~")
        print("3. 로그아웃")
        print("4. 쇼핑몰 종료")
        print("번호를 입력해주세요.\n")
        answer = int(input(">>> "))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        if answer == 1: profile(current_user)
        elif answer == 2: shop(current_user)
        elif answer == 3: break
        elif answer == 4:
            print("\n프로그램을 종료합니다.")
            print("바이바이~\n")
            exit()
        else: print("1,2,3,4 중 하나만 입력해 주세요~")

    print("\n로그아웃합니다.")
    return

def log_in():
    print("\n------로그인페이지------")
    print("ID을 입력해주세요!")
    print("우리는 비밀번호 안 받아요 ^^\n") 
    user_id = input(">>> ")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    user = User()
    exist_user = user.select_by_id(user_id)

    if exist_user:
        print("\n로그인되었습니다.")
        logged_in(exist_user)
    else:
        print("!!!!!해당 아이디에 대한 정보가 없습니다.!!!!!\n")
        return 

def main(conn):

    while True:
        print("\n플레이데이터 4조 쇼핑몰\n")
        print("0. 관리자페이지")
        print("1. 로그인")
        print("2. 회원가입")
        print("3. 종료")
        print("번호를 입력해주세요!\n")
        answer = int(input(">>> "))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        if answer == 0: admin_main()
        elif answer == 1: log_in()
        elif answer == 2: register()
        elif answer == 3: break
        else: print("1,2,3 중 하나만 입력해 주세요~")

    print("\n바이바이~\n")

    conn.close()

if __name__ == "__main__":

    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        db = 'ShoppingMall',
        charset = 'utf8'
    )

    main(conn)