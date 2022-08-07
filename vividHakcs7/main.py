import cv2
import os
from PIL import Image
import image_similarity_measures
# from sys import argv
import imageio as iio
from image_similarity_measures.quality_metrics import rmse, ssim, sre
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import main
import random
import pygame as pg

global color
global width
global random_index

global country_names
global europe_flags

width = 5
color = 'red'


def read_files():

    with open('countryList.txt', 'r') as file:
        main.country_names = file.read().split("\n")

    main.europe_flags = os.listdir('Flags_of_Europe')

global flag
flag = True

def init():
    while main.flag:

        global screen

        read_files()
        main.random_index = random.randrange(51)
        print("Please draw the flag from " + main.country_names[main.random_index])
        # cv2.imshow(str(country_flags[random_index]),str(country_flags[random_index]))


        pg.init()

        screen = pg.display.set_mode((400, 400))
        pg.display.flip()
        mainloop()
        if not flag:
            break
        main.flag = False


drawing = False
last_pos = None


def draw(event):
    global drawing, last_pos

    if event.type == pg.MOUSEMOTION:
        if drawing:
            mouse_position = pg.mouse.get_pos()
            if last_pos is not None:
                pg.draw.line(screen, color, last_pos, mouse_position, width)
            last_pos = mouse_position
    elif event.type == pg.MOUSEBUTTONUP:
        drawing = False
        last_pos = None
    elif event.type == pg.MOUSEBUTTONDOWN:
        drawing = True


def mainloop():
    global screen

    flag = True
    while flag:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                flag = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    pg.image.save(screen, "image.png")
                    print("Saving image")

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_b:
                    main.color = 'blue'
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    main.color = 'white'
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_n:
                    main.color = 'black'
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    main.color = 'red'
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_g:
                    main.color = 'green'
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_y:
                    main.color = 'yellow'
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_o:
                    main.color = 'orange'
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_m:
                    main.color = 'brown'
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_v:
                    main.color = 'gray'
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    main.color = 'purple'

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    main.width += 5
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_2:
                    main.width -= 5

            draw(event)
        pg.display.flip()
    # pg.quit()


init()

#
# for x in main.country_flags:
#     arr=str(x).split('.')
#     arr2=arr[0].split(' ')
#     name=arr2[2:]
#     name2=' '.join(name)
#
#     print(name2)
#     print('x = ' + x)
#     if name2==main.country_names[main.random_index]:
#         print("hi")
#         # img = argv[1]
img1 = 'image.png'
img2 = r'{}\{}'.format('Flags_of_Europe', str(main.europe_flags[main.random_index]))



fig1 = cv2.imread(img1)
fig2 = cv2.imread(img2)


ssim_measures = {}
rmse_measures = {}
sre_measures = {}
fig_yy=fig2.shape

fig_y=int(fig_yy[0])

scale_percent = 100  # percent of original img size
width1 = int(fig1.shape[1] * scale_percent*6.4 / 100)
height1 = int(fig1.shape[0] * scale_percent*((fig_y)/400)/ 100)
dim1 = (width1, height1)

scale_percent = 100  # percent of original img size
width2 = int(fig2.shape[1] * scale_percent / 100)
height2 = int(fig2.shape[0] * scale_percent / 100)
dim2 = (width2, height2)
#
# width1=fig1.width
# height1=fig1.height
# dim1=(width1,height1)
#
# width2=fig2.width
# height2=fig2.height
# dim2=(width2,height2)
# data_dir = 'dataset'

# img_path = os.path.join(data_dir, file)
# data_img = mpimg.imread(img_path)
fig11 = cv2.resize(fig1, dim1, interpolation=cv2.INTER_AREA)
fig22 = cv2.resize(fig2, dim2, interpolation=cv2.INTER_AREA)
ssim_measures = ssim(fig11, fig22)
rmse_measures = rmse(fig11, fig22)
sre_measures = sre(fig11, fig22)
# match=int((ssim_measures*100+sre_measures)//2-rmse_measures*100)
match=ssim_measures*100
# print("You got " + str(match) + " % match")
print("RMSE"+str(rmse_measures))
# print("You got " + str(rmse_measures) + " points")
# print("You got " + str(sre_measures) + " points")

# print(points)
if int(match)<65:
    print("Sorry your answer is incorrect")
else:
    print("Congrats! Your answer was right.")
#
# cv2.imshow('image',img2)
# cv2.waitKey()
#




#
# img1 = 'image.png'
# img2 = 'image.png'
#
#
# fig1 = cv2.imread(img1)
# fig2 = cv2.imread(img2)
#
#
# ssim_measures = {}
# rmse_measures = {}
# sre_measures = {}
#
# scale_percent = 100  # percent of original img size
# width1 = int(fig1.shape[1] * scale_percent / 100)
# height1 = int(fig1.shape[0] * scale_percent/ 100)
# dim1 = (width1, height1)
#
# scale_percent = 100  # percent of original img size
# width2 = int(fig2.shape[1] * scale_percent / 100)
# height2 = int(fig2.shape[0] * scale_percent / 100)
# dim2 = (width2, height2)
#
# data_dir = 'dataset'
#
# # img_path = os.path.join(data_dir, file)
# # data_img = mpimg.imread(img_path)
# fig11 = cv2.resize(fig1, dim1, interpolation=cv2.INTER_AREA)
# fig22 = cv2.resize(fig2, dim2, interpolation=cv2.INTER_AREA)
#
# ssim_measures = ssim(fig11, fig22)
# rmse_measures = rmse(fig11, fig22)
# sre_measures = sre(fig11, fig22)
# print("You got " + str(int(ssim_measures * 100)) + " % match")
#
#
#



