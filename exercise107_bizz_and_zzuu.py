# Write a bizz and zzuu game ##project

# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu



# Learn about how to define a function
# remember what is DRY?
# what is separation of concerns?
# Turn this into a functional program

# Definition of done for the project:
# This should be it's own project
# it should have a read me
    # it should outline the project
    # it should have simple instructions on how to run the project
# it should have git and git history
# it should be on git hub

def bizz_zzuu(num):
    if num % 3 == 0 and num % 5 == 0:
        return str(num) + ' is a multiple of 3 or 5, bizzzzuu'
    elif num % 3 == 0:
        return str(num) + ' is a multiple of 3, bizz!'
    elif num % 5 == 0:
        return str(num) + ' is a multiple of 5, zzuu!'
    else:
        return str(num) + ' is not a multiple of 3 or 5, please try again.'

print(bizz_zzuu(30))
print(bizz_zzuu(33))
print(bizz_zzuu(35))
print(bizz_zzuu(37))
