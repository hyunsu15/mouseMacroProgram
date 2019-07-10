import pyautogui as autoGui
import mss,time
import cv2
import numpy as np

autoGui.PAUSE= 0.045

#플레이어 마다 아이콘의 밝기와 위치가 조금씩 다르다. 그러므로 그 부분을 유의.
#나는 LD플레이어를씀.
# (뇌피셜) 빨리 처리하다보니 전꺼의 잔상에 색이 입력되어 콤보가 깨지는것같음.

icon_length = 105
icon_height = 700
left_icon_pos = {'left': 130, 'top': icon_height,
                 'width': icon_length, 'height': icon_length}
right_icon_pos = {'left': 330, 'top': icon_height,
                  "width": icon_length, "height": icon_length}

button_height = 895
left_button = [100, button_height]
right_button = [355, button_height]

state_sword = "SWORD"
state_jewel = "JEWEL"
fail_count =0;
fever_count =0;
count =0;
def doAction():
    with mss.mss() as sct:
        global  fail_count,fever_count
        left_img = np.array(sct.grab(left_icon_pos))[:, :, :3]
        right_img = np.array(sct.grab(right_icon_pos))[:, :, :3]

        left_icon = compute_icon_typeByRGB(left_img)
        right_icon = compute_icon_typeByRGB(right_img)

        if left_icon == state_sword:
            click(left_button)
        elif right_icon == state_sword:
            click(right_button)
        elif left_icon == state_jewel and right_icon == state_jewel:
            click(left_button)
        else:
            fail_count+=1;

def compute_icon_typeByRGB(image):
    global count
    rgb = np.mean(image, axis=(0, 1))
    result = False

    if rgb[0] > 140 and rgb[1] > 50 and rgb[1] < 100 and rgb[2] > 110:
        result = 'SWORD'
    elif rgb[0] > 130 and rgb[1] > 130 and rgb[2] > 90:
        result = 'JEWEL'


    return result

def click (axis):
    global fail_count
    autoGui.moveTo(x=axis[0],y=axis[1],duration=0.0)
    autoGui.mouseDown()
    autoGui.mouseUp()
    fail_count=0

while True:
    if fail_count> 5 :
       print("끝")
       break
    else:
        doAction()





