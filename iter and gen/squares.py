def squares(n):
   curr_num = 1

   while curr_num <= n:
       yield curr_num ** 2
       curr_num +=1


print(list(squares(5)))
