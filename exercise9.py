def tsum (num : list[int], tar : int ):
    for i in range (len(num)):
        for j in range (i + 1 , len(num)):
            if num[i] + num[j] == tar:
                print([i ,j])
tsum([2,7,11,15],9)