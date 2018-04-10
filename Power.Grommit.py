# create a program that utilizes a function

# the function should be exponential

#include edge cases for negative exponents, the power of 1, or the power of 0


# function should be able to take in negative numbers and float point numbers


'''
        
def power_func(n, p):
    power=1
    for mult in range(1,p+1):
        power= power * n
        print power
    if p==0:
        print 1
    elif p==1:
        print n
    elif p==-1:
        print (1/n)
    elif p==-p:
        print (1/x)**n
 '''          
    



#main program
n = int(raw_input("Enter an base to raised to a power: "))
p = int(raw_input("Enter a power: "))

result = power_func(n,p)


print "This program does a Grommit industry sales forecast"


ug_sales = int(raw_input("Please enter initial sales for UG: "))
gi_sales = int(raw_input("Please enter initial sales for GI: "))
increase_gi = int(raw_input("Enter annual growth for gi:" ))
increase_ug = int(raw_input("Enter annual growth for ug:" ))

ugbeg = ug_sales
gibeg = gi_sales

ug_ann=increase_gi/100.
gi_ann=increase_ug/100.

print "The Grommit Industry"

print " GROMMIT INDUSTRY"
print " FORECAST"
print
print "Year UG", "    ", "GI"

year_cross = 0 #initiate a counter for when the sales overlapped
start_date = 2017
end_date = 2026

for year in range(start_date, end_date+1): # for loop set up to include a range of years between 2017 and 2026 inclusive
    if year_cross == 0:
        if ugbeg > gibeg:
            if gi_sales > ug_sales:
                year_cross = year
        elif gibeg > ugbeg:
            if ug_sales > gi_sales:
                year_cross = year
    ug_sales = (ug_sales)*(1.+ ug_ann) # calculate the result of annual sale growth
    gi_sales = (gi_sales)*(1. + gi_ann) # calculate the result of annual sale growth
    print year, round(ug_sales,1)," ",round(gi_sales,1)    #print the start sales in a tabular format

    
if year_cross != 0:
    print "The sales crossed in", year_cross
else:
    print "The sales never crossed"
if gi_sales > ug_sales:
    if (gi_sales/ug_sales)>=1.25:
        print "In the final year GI's sales exceeded UG's sales by more than 25%"
elif ug_sales > gi_sales:
    if (ug_sales/gi_sales)>=1.25:
        print "In the final year UG's sales exceeded GI's sales by more than 25%"
else:
    print "They finished equal"
    
    


