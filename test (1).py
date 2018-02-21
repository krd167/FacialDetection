import cv2
import numpy as np
import sys
import math

faceCascade = cv2.CascadeClassifier('face.xml')
eyeCascade = cv2.CascadeClassifier('eye.xml')
smileCascade = cv2.CascadeClassifier('smile.xml')


def camera():
    cap = cv2.VideoCapture(0)
    while True:
        try:
            ret,frame = cap.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.1,
                minNeighbors = 5,
                minSize = (30,30),
                flags = cv2.CASCADE_SCALE_IMAGE
                )
            if faces == ():
                print('No Face Found')
            else:
                 print(faces)
                
                
            for (x,y,w,h) in faces:
                area = ((w)*(h))
                #print(h)
                cv2.circle(frame, (int(x+(w/2)),int(y+(h/2))),int(math.sqrt(area/math.pi)),(0,255,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]                
                '''eyes = eyeCascade.detectMultiScale(
                    roi_gray,
                    scaleFactor = 2,
                    minNeighbors = 5,
                    minSize = (20,20),
                    flags = cv2.CASCADE_SCALE_IMAGE)
                smiles = smileCascade.detectMultiScale(
                    roi_gray,
                    scaleFactor = 1.1,
                    minNeighbors = 5,
                    minSize = (30,30),
                    flags = cv2.CASCADE_SCALE_IMAGE)
                for (ex,ey,ew,eh) in eyes:
                    areaE = ((ew)*(eh))
                    #cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(255,0,0),1)
                    cv2.circle(roi_color,(int(ex+(ew/2)),int(ey+(eh/2))),int(math.sqrt(areaE/math.pi)),(0,0,255),2)
                for (sx,sy,sw,sh) in smiles:
                    areaS = sw*(sh)
                    cv2.circle(roi_color,(int(sx+(sw/2)),int(sy+(sh/2))),int(math.sqrt(areaS/math.pi)),(0,255,255),2)'''
            cv2.imshow('Face and eye detection',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except OSError as err:
            cap.release()
            cv2.destroyAllWindows()
            print("OS error: {0}".format(err))
            print('It failed')
            cap.release()
            cv2.destroyAllWindows()
            break
            
    cap.release()
    cv2.destroyAllWindows()




def picture():
    sf,sfMax = 1.1,2
    mn,mnMax = 1,10
    msx,msy,msxMax,msyMax = 1,1,20,20
    
    imgPath = ('pic.jpg')
    image = cv2.imread(imgPath)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    while True:
        faces = faceCascade.detectMultiScale(
                  gray,
                  scaleFactor = sf,
                  minNeighbors = mn,
                  minSize = (msx,msy),
                  flags = cv2.CASCADE_SCALE_IMAGE
                  )
        if len(faces) < 2 :
            print("found {0} faces!".format(len(faces)))
            sf+=.1
            mn+=1
            msx+=1
            msy+=1
                        
            '''if sf >= sfMax:
                sf = sfMax
            if mn >=mnMax:
                mn =mnMax
            if msx >= msxMax:
                msx = msxMax
            if msy >= msyMax:
                msy = msyMax
            '''
            if sf == sfMax and mn == mnMax and msx == msxMax and msy == msyMax:
                break
        else:
            print("found {0} faces!".format(len(faces)))
            for (x,y,w,h) in faces:
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
            break
    cv2.imshow('Faces',image)
    cv2.waitKey(0)    



camera()
#picture()
