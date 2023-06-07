import cv2
import os 
import numpy as np 

def cut_write(img):
    window_height,window_width = 200,200
    h,w = img.shape[:2]
    for y in range(10,h):
        flag = False
        if y+window_height>=h:
            return img[:h]
        window_region = img[y:y+window_height,:window_width]   # window region  
        target= np.sum(window_region[:,:,0])//(window_height*window_width)
        for j in range(window_height-1):
            for i in range(10,window_width-1): #from pixel 10 
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

imgs_path = './imgs_cut_v2/'
save_path = './save_imgs_cut_v2/'
if not os.path.exists(save_path):
    os.mkdir(save_path)
imgs_list = os.listdir(imgs_path)
for f in imgs_list:
    print("Processing: ",f)
    full_path = os.path.join(imgs_path,f)
    img = cv2.imread(full_path)
    img_cut = cut_write(img=img)
    cv2.imwrite(save_path+'cut_'+f,img_cut)
