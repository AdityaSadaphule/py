# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

list1 = {"Januaray": 2200,
         "February": 2350,
         "March": 2600,
         "April": 2130,
         "May": 2190}

# 1. In Feb, how many dollars you spent extra compare to January?
print(f"""1].In Feb, dollars you spent extra compare to January is {list1.get("February") - list1.get("Januaray")}""")# 150

# 2. Find out your total expense in first quarter (first three months) of the year
print(f"""2].Total expense in first quarter (first three months) of the year {list1.get("Januaray") + list1.get("February") + list1.get("March")}""")
 # 7150

# 3. Find out if you spent exactly 2000 dollars in any month
print(f"""3].If you spent exactly 2000 dollars in any month is {2000 in list1.values()}""") # False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
list1["June"] = 1980
print(f"""4].{list1}""")

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
list1["April"] = 2130-200
print(f"""4].{list1}""")
