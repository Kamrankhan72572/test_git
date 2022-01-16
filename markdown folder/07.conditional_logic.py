# logical operators are either true or false, yes or no,0 or 1,
# equal to                              ==
# # not equal to                        !=
# greater than                          >
# less than                             <
# greater than or equal to              =>
# less than or equal to                 =<


print(4==4)
print(4!=4)
print(4>3)
print(5<6)
print(5>=3)
print(5<=6)


# application of logical operators

hammad_age=4
age_at_school=5
print(hammad_age==age_at_school)


# input function and logical operators

age_at_school=5
hammad_age=input("how old is hammad")
print(type(hammad_age))
print(hammad_age==age_at_school)

age_at_school=5
hammad_age=input("how old is hammad")
hammad_age=int(hammad_age)
print(type(hammad_age))
print(hammad_age==age_at_school)