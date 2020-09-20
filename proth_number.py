def proth_number(N = int(input("What is you N number? ")), K = int(input("What is your K number? "))):
    if K % 2 == 1:
        N = K * 2 ** N + 1 #Proth's Theorem
        print("The prime number is", N)
    else: 
        print("K is not an odd number")

proth_number()
