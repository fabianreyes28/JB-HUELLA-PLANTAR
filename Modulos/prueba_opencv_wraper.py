#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:56:27 2020

@author: fabian
"""


import os
import cv2
import numpy as np
from scipy import stats
image = cv2.imread('contornos.png')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#dilation
kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)

#find contours
ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# https://www.pyimagesearch.com/2015/04/20/sorting-contours-using-python-and-opencv/
def sort_contours(cnts, method="left-to-right"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))

    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)

sortedctrs,sortedbbs=sort_contours(ctrs)
xyminmax=[]
for cnt in sortedctrs:
    x, y, w, h = cv2.boundingRect(cnt)
    xyminmax.append([x,y,x+w,y+h])

distances=[]
for i in range(len(xyminmax)):
    try:
        first_xmax = xyminmax[i][2]
        second_xmin = xyminmax[i + 1][0]
        distance=abs(second_xmin-first_xmax)
        distances.append(distance)
    except IndexError:
        pass

THRESHOLD=stats.mode(distances, axis=None)[0][0]

new_rects=[]
for i in range(len(xyminmax)):
    try:
        # [xmin,ymin,xmax,ymax]
        first_ymin=xyminmax[i][1]
        first_ymax=xyminmax[i][3]

        second_ymin=xyminmax[i+1][1]
        second_ymax=xyminmax[i+1][3]

        first_xmax = xyminmax[i][2]
        second_xmin = xyminmax[i+1][0]

        firstheight=abs(first_ymax-first_ymin)
        secondheight=abs(second_ymax-second_ymin)

        distance=abs(second_xmin-first_xmax)

        if distance<THRESHOLD:
            new_xmin=xyminmax[i][0]
            new_xmax=xyminmax[i+1][2]
            if first_ymin>second_ymin:
                new_ymin=second_ymin
            else:
                new_ymin = first_ymin

            if firstheight>secondheight:
                new_ymax = first_ymax
            else:
                new_ymax = second_ymax
            new_rects.append([new_xmin,new_ymin,new_xmax,new_ymax])
        else:
            new_rects.append(xyminmax[i])
    except IndexError:
        pass

for rect in new_rects:
    cv2.rectangle(image, (rect[0], rect[1]), (rect[2], rect[3]), (121, 11, 189), 2)
cv2.imwrite("result.png",image) 