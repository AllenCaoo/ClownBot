import math

circus_tent = ":circus_tent:"
partying_face = ":partying_face:"
yes_no_questions = ['is', 'are', 'will', 'wont', "won't", 'do', 'does', "don't",
                    'dont', 'doesnt', "doesn't", "am", "should", "can", "r"]


def dist(pt1, pt2):
    x1 = pt1[0]
    y1 = pt1[1]
    x2 = pt2[0]
    y2 = pt2[1]
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


def is_image(url):
    """Returns true if string url is an image"""
    return url[-3:].lower() == 'jpg' or url[-3:] == 'png' or url[-4].lower() == 'jpeg'
