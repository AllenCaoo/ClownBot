class Face:
    """A face includes 2 eyes and one nose"""

    def __init__(self, face_info):
        self.x = face_info[0]  # x coordinate
        self.y = face_info[1]  # y coordinate
        self.w = face_info[2]  # width
        self.h = face_info[3]  # height
        self.eyes = []
        self.nose = None

    def getFaceCenter(self):
        return self.x + self.w // 2, self.y + self.h // 2

    def addEyeWithInfo(self, eye_info):
        self.eyes.append(Eye(eye_info, self))

    def addEyeObject(self, e):
        self.eyes.append(e)

    def setNoseObject(self, nose):
        self.nose = nose

    def setNoseWithInfo(self, nose_info):
        self.nose = Nose(nose_info, self)


class Eye:
    def __init__(self, eye_info, face):
        self.x = eye_info[0]  # x coordinate
        self.y = eye_info[1]  # y coordinate
        self.w = eye_info[2]  # width
        self.h = eye_info[3]  # height
        self.face = face  # the face the eye belongs to

    def getEyeCenter(self):
        return self.face.x + self.x + self.w // 2, self.face.y + self.y + self.h // 2


class Nose:
    def __init__(self, eye_info, face):
        self.x = eye_info[0]  # x coordinate
        self.y = eye_info[1]  # y coordinate
        self.w = eye_info[2]  # width
        self.h = eye_info[3]  # height
        self.face = face  # the face the nose belongs to

    def getNoseCenter(self):
        return self.face.x + self.x + self.w // 2, self.face.y + self.y + self.h // 2
