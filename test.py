import pyautogui as pag
# import time
# while True:
#     print(pag.position())
#     time.sleep(0.2)
#     if pag.position().x<=20:
#         break;

print(pag.size())
print((508+846)/2)
#
# from ctypes import windll
#
# def get_ppi():
#     LOGPIXELSX = 88
#     LOGPIXELSY = 90
#     user32 = windll.user32
#     user32.SetProcessDPIAware()
#     dc = user32.GetDC(0)
#     pix_per_inch = windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX)
#     print("Horizontal DPI is", windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX))
#     print("Vertical DPI is", windll.gdi32.GetDeviceCaps(dc, LOGPIXELSY))
#     user32.ReleaseDC(0, dc)
#     return pix_per_inch
#
# print(get_ppi())

#
#
# import pyautogui as pag
# import time
#
# time.sleep(2)
# button7location = pag.locateOnScreen('photo_collection/second_page.png')
# print(type(button7location))


# print(type({}))

#
# k=900
# while k>500:
#     k+=1
#     if k>1000:
#         break