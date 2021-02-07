def my_sort(l):
    for j in range(1,len(l)):
        key = j
        i = j-1
        print("this is j:", l[key], "this is i:", l[i])
        while(i>=0 and key >=0 and l[key]<l[i]):

            #swap
            temp = l[key]
            l[key] = l[i]
            l[i] = temp
            i-=1
            key = i+1

    return l




