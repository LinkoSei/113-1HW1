while True:
    n = int(input("請輸入一個正整數 (1 <= N <= 100000): "))
    if 1 <= n <= 100000:
        print(int(str(n)[::-1]))
        break #Break作用 => 如果輸入正確則會執行，執行後跳出循環
    else:
        print("輸入的數字超出範圍，請重新輸入！")