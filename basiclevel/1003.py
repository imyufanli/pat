"""
Author: Yufan Li (yufan.l@hotmail.com)
PAT (Basic Level) Practice
1003 我要通过！
score: 15 out of 20
"""


def check_con1(w):
    if "P" in w and \
            "A" in w and \
            "T" in w:
        # print(w, "pass con 1")
        return True
    else:
        # print(w, "didn't pass con 1")
        return False


def check_con2(w):
    if w.find("PAT") == 0:
        # print(w, "pass con 2 node 1")
        return True
    elif w.find("PAT") > 0:
        for i in w[:w.find("PAT")]:
            if i == "A":
                continue
            else:
                # print(w, "didn't pass con 2 node 2")
                return False
        if w.rfind("PAT") == len(w)-3:
            # print(w, "pass con 2 node 3")
            return True
        elif w.rfind("PAT") < len(w)-3:
            for j in w[w.rfind("PAT")+3:]:
                if j == "A":
                    continue
                else:
                    # print(w, "didn't pass con 2 node 4")
                    return False
            # print(w, "pass con 2 node 5")
            return True
        else:
            # print(w, "didn't pass con 2 node 6")
            return False
    else:
        # print(w, "didn't pass con 2 node 7")
        return False


def check_con3(w):
    if w.find("AT"):
        w = w[:w.find("AT")-1] + w[w.find("AT"):]
        a = w[:w.find("P")]
        if a == "":
            return check_con2(w)
        elif a:
            w = w[:w.rfind(a)]
            # print("Enter con 2")
            # print(w)
            return check_con2(w)
        else:
            # print(w, "didn't pass con 3 node 1")
            return False
    else:
        # print(w, "didn't pass con 3 node 2")
        return False


def main_check():
    count = int(input())
    for i in range(count):
        w = input()
        # print(w, "enter con 1")
        if check_con1(w):
            # print(w, "enter con 2")
            if check_con2(w):
                # print(w, "pass main check node 1")
                print("YES")
            else:
                # print(w, "enter con 3")
                if check_con3(w):
                    # print(w, "pass main check node 2")
                    print("YES")
                else:
                    # print(w, "didn't pass main check node 3")
                    print("NO")
        else:
            # print(w, "didn't pass main check node 4")
            print("NO")


main_check()
"""for i in ["AAPATAA", "AAPAATAAAA"]:
    check_con2(i)
for i in ["AAPAATAAAA", "AAPAAATAAAA", "AAPAAAATAAAA"]:
    check_con3(i)"""
