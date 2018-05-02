
from numpredict import *


def estimate(vectorValues, vectorBlog1, vectorBlog2):
    nn = knnestimate(allBlogVector.values(), vectorBlog1)
    print("\n\n************\tF-Measure\t************")
    kvals = [1, 2, 5, 10, 20]
    for k in kvals:
        print('k =', k)
        for j in range(k):
            print('%s' % (list(allBlogVector.keys())[nn[j][1]]))
        print("--------" )

    print("************\tWeb Science and Digital Libraries Research Group\t************")
    nn = knnestimate(allBlogVector.values(), vectorBlog2)
    for k in kvals:
        print('k =', k)
        for j in range(k):
            print('%s' % (list(allBlogVector.keys())[nn[j][1]]))
        print("--------" )



def formatData():
    givenBlog_1 = 'F-Measure'
    givenBlog_2 = 'Web Science and Digital Libraries Research Group'
    allBlogVector = {}
    blog1List = []
    blog2List = []
    with open("blogdata.txt", 'r') as f:
        allLines = f.readlines()
        for i, line in enumerate(allLines):
            if i == 0:
                # skip header
                continue
            blogMatrix = line.strip().split('\t')
            if blogMatrix[0] == givenBlog_1:
                for i in range(1, len(blogMatrix)):
                    blog1List.append(float(blogMatrix[i]))
            elif blogMatrix[0] == givenBlog_2:
                for i in range(1, len(blogMatrix)):
                    blog2List.append(float(blogMatrix[i]))
            else:
                allBlogVector[blogMatrix[0]] = []
                for i in range(1, len(blogMatrix)):
                    allBlogVector[blogMatrix[0]].append(float(blogMatrix[i]))
    return allBlogVector, blog1List, blog2List


if __name__ == "__main__":
    allBlogVector, vectorBlog1, vectorBlog2 = formatData()
    estimate(allBlogVector.values(), vectorBlog1, vectorBlog2)