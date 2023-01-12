import PIL.ImageGrab
screenshot = PIL.ImageGrab.grab()
#screenshot.show()
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = screenshot.size
# Setting the points for cropped image
left = 725
top = 145
right = 1789
bottom =  1209
# Cropped image of above dimension
# (It will not change original image)
im1 = screenshot.crop((left, top, right, bottom))
# Shows the image in image viewer
# im1.show()
im1.save("D:\chess\chess_screenshot.png")