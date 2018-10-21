def prod_non_zero_diag(x):
    x = [[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]]
    mult = 1
    for i in range(len(x)-1):
    if (x[i][i]>0 or x[i][i]<0):
    mult = mult*x[i][i]
    #len(x[0])- количевство столбцов
    for i in range(len(x[0])-1):
    if (x[i][len(x[0])-1-i]>0 or x[i][len(x[0])-1-i]<0) and (i>len(x[0])-1-i or i<len(x[0])-1-i):
    mult = mult*x[i][len(x[0])-i-1]
    print(mult) pass


def are_multisets_equal(x, y):
    x = [1, 2, 2, 4]
    y = [4, 2, 1, 2]
    status = False
    for i in range(len(x)):
        if (x[i] == y[i]):
        status = True
        break
    if (status):
         print("TRUE")
    else: 
         print("FALSE")
    pass


def max_after_zero(x):
    x = [6,2,0,3,0,0,5,7,0]
    max = -1111
    for i in range(1,len(x)):
         if (x[i-1]==0 and x[i]>max):
            max = x[i]
        print(max)
    pass


def convert_image(img, coefs):
    from PIL import Image
    img = Image.open('image.png').convert('LA')

    pass


def run_length_encoding(x):
    x = [2,2,2,3,3,3,5]
    counts = []
    elements = []
    for i in x:
         if(i not in elements):
            elements.append(i)
    for i in elements:
         counter = 0
            for j in x:
                  if(j==i):
                           counter +=1
                                counts.append(counter)
    print(elements)
    print(counts)
    pass

