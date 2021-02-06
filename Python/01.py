import time
print("       {[(>------------NuyoaH------------<)]}")
A = input("请输入你的姓名:")
print("尊敬的"+ A + "您好！")
print("您接下来准备:")
print("A.登录 B.注册 ")
B = input("<\>")
if B == "A":
    C = input("用户名:")
    if C == "NuyoaH":
        print("欢迎回来，主人！")
        print("接下来您准备:")
        print("A.获取密码 B.入侵服务器 C.渗漏")
        D = input("<\>")
        if D == "A":
            input("请输入目标帐号:")
            print("正在破译...")
            time.sleep(5)
            print("破译完成")
            print("Password:**********")
        else:
            if D == "B":
                input("请输入目标IP:")
                print("正在入侵...")
                time.sleep(5)
                print("入侵完成")
            else:
                input("请输入渗漏目标端口:")
                print("正在渗漏...")
                time.sleep(5)
                print("渗漏成功")
    else:
        input("密码:")
        print("登录成功！")
        print("接下来您准备:")
        print("A.获取密码 B.入侵服务器 C.渗漏")
        D = input("<\>")
        if D == "A":
            input("请输入目标帐号:")
            print("正在破译...")
            time.sleep(5)
            print("破译完成")
            print("Password:**********")
        else:
            if D == "B":
                input("请输入目标IP:")
                print("正在入侵...")
                time.sleep(5)
                print("入侵完成")
            else:
                input("请输入渗漏目标端口:")
                print("正在渗漏...")
                time.sleep(5)
                print("渗漏成功")
else:
    input("您的邮箱:")
    input("您的用户名:")
    input("您的密码:")
    print("接下来您准备:")
    print("A.获取密码 B.入侵服务器 C.渗漏")
    D = input("<\>")
    if D == "A":
        input("请输入目标帐号:")
        print("正在破译...")
        time.sleep(5)
        print("破译完成")
        print("Password:**********")
    else:
        if D == "B":
            input("请输入目标IP:")
            print("正在入侵...")
            time.sleep(5)
            print("入侵完成")
        else:
            input("请输入渗漏目标端口:")
            print("正在渗漏...")
            time.sleep(5)
            print("渗漏成功")
            
        