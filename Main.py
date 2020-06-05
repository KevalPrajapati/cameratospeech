import cv2
import pytesseract
from speaker import speak
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# Function to convert :: used later  
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1



#Capturing camera feed and when user presses q the feed at that momment is used further
cap = cv2.VideoCapture(0)
while(True):
    _,img =cap.read()
    

    cv2.imshow("tee",img) 
    k=cv2.waitKey(5) &0xFF


    
    if k == ord('q'):
        break

## BGR to RGB as pytesseract needs RGB   
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)



print("start")

print(pytesseract.image_to_data(img, lang='eng'))
hImg,wImg,_ = img.shape
Idata=pytesseract.image_to_data(img, lang='eng')
sentence=[""]
for x,b in enumerate(Idata.splitlines()):
    if x != 0:
        b=b.split()
##        print(b)
        if(len(b)==12):
##            x,y,w,h = int (b[6]),int(b[7]),int (b[8]),int (b[9])
##            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
##            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,255,50),2)
            wordhai = b[11]
            sentence.append(wordhai)
            sentence.append(" ")
##            print(wordhai)
            
        ##print(pytesseract.image_to_string(img))
speak(listToString(sentence))
cv2.imshow("tee",img)
cap.release()
##cv2.destroyAllWindows()
                
        
        
