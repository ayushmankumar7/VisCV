import cv2 

class TrackBar:
    def __init__(self, bar_type = "horizontal", intend = 0 ,thickness = 25):
        if bar_type in ['verticle', 'horizontal']:
            self.bar_type = bar_type
        else:
            print("Please enter bar_type from ['verticle', 'horizontal'].")
        if intend in [0, 1]:
            self.intend = intend
        self.thickness = thickness 

    def get_coord(self, img, length):
        coords = {
            'horizontal_0': [(0, 0), (img.shape[0] * length//100, self.thickness)],
            'horizontal_1': [(img.shape[0], 0), (img.shape[0] * (100-length)//100, self.thickness)],
            'verticle_0': [(0, 0), (self.thickness, img.shape[1] * (length)//100)],
            'verticle_1': [(0, img.shape[1]), (self.thickness, img.shape[1] * (100 - length)//100)]
        }
        return coords

    def __call__(self, img, length):
        """
            length in Percentage 
        """
        start_coord, end_coord = self.get_coord(img, length)[f"{self.bar_type}_{self.intend}"]
        cv2.rectangle(img, start_coord, end_coord,(255, 255, 255), -1)