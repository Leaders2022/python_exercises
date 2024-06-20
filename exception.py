# EXAMPLE OF A CODE WITH EXEMPTIONS
# myname="eMobilis"
#
# for i in myname:
#     if 1!-k:
#         print(i)
jina= ["banana", "mangoes", "apples"]
# I want to loop inside the list


try:
    # code that may raise exception
    result = 1/0

    for i in range(5):
        print(i, jina[i])


except ZeroDivisionError as e :
    print(f"An error has occured {e}")
finally:
    # code that runs no matter what
    print("This will always be printed")

# Format: Try, except, finally