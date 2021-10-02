from PIL import Image
import matplotlib.pyplot as pyplot

image = Image.open('./image/sistine-chapel.png')


###########################################---MENU BUILDER---###########################################

def set_line(size=50):
    return '-' * size


def header(text):
    print(set_line())
    print(text.center(50))
    print(set_line())


def menu(list):
    header('HISTOGRAM MAIN MENU')
    print('Select the type of image you want to see the histogram:\n')
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c += 1
    print('\n{}'.format(set_line()))


menu(['Original Image(RGBA)', 'Black & White Image', 'RGB Image', 'Exit'])


##########################################################################################################


def original():
    global image
    print(image.mode)
    print('Image size{}'.format(image.size))
    image.show()
    pyplot.hist(image.histogram())
    pyplot.show()


def blackAndWhite():
    global image
    imageConverted = image.convert('L')
    print(imageConverted.mode)
    print('Image size{}'.format(image.size))
    imageConverted.show()
    pyplot.hist(imageConverted.histogram())
    pyplot.show()


def rgb():
    global image
    imageConverted = image.convert('RGB')
    print(imageConverted.mode)
    print('Image size{}'.format(image.size))
    imageConverted.show()
    pyplot.hist(imageConverted.histogram())
    pyplot.show()


def switch(case_selected):
    if case_selected == 1:
        return original()
    elif case_selected == 2:
        return blackAndWhite()
    elif case_selected == 3:
        return rgb()
    elif case_selected == 4:
        return exit()
    else:
        print('You typed a wrong character!')


if __name__ == '__main__':
    case_selected = int(input())
    switch(case_selected)
