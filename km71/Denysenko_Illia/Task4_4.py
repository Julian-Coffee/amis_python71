year_number = int(input(" Enter number of the year: "))
if year_number%4==0 and year_number%100!=0:
    print(" LEAP")
elif year_number%400==0:
    print(" LEAP")
else:
    print(" COMMON")
+input()