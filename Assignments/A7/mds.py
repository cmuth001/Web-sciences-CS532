import clusters

def mds():
    blognames, words, data = clusters.readfile('blogdata.txt')
    coords, itercount = clusters.scaledown(data)
    clusters.draw2d(coords, labels=blognames, jpeg='mds.jpg')
    print ('Iteration count: %d' % itercount)

if __name__ == "__main__":
    mds()