# f = open("file1.txt","r") # if mode not specified by default mode is "r"
# data = f.read()
# print(data)
# f.close()
# f = open("file1.txt","r")  #you can not perform multiple read in single read
# data1 = f.read(7)
# print(data1)
# f.close()

# # Read by line
# f = open("file1.txt","r")  #you can not perform multiple read in single read
# data2 = f.readline()
# print(data2)
# data2 = f.readline()
# print(data2)
# f.close()

# # to write to file ,it will replace content
# f = open("file1.txt","w")
# f.write("Thanks for Visit")
# f.close()
# f = open("file1.txt","r")
# data4 = f.read()
# print(data4)
# f.close()

# #to append content to end
# f = open("file1.txt","a")
# f.write("\nGood Day")
# f.close()
# f = open("file1.txt","r")
# data5 = f.read()
# print(data5)
# f.close()


# # With statement 
# with open("file1.txt","r") as f:
#     a = f.read()
# print(a)
# # with statement close the file automatically 


# Update high score of game by file_io 
def game():
    return 57

score = game()

with open("high.txt","r") as f:
    high = f.read()

if high=="" or score>int(high):
    with open("high.txt","w") as f:
        f.write(str(score))



    
