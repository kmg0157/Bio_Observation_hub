from connection import Database
from query import Query

def main():
    bio_db=Database()

    while True:
        try:    
            user_input = input("1: 테이블 생성, 2: 테이블 삭제, 3: 데이터 삽입 , 4: 조인 1, 5: 조인 2, 'q' 는 quit: ")

            # 'q'를 입력하면 프로그램 종료
            if user_input.lower() == 'q':
                print("Exiting the program.")          
                #DB 종료
                bio_db.close_db()
                break

            user_input = int(user_input)

            # 선택된 숫자에 따라 다른 함수 실행
            if user_input == 1:
                #테이블 생성
                bio_db.create_table()   #생성되는 테이블은 table.py 참조 및 변경 가능
            
            elif user_input == 2:            
                #테이블 삭제
                table_to_drop = input("Which one drop your_table?: ")
                bio_db.drop_table(table_to_drop)
                
            elif user_input == 3:
                bio_db.insert_data()

            elif user_input == 4:
                Query.join_1()
            
            elif user_input == 5:
                Query.join_2()
            
            else:
                print("Invalid input. Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
       
if __name__=="__main__":
    main()