
test_list= """
select the test topic :
1 Data Types
2 Control flow
3 Functions
4 Exit
"""

def load_test():
    while True:
        print(test_list)
        test_choice = input ()
        print("user choice:", test_choice)

        if test_choice == "1":
            print("Data types has been started : total time is 5 mins")
        
        elif test_choice == '4':
             print("logged out succefully.")
             break
        
        else:
            print("inccorect coice , pls try again...")
    




if __name__ == "__main__":
    load_test()
