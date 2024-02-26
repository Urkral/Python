# # ------------------------------------------------------ Exo page 186 ----------------------------------------------------------------
# def is_year_leap(year):
#     if(year%4 == 0 and year%100 != 0) or (year%400 == 0):
#        return True
#     else: 
#        return False
# def days_in_month(year, month): 
    
#     if month == 2 and (year%4 == 0 | year%100 == 0) or (year%400 == 0):
#        return 29
#     elif month == 2 and (year%4 != 0 | year%100 != 0) or (year%400 != 0):
#        return 28
#     elif month == 1 | 3 | 5 | 7 | 8 | 10 | 12:
#        return 31
#     elif month == 4 | 6 | 9 | 11: 
#        return 30
#     else: 
#        return None

       

# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#  yr = test_years[i]
#  mo = test_months[i]
#  print(yr, mo, "->", end="")
#  result = days_in_month(yr, mo)
#  if result == test_results[i]:
#     print("OK")
#  else:
#     print("KO") 

# ------------------------------------ Exo page 204 -------------------------------------------------

# def factorial(n):
#  if n < 0:
#     return None
#  if n < 2:
#     return 1
 
#  product = 1
#  for i in range(2, n+1):
#     product *=i
#  return product
# for n in range(1,6):
#   print(n, factorial(n))


# --------------------------------- Exo page 206 ---------------------------------------------
