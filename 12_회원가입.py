def checkIDPW(IP):
    for n in IP:
        if n.isalpha():
            break
        elif IP[-1] == n:
            print("알파벳이 없습니다. 추가해주세요.")
    for n in IP:
        if n.isdigit():
            return True
        elif IP[-1] == n:
            print("숫자가 없습니다. 추가해주세요.")
    

def countID(ID):
    if not(8<= len(ID) <= 20):
        print(ID,"은(는)",len(ID),"자로 자수를 초과(미달)했습니다. 확인해주세요.")
    else:
        return True

def countPW(PW):
    if len(PW) < 12:
        print(PW,"은(는)",len(PW),"자로 자수를 미달했습니다. 확인해주세요.")
    else:
        return True
    


d = {"이름":"","생년월일":[0000,00,00],"아이디":"","비밀번호":""}

#이름, 생년월일
print("[회원가입 절차]")
name = input("성함을 입력해주세요: ")
print("생년월일을 입력해 주세요")
year = int(input("년도: "))
month = int(input("월: "))
day = int(input("일: "))

#딕셔너리 수정
d["이름"] = name
d["생년월일"][0] = year
d["생년월일"][1] = month
d["생년월일"][2] = day

#아이디, 비번
ID = input("""사용하실 아이디를 입력해주세요.
(단, 8~20사이. 최소 영문(또는 한글)+숫자 조합): """)
checkID = checkIDPW(ID)
lenID = countID(ID)
while not(checkID and lenID):
    ID = input("""다시 입력해주세요.
(단, 8~20사이. 최소 영문(또는 한글)+숫자 조합): """)
    checkID = checkIDPW(ID)
    lenID = countID(ID)

PW = input("""사용하실 비밀번호를 입력해주세요.
(단, 12자 이상. 최소 영문(또는 한글)+숫자 조합): """)
checkPW = checkIDPW(PW)
lenPW = countID(PW)
while not(checkPW and lenPW):
    PW = input("""다시 입력해주세요.
(단, 12자 이상. 최소 영문(또는 한글)+숫자 조합): """)
    checkPW = checkIDPW(PW)
    lenPW = countID(PW)

#딕셔너리 수정
d["아이디"] = ID
d["비밀번호"] = PW

print(d)
