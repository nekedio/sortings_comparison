def show_sorting(ar):
    print(ar)
    len_ar = len(ar)
    marker = 0

    i = 0
    while i < len_ar - 1:
        if ar[i] > ar[i + 1]:
            (ar[i], ar[i + 1]) = (ar[i + 1], ar[i])
            marker = 1
        i+=2

    i = 1
    while i < len_ar - 1:
        if ar[i] > ar[i + 1]:
            (ar[i], ar[i + 1]) = (ar[i + 1], ar[i])
            marker = 1
        i+=2
    
    if marker == 1:
        return show_sorting(ar)

    if marker == 0:
        return ar
