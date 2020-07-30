table={"월요일":"청국장","화요일":"비빔밥",
      "수요일":"된장찌개","목요일":"칼국수",
      "금요일":"냉면","토요일":"소불고기","일요일":"오삼불고기"}
day=0
while(1):
    day=input("요일을 입력하세요(끝내려면  '종료'입력): ")
    if(day=="종료"):
        break
    elif(day in table):
        print("%s: %s"%(day,table[day]))
    else:
        print("잘못 입력하셨습니다.")
