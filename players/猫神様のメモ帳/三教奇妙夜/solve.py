import cv2
vc=cv2.VideoCapture("output.mp4")  #读入视频文件
c=1
if vc.isOpened():
    rval,frame=vc.read()
else:
    rval=False
count=0
save=0
while True:
    count=count+1
    if(count%60000==0):
        print("[*]"+str(count))
    rval,frame=vc.read()
    #print(len(frame[0]))
    if(frame[150][150][1]!=save): #每隔timeF帧进行存储操作
        cv2.imwrite(str(c)+'.jpg',frame) #存储为图像
        c=c+1
        save=frame[150][150][1]
        #print(frame[0][0][0])
vc.release()
