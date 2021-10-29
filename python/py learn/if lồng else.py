#giải và biện luận phương trình bậc I: ax+b=0
a=float(input("a="))
b=float(input("b="))
if a==0:
    if b==0:
        print("phương trình vô số nghiệm")
    else:
        print("phương trình vô nghiệm")
else:
    x= -b/a
    print("nghiệm x= %.2f" %x)
    # %f là số thực (float), .2 là lấy đuôi 2 số
    # %x là gán cho %F