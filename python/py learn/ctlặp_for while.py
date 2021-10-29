#cấu trúc for: for i in range():
# i là biến lặp, hàm range là 1 tham số
#range có 3 tham số (x,y,z): là thứ tự lần lượt (start,stop,step)
#cấu trúc while: while + câu điều kiện:

#vừa gà vừa chó, bó lại cho tròn, 36 con, 100 chân chẵn. giải bài toán
for ga in range(1,36):
    cho=36-ga
    if 2*ga+4*cho==100:
        print("số gà:", ga, "số chó:", cho)
#hoặc cho ra nhiều đáp án với 2 trường hợp for
for ga in range(1, 36):
    for cho in range(1, 36):
        if ga * 2 + cho * 4 == 100:
            print("ga  la ", ga, "cho la ", cho)
            #hoặc print("ga  la ", ga, "cho la ", cho, end =" ")
            # thì end=" " là xuất kết quả không xuống hàng

#nhập tuổi cha và con (hiện tuổi cha lớn hơn 2 lần tuổi con và tuổi cha hơn tuổi
# con ít nhất là 25). tính bao nhiêu năm nữa tuổi cha gấp đôi tuổi con.
tcha=int(input('nhập tuổi cha:'))
tcon=int(input('nhập tuổi con:'))
năm=0
if tcha>2*tcon and tcha-tcon>=25:
    while tcha!=2*tcon:         #dấu ! là khác
        tcha=tcha+1
        tcon=tcon+1
        năm=năm+1
    print("số năm để tuổi cha gấp đôi tuổi con:",năm)
else:
    print("nhập lại số tuổi, tuổi cha phải hơn con ít nhất 25 tuổi:")
