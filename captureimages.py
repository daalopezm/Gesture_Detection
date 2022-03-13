import cv2
import os
import time
import uuid

#Intall opencv: pip install opencv-python
NUMBER_IMAGES: int = 15
#IMAGES_PATH = os.path.join('workspace', 'images','try_2','test')
IMAGES_PATH = os.path.join('workspace', 'images','try_4','train')

def run():
    labels = ['indicearriba', 'indiceabajo', 'indiceizquierda', 'indicederecha']
    #labels = ['indiceabajo']
    number_imgs = NUMBER_IMAGES
    if not os.path.exists(IMAGES_PATH):
        os.makedirs(IMAGES_PATH) #os.makedirs() to make the intermediate folders
    capture_images(labels, number_imgs)

def capture_images(labels, number_imgs):
    for label in labels:
        camara = cv2.VideoCapture(0)
        print(f'Capturando imagenes para {label}')
        time.sleep(5)
        for imgnum in range(number_imgs):
            print(f'Imagen {imgnum}')
            retval, frame = camara.read()
            imgname = os.path.join(IMAGES_PATH, f'{label}.{str(uuid.uuid1())}.jpg')
            cv2.imwrite(imgname, frame)
            cv2.imshow('frame',frame)
            time.sleep(2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    camara.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run()