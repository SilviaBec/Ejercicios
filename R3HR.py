def timeConversion(s):
    if "AM" in s:
        if s[0:2] =='12':
            return f'00:{s[3:8]}'  
        else:
            return s[0:8] 
    else:
        if s[0:2]=='12':
            return s[0:8]  
        else:
            return f'{str(int(s[0:2])+12)}:{s[3:8]}'
print(timeConversion('06:45:54PM'))