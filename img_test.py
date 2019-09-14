import cv2
import matplotlib.pyplot as plt


def print_img(img2):
    for i in range (0, len(img2)-1):
        for j in range (0, len(img2[i])-1):
            print("img[{}, {}]: {}".format(i, j, img2[i,j]))            


img      = cv2.imread('C:/Users/arw0174/Desktop/JonathanMoonTinder.png')
edges    = cv2.Canny(img, 100, 200, 3, L2gradient=True)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
test_img = gray_img

left_indice  = 0
right_indice = 0
size = len(edges[0])

for i in range (0, len(edges)-1):
    j = 0
    while(j < len(edges[i])-45):
        #print("edges[{}][{}]: {}".format(i, j, edges[i][j]))
        if (edges[i][j] == 255):            
            #print("i:{}, j:{}".format(i, j))
            while (edges[i][j] == 255):
                j = j+1
                if (j == size):
                    break
            left_indice = j
            #print("left_indice: {}".format(left_indice))
            if (left_indice == size):
                break
            while (edges[i][j] == 0):
                j = j+1
                if (j == size):
                    break
            right_indice = j
            #print("right_indice: {}".format(right_indice))
            if(gray_img[i][left_indice] < 25):
                test_img[i][left_indice:right_indice] = \
                    sorted(gray_img[i][left_indice:right_indice])
            else:
                test_img[i][left_indice:right_indice] = \
                    sorted(gray_img[i][left_indice:right_indice], reverse=True)
            
            left_indice  = 0
            right_indice = 0
        
        j = j+1
        if (j > size):
            break
        


plt.imshow(test_img, cmap='gray')
#plt.imshow(img)
print("len(img[0]): {}".format(len(img[0])))
print("len(img): {}".format(len(img)))

plt.figure()
plt.title('Test')
plt.imsave('Test_img.png', edges, cmap='gray', format='png')
plt.imshow(edges, cmap='gray')
plt.show()

    