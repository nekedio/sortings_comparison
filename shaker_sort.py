def show_sorting(ar):
    print(ar)
    len_ar = len(ar)
    i = 0
    marker = 0 
    while i < len_ar - 1:
        #print(i)
        if ar[i] > ar[i + 1]:
            (ar[i], ar[i + 1]) = (ar[i + 1], ar[i])
            marker = 1
        i+=1
    if marker == 0:
        return ar

    while i > 0:
        #print(i)
        if ar[i] < ar[i - 1]:
            (ar[i], ar[i - 1]) = (ar[i - 1], ar[i])
            marker = 1
        i-=1
    if marker == 0:
        return ar

    if marker == 1:
        return show_sorting(ar)
