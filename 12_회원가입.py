def checkID(ID):
    if not(8<= len(ID) <= 20):
        print(ID,"은(는)",len(ID),"자로 자수를 초과(미달)했습니다. 확인해주세요.")
    for n in ID:
        if n.isalpha():
            break
        elif ID[-1] == n:
            print("아이디 내에 알파벳이 없습니다.")
    for n in ID:
        if n.isdigit():
            break
        elif ID[-1] == n:
            print("아이디 내에 숫자가 없습니다.")

d = {"이름":"","생년월일":[0000,00,00],"아이디":"","비밀번호":""}

print("[회원가입 절차]")
name = input("성함을 입력해주세요: ")
print("생년월일을 입력해 주세요")
year = int(input("년도: "))
month = int(input("월: "))
day = int(input("일: "))

d["이름"] = name
d["생년월일"][0] = year
d["생년월일"][1] = month
d["생년월일"][2] = day

ID = input("""사용하실 아이디를 입력해주세요.
(단, 8~20사이. 최소 영문(또는 한글)+숫자 조합): """)
checkID(ID)
#print(d)
