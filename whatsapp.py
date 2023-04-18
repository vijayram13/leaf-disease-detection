# modules
import pywhatkit
import datetime
import matplotlib.pyplot as plt
import cv2
import pyautogui
import time

# 7008879179


def send_time():

    t = datetime.datetime.now()
    h = int(t.strftime("%H"))
    m = int(t.strftime("%M"))
    # Seconds
    s = int(t.strftime("%S"))
    return t, h, m, s


# send information through whatsapp
def send_information():
    """
    This Function is used to send the information by using 'pywhatkit' module.
    Documentation link: https://pypi.org/project/pywhatkit/

    """
    # CONSTANTS
    WAIT_TIME = 15
    TAB_CLOSE = True
    CLOSE_TIME = 15

    message = input("Enter Message: ")
    m_number = "+91" + input("Enter Mobile Number: ")

    # Function call send_time()
    t, hour, minute, second = send_time()

    # Current time
    curr_time = t.strftime("%X")
    print(f"Current Time: {curr_time}")

    if second >= 45:
        delay = 60-second
        print(f"Wait: {delay} sec")
        time.sleep(delay)
        t, hour, minute, second = send_time()

    # Same as above but Closes the Tab in 2 Seconds after Sending the Message
    pywhatkit.sendwhatmsg(m_number, message, hour, (minute + 1), WAIT_TIME, TAB_CLOSE, CLOSE_TIME)

    # image path
    img_path = 'C:/Users/NITRO/Desktop/road.jpg'

    # caption of the image
    caption = "caption"
    time.sleep(1)

    # Send an Image to a Contact with the no Caption
    #pywhatkit.sendwhats_image(m_number, img_path, caption, WAIT_TIME, TAB_CLOSE, CLOSE_TIME)

    print("Message sent Successfully")


def image_resizer():
    # Reading the image using imread() function
    image = cv2.imread('C:/Users/NITRO/Desktop/road.jpg', cv2.IMREAD_UNCHANGED)

    # Extracting the height and width of an image
    h, w = image.shape[:2]

    # Displaying the height and width
    print("Height = {},  Width = {}".format(h, w))

    # resize 400x400
    # Calculating the ratio
    ratio = 400 / w

    # Creating a tuple containing width and height
    dim = (400, int(h * ratio))

    # Resizing the image
    resize_aspect = cv2.resize(image, dim)

    # Converting BGR color to RGB color format
    RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    cv2.imshow("Image", resize_aspect)
    plt.imshow(resize_aspect)
    # plt.imshow(RGB_img)

    plt.waitforbuttonpress()
    plt.close('all')
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":

    # image processing
    #image_resizer()

    # to send information
    send_information()

    # Wait for Chrome to open


    time.sleep(3)

    # Close the Chrome window
    #pyautogui.hotkey('alt', 'f4')





