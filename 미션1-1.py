def inp(): #간단한 수정 #나도
    stuff=(input("물품 이름 : "))
    stuff_list[0]=float(input("기존 %s의 재고량 (단위 : 개): "%(stuff)))
    stuff_list[2]=float(input("물품의 가격 (단위 : 원) : "))
    stuff_list[3]=stuff_list[2]*1.1

def chg():
     stuff=(input("물품 이름 : "))
     stuff_list[1]=int(input("주문 건수 (단위 : 건) :  "))
     if(stuff_list[1]>stuff_list[0]):
         print("재고가 부족합니다. 다시 입력해주세요.")
         
def prt():
    stuff=(input("물품 이름 : "))
    print("주문건수 : %i 건"%(stuff_list[1]))
    print("기존 재고량 : %i개"%(stuff_list[0]))
    print("남은 재고량 : %i개"%(stuff_list[0]-stuff_list[1]))
    print("매출액(부가세포함) : %.2f원"%(stuff_list[3]*stuff_list[1]))


stuff=0
stuff_list=[0,0,0,0]
dic={stuff:stuff_list}

while(1):

    print("1. 재고 정리 2. 재고량 변경 3. 재고 확인 4. 종료" )
    num=int(input("원하시는 서비스의 번호를 입력하시오 : "))

    if(num==1):
        inp()
    elif(num==2):
        chg()
    elif(num==3):
        prt()
    elif(num==4):
        print("종료")
        break
    else:
        print("잘못 입력하셨습니다 .1~3의 정수를 입력하세요")
        


