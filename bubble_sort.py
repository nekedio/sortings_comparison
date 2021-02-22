def show_sorting(ar):
    print(ar)
    len_ar = len(ar)
    i = 0
    marker = 0
    while i < len_ar - 1:
        if ar[i] > ar[i + 1]:
            (ar[i], ar[i + 1]) = (ar[i + 1], ar[i])
            marker = 1
        i+=1
    if marker != 0:
        return show_sorting(ar)
    return ar

def sort(ar):
    len_ar = len(ar)
    marker = 1
    while marker == 1:
        #print(ar)
        marker = 0
        i = 0
        while i < len_ar - 1:
            if ar[i] > ar[i + 1]:
                (ar[i], ar[i + 1]) = (ar[i + 1], ar[i])
                marker = 1
            i+=1
    return ar

def sort_r(ar):
    len_ar = len(ar)
    i = 0
    marker = 0
    while i < len_ar - 1:
        if ar[i] > ar[i + 1]:
            (ar[i], ar[i + 1]) = (ar[i + 1], ar[i])
            marker = 1
        i+=1
    if marker != 0:
        return sort_r(ar)
    return ar


