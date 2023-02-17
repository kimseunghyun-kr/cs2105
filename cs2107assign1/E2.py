str = "PF2107{Gurer_V5_n_YbG_Bs_Uby3f_Va_Gu1f_Ba3}"
# caesar cipher -> shift P->C F ->S
#  fixed by a rotational constant
minCap = ord('A')
maxCap = ord('Z')
minsmall = ord('a')
maxsmall = ord('z')

rot = ord('S') - ord('F')
# print(rot)
str1 = ""
for i in range(len(str)):
    if(ord(str[i]) in range(ord('a'), ord('z')) or ord(str[i]) in range(ord('A') , ord('Z'))):
        asciiVal = ord(str[i]) + rot
        if(asciiVal > maxsmall):
            asciiVal = asciiVal- maxsmall + minsmall -1 ;
        elif(ord(str[i]) <= maxCap and asciiVal > maxCap):
            asciiVal = asciiVal - maxCap + minCap - 1;
        chartoAdd = chr(asciiVal)
        # print(chartoAdd)
        str1+=chartoAdd
    else:
        str1 += str[i]
print(str1)
    
    