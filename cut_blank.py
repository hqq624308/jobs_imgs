import cv2
import os 
import numpy as np 

<<<<<<< HEAD

=======
>>>>>>> cb36f60 (add cut_v2)
def cut_write(img):
    window_height,window_width = 200,200
    h,w = img.shape[:2]
    for y in range(10,h):
        flag = False
        window_region = img[y:y+window_height,:window_width]
        target= np.sum(window_region[:,:,0])//(window_height*window_width)
        for j in range(window_height):
<<<<<<< HEAD
            for i in range(window_width):
=======
            for i in range(10,window_width):
>>>>>>> cb36f60 (add cut_v2)
                if target-5 <= window_region[j,i,0] <= target+5:
                    flag=True
                else:
                    flag= False
                    break
            if not flag:
                break
        if flag:
            break
    return img[:y]

imgs_path = './imgs_cut_v1/'
save_path = './save_imgs_cut/'
if not os.path.exists(save_path):
    os.mkdir(save_path)
imgs_list = os.listdir(imgs_path)
for f in imgs_list:
    print("Processing: ",f)
    full_path = os.path.join(imgs_path,f)
    img = cv2.imread(full_path)
    print(img.shape)
    img_cut = cut_write(img=img)
    cv2.imwrite(save_path+'cut_'+f,img_cut)
