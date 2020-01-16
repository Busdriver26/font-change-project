import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
import os


def cxg():
    path = '.\\src\\'
    pathout ='.\\out\\'
    ls = os.listdir(path)
    output = np.zeros((97,81,3),int)
    for name in ls:
        src = mpimg.imread(path+name)
        for i in range(0,16):
            for j in range(0,16):
                if src[i][j][1] == 0:
                    for m in range(i*6,i*6+6):
                        for n in range(j*5,j*5+5):
                            if m<=3+i*6 and n<=3+j*5:
                                if (m,n) != (i*6,j*5) and (m,n) != (i*6,j*5+3) and (m,n) != (i*6+3,j*5) and (m,n) != (i*6+3,j*5+3):
                                    output[m+1,n+1] =[255,255,255]
                                    #print(1,end="")
                            else:
                                output[m+1,n+1] =0
                                #print(0,end="")
                else:
                    for m in range(i*6,i*6+6):
                        for n in range(j*5,j*5+5):
                            output[m+1,n+1] =0
        plt.imsave(pathout+name[:-4]+'.png', output)


if __name__ == '__main__':
    cxg()
    # print(__name__)
