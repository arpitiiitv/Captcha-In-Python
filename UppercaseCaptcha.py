from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt
import random

# number list from 0 to  9
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# this function will create random captcha from number list
# function will take length of captcha as input

def create_random_captcha_uppercase(length=5):
    captcha_list=[]
    

    for i in range(length):
        # select one digit randomly
        char = random.choice(uppercase)
        # Append captcha to the list
        captcha_list.append(char)

    captcha_string=''
    #change character list to string
    for item in captcha_list:
        captcha_string += str(item)

    return captcha_string


# Create Image Captch with digits
def create_image(cap_text):
    image_captcha = ImageCaptcha()
    image = image_captcha.generate_image(cap_text) 

# save the image to a png file
    image_file =  ".\Bigger"+ cap_text +'.png'
    image_captcha.write(cap_text,image_file)

    # Display Image
    plt.imshow(image)
    plt.show()



## driver programme

if __name__ == '__main__':
    #create random digit
    random_lowercase = create_random_captcha_uppercase()

    #  create image captcha
    create_image(random_lowercase)





