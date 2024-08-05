pa = input().split(',')
special_char = '@#$'
pass_word = []
for word in pa:
    if(
       any(c.isupper() for c in word) and 
       any(c.islower() for c in word) and
       any(c.isdigit() for c in word) and
       any(c in special_char for c in word) and 
       8<= len(word) <=12       
    ):
        pass_word.append(word)
print(','.join(pass_word))