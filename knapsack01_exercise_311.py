def knapsack01(M,N,K,E):
    #Results array initialization
    k = [[0 for x in range(N + 1)] for x in range(M + 1)]
    
    # Build array in bottom-up approach
    print("\nKnapsack 0/1 array")
    for i in range(M + 1):
        for w in range(N + 1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif K[i-1] <= w:
                k[i][w] = max(E[i-1]+ k[i-1][w-K[i-1]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]
        
        #print Knapsack 0/1 array
        print(k[i][:])
       
    
    #Find selected-rejected offers and maximum profit 
    i = M
    j = N
    
    #Save selected-rejected buyers to lists
    #And total number of diamonds sold
    take_list = []
    no_take_list = []
    total_diamonds_sold = 0

    while(i>0 and j>=0):
        if k[i][j] == k[i-1][j]:
            no_take_list.append(i)
            i = i-1
        else:
            j = j-K[i-1]
            take_list.append(i)
            total_diamonds_sold += K[i - 1]
            i = i-1
    
    #Sort lists
    take_list = sorted(take_list)
    no_take_list = sorted(no_take_list)
    
    print("\nAccepted offers from buyers: ",",".join(str(item) for item in take_list))
    print("Not accepted offers from buyers: ",",".join(str(item) for item in no_take_list))
    print("Total diamonds sold:", total_diamonds_sold,"of",N)
    print("Max profit earned:", k[M][N], "Euros")
    


if __name__ == '__main__':
    M = int(input("Number of buyers: "))

    N = int(input("Number of diamonds for sale: "))

    #Initialize arrays for buyer offers to size of M
    #Diamonds that every buyer asks
    K = M*[0]

    #Amount of money that buyer gives
    E = M*[0]

    #Read offer per buyer
    for i in range(M):
        
        print("\nK = No. of diamonds, E = amount of Euros")
        offer = input(f"Offer from buyer {i+1} in form (K,E) --> ")
        
        #Convert offer to tuple (K,E) and then to integer
        K[i], E[i] = offer.strip('()').split(',')
        K[i] = int(K[i])
        E[i] = int(E[i])

    #Call the function knapsack01 with M,N,K,E as parameters
    knapsack01(M,N,K,E)

