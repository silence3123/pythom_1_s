d = {}
thing = input("물건의 이름을 입력해주세요: ")
while thing != '': #빈문자열이면 멈춤
    price = int(input("가격을 입력해주세요: "))
    num = int(input("현재 재고를 입력해주세요: "))
    d[thing] = [price, num, 0,num,0]
    thing = input("물건의 이름을 입력해주세요: ")

print("현재 물량은 다음과 같습니다. (참고: 가격, 기존재고, 주문건수, 남은재고, 매출액 순서)")
for n in d:
    print(n,d[n])

orderThing = input("무엇을 주문하시겠습니까?: ")
while orderThing != '': #빈문자열이면 멈춤
    orderNum = int(input("몇 건 주문하시겠습니까?: "))
    num = d[orderThing][3] #재고
    if orderNum <= num:
        price = d[orderThing][0] #물건 가격
        pay = orderNum * (price + price*1/10) #매출액
        remainNum = num - orderNum
        d[orderThing] = [price, num, orderNum, remainNum, pay]
    else:
        print("재고가 부족합니다. 확인해주세요.")
    orderThing = input("무엇을 주문하시겠습니까?: ")

print("최종 물량은 다음과 같습니다. (참고: 가격, 기존재고, 주문건수, 남은재고, 매출액 순서)")
for n in d:
    print(n,d[n])
