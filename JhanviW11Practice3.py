#COMBINED (HYBRID) LISTS[] AND TUPLES() #tuple section first, then second index for the item in the tuple
MachineLearning = [("Supervised", "Decision Tree"), ("Supervised", "Random Forest"), ("Unsupervised", "K-Means"), ("Unsupervised", "Gaussian Mixture Model")]

# print("Learning Type: ", MachineLearning[1][0])
# for item in MachineLearning:
#     if item[0] == "Supervised":
#         print(item[1])
#
# print("\nLearning Type: ", MachineLearning[3][0])
# for item in MachineLearning:
#     if item[0]=="Unsupervised":
#         print(item[1])

for learntype in ["Supervised", "Unsupervised"]:
    print("\nLearning Type: ", learntype)
    for item in MachineLearning:
        if item[0]==learntype:
            print(item[1])


    # print("Learning Type: ", item[0])
    # for algorithm in item[1]:
    #     print(algorithm)
#     if item[0]=="Supervised":
#         #print("Learning Type: Supervised")
#         print(item[1])
#     elif item[0]=="Unsupervised":
#         #print("Learning Type: Unsupervised")
#         print(item[1])
#     else:
#         print('Not in the list')
# #
# for item in MachineLearning:
#     if item[0]=="Unsupervised":
#         print(item[1])
#     else:
#         print("Not in list.")