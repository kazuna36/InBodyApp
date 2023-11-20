import cv2
import numpy as np
from tkinter import filedialog
filename = filedialog.askopenfilename()
print(filename)
buf = np.fromfile(filename,np.uint8)
print(type(buf))
img = cv2.imdecode(buf,cv2.IMREAD_UNCHANGED)
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
img = cv2.resize(img,(500,200))
cv2.imshow("Image", img)
cv2.waitKey()


