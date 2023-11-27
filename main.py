from function import Database

def main():
    bio_db=Database()

    while True:
        try:    
            user_input = input("\n 1: 테이블 생성 \n 2: 테이블 삭제 \n 3: 데이터 삽입 \n 4: 조인 \n 5: 쿼리 \n ('q' 는 quit) : ")

            # 'q'를 입력하면 프로그램 종료
            if user_input.lower() == 'q':
                print("\n Exiting the program.")          
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
                table_to_drop = input("\n Which one drop your_table?: ")
                bio_db.drop_table(table_to_drop)
                
            elif user_input == 3:
                bio_db.insert_data()

            elif user_input == 4:
                joiny=input("\n Select 1~3 Join : ")
                join=int(join)
                if join == 1:
                    bio_db.join1()
                elif join == 2:
                    bio_db.join2()
                elif join == 3:
                    bio_db.join3()
                else:
                    print("\n Invalid input. Please enter a number between 1 and 3.")

            elif user_input == 5:
                query=input("\n Select 1~8 Query : ")
                query=int(query)
                if query == 1:
                    bio_db.query1()
                elif query == 2:
                    bio_db.join2()
                elif query == 3:
                    bio_db.join3()
                else:
                    print("\n Invalid input. Please enter a number between 1 and 3.")

            else:
                print("\n Invalid input. Please enter a number between 1 and 5.")

        except ValueError:
            print("\n Invalid input. Please enter a valid number.")
       
if __name__=="__main__":
    main()