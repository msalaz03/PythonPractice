def simpleArraySum(ar):
   return sum(ar)
    
arr = [25,4,3,66,7,2]
arr.sort()

total_max = 0
total_min = 0

time_str = "12:01:00AM"

hours = int(time_str[:2])
minutes = int(time_str[3:5])
seconds = int(time_str[6:8])

# if time_str.endswith('Am'):
#     if hours == 12:
#         hours = 0
#     else:
#         if hours != 12:
#             hours+= 12    
    
# return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# for i in range (len(arr) - 4,len(arr)):
#     total_max += arr[i]
    
# for i in range(0, len(arr)  - 2):
#     total_min += arr[i]
    
# print(f"{total_max} {total_min}")

#Birthday Cake Candles

