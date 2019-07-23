def mock(string):
    index = 0
    for i in string:
        if index % 2 == 0:
            if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
                temp_string1 = string[:index]
                temp_string2 = string[index+1:]
                temp_list = [temp_string1,temp_string2]
                if ord(i)>=97 and ord(i)<=122:
                    upper = chr(ord(i)-32)
                else:
                    upper = chr(ord(i)+32)
                string = upper.join(temp_list)
        index+=1
    return string

user_input = input("Enter word: ")
