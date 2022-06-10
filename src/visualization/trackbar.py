import cv2 

class TrackBar:
    def __init__(self, thickness = 25):
        self.thickness = thickness 

    def __call__(self, img, length):
        """
            length in Percentage 
        """
        end_coord = (img.shape[0] * length//100, self.thickness)
        cv2.rectangle(img, (0, 0), end_coord,(255, 255, 255), -1)