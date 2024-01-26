import numpy as np
import cv2 as cv
import random
import math


# --------------------------------------------Settings------------------------------------------- #
to_blend_background = True
image_blur = True
image_blur_size = 5
shape_max_size = 90
shape_min_size = 30
frame_width = 600
frame_height = 600
blur_size = 15
channels = 4
repeat_count = 1
shape_output_path = ""
background_file_path = [
    "grass1.jpg",
    "grass2.jpg",
    "grass3.jpg",
    "grass4.jpg",
]
common_rgb = {
    "blue" : (255, 0, 0, 255),      "green" : (0, 255, 0, 255),    "red" : (0, 0, 255, 255), 
    "white" : (255, 255, 255, 255), "orange" : (0, 165, 255, 255), "purple" : (204, 0, 204, 255),
    "brown" : (0, 75, 150, 255),    "black" : (0, 0, 0, 255),
}
# --------------------------------------------Settings------------------------------------------- #


def generate_circle(frame, frame_width, frame_height, min_radius, max_radius, color):
    radius = random.randint(min_radius, max_radius)
    O_x = random.randint(radius, frame_width - radius)
    O_y = random.randint(radius, frame_height - radius)
    cv.circle(frame, (O_x, O_y), radius, color, -1)
    return frame

def generate_semi_circle(frame, frame_width, frame_height, min_radius, max_radius, color):
    radius = random.randint(min_radius, max_radius)
    O_x = random.randint(radius, frame_width - radius)
    O_y = random.randint(radius, frame_height - radius)
    rotation = random.randint(0, 360)
    cv.ellipse(frame, (O_x, O_y), (radius, radius), rotation, 0, 180, color, -1)
    return frame

def generate_quater_circle(frame, frame_width, frame_height, min_radius, max_radius, color):
    radius = random.randint(min_radius, max_radius)
    O_x = random.randint(radius, frame_width - radius)
    O_y = random.randint(radius, frame_height - radius)
    rotation = random.randint(0, 360)
    cv.ellipse(frame, (O_x, O_y), (radius, radius), rotation, 0, 90, color, -1)
    return frame

def generate_triagnle(frame, frame_width, frame_height, min_length, max_length, color):
    rotation = random.randint(-6, 6)
    length = random.randint(min_length, max_length)
    O_x = random.randint(length, frame_width - (length))
    O_y = random.randint(length, frame_height - (length))
    pts = []
    for i in range(3):
        p = (length * math.cos(2*math.pi*i / 3 + rotation) + O_x,
             length * math.sin(2*math.pi*i / 3 + rotation) + O_y)
        pts.append(p)
    pts = np.array(pts, np.int32)
    pts = pts.reshape((-1,1,2))
    cv.fillPoly(frame, [pts], color)
    return frame

def generate_rectangle(frame, frame_width, frame_height, min_length, max_length, color):
    width = random.randint(min_length, max_length)
    height = random.randint(min_length, max_length)
    length = min([width, height])
    rotation = random.randint(-6, 6)
    O_x = random.randint(length, frame_width - (length))
    O_y = random.randint(length, frame_height - (length))
    p1 = (-width//2, -height//2)
    p2 = ( width//2, -height//2)
    p3 = ( width//2,  height//2)
    p4 = (-width//2,  height//2)
    p1 = (p1[0] * math.cos(rotation) - p1[1] * math.sin(rotation) + O_x,
          p1[0] * math.sin(rotation) + p1[1] * math.cos(rotation) + O_y)
    p2 = (p2[0] * math.cos(rotation) - p2[1] * math.sin(rotation) + O_x,
          p2[0] * math.sin(rotation) + p2[1] * math.cos(rotation) + O_y)
    p3 = (p3[0] * math.cos(rotation) - p3[1] * math.sin(rotation) + O_x,
          p3[0] * math.sin(rotation) + p3[1] * math.cos(rotation) + O_y)
    p4 = (p4[0] * math.cos(rotation) - p4[1] * math.sin(rotation) + O_x,
          p4[0] * math.sin(rotation) + p4[1] * math.cos(rotation) + O_y)
    pts = np.array([p1, p2, p3, p4], np.int32)
    pts = pts.reshape((-1,1,2))
    cv.fillPoly(frame, [pts], color)
    return frame

def generate_pentagon(frame, frame_width, frame_height, min_length, max_length, color):
    rotation = random.randint(-6, 6)
    length = random.randint(min_length, max_length)
    O_x = random.randint(length, frame_width - (length))
    O_y = random.randint(length, frame_height - (length))
    pts = []
    for i in range(5):
        p = (length * math.cos(2*math.pi*i / 5 + math.pi/2 + rotation) + O_x,
             length * math.sin(2*math.pi*i / 5 + math.pi/2 + rotation) + O_y)
        pts.append(p)
    pts = np.array(pts, np.int32)
    pts = pts.reshape((-1,1,2))
    cv.fillPoly(frame, [pts], color)
    return frame

def generate_cross(frame, frame_width, frame_height, min_length, max_length, color):
    length = random.randint(min_length, max_length)
    rotation = random.randint(0, length)
    O_x = random.randint(length, frame_width - (length))
    O_y = random.randint(length, frame_height - (length))
    p1 = (int(O_x - length / math.sqrt(2)), int(O_y - length / math.sqrt(2) + rotation))
    p2 = (int(O_x + length / math.sqrt(2)), int(O_y + length / math.sqrt(2) - rotation))
    p3 = (int(O_x + length / math.sqrt(2) - rotation), int(O_y - length / math.sqrt(2)))
    p4 = (int(O_x - length / math.sqrt(2) + rotation), int(O_y + length / math.sqrt(2)))

    cv.line(frame, p1, p2, color, thickness = int(length * 0.3))
    cv.line(frame, p3, p4, color, thickness = int(length * 0.3))
    return frame

def generate_star(frame, frame_width, frame_height, min_length, max_length, color):
    rotation = random.randint(-6, 6)
    length = random.randint(min_length, max_length)
    length_ = length // 2
    O_x = random.randint(length, frame_width - (length))
    O_y = random.randint(length, frame_height - (length))
    pts = []
    for i in range(5):
        p = (length * math.cos(2*math.pi*i / 5 + rotation) + O_x,
             length * math.sin(2*math.pi*i / 5 + rotation) + O_y)
        
        p_ = (length_ * math.cos(2*math.pi*i / 5 + 2*math.pi/10 + rotation) + O_x,
              length_ * math.sin(2*math.pi*i / 5 + 2*math.pi/10 + rotation) + O_y)
        pts.append(p)
        pts.append(p_)
    pts = np.array(pts, np.int32)
    pts = pts.reshape((-1,1,2))

    cv.fillPoly(frame, [pts], color)
    return frame

def blend_background(bg_img, img_to_overlay_t):
    if not to_blend_background:
        return img_to_overlay_t
    
    bg_img = cv.resize(bg_img, (frame_width, frame_height))
    overlay_color = img_to_overlay_t[:,:, :-1]
    mask = img_to_overlay_t[:,:,3]

    # Black-out the area behind the logo in our original ROI
    img1_bg = cv.bitwise_and(bg_img.copy(), bg_img.copy(), mask = cv.bitwise_not(mask))

    # Mask out the logo from the logo image.
    img2_fg = cv.bitwise_and(overlay_color, overlay_color, mask = mask)

    # Update the original image with our new ROI
    bg_img = cv.add(img1_bg, img2_fg)

    if image_blur:
        bg_img = cv.GaussianBlur(bg_img, (image_blur_size, image_blur_size), 0)

    return bg_img

def main():
    backgrounds = []
    for path in background_file_path:
        img = cv.imread(path)
        backgrounds.append(img)

    for i in range(repeat_count):
        for color_name, color in common_rgb.items():
            # Circle
            frame = np.zeros((frame_width, frame_height, channels), np.uint8)
            frame = generate_circle(frame, frame_width, frame_height, shape_min_size, shape_max_size, color)
            bg_n = random.randint(0, len(backgrounds) - 1)
            frame = blend_background(backgrounds[bg_n], frame)
            cv.imwrite(f"{shape_output_path}circle_{color_name}_{i}.png", frame)

            # Semi Circle
            frame = np.zeros((frame_width, frame_height, channels), np.uint8)
            frame = generate_semi_circle(frame, frame_width, frame_height, shape_min_size, shape_max_size, color)
            bg_n = random.randint(0, len(backgrounds) - 1)
            frame = blend_background(backgrounds[bg_n], frame)
            cv.imwrite(f"{shape_output_path}semi_circle_{color_name}_{i}.png", frame)

            # Quater Circle
            frame = np.zeros((frame_width, frame_height, channels), np.uint8)
            frame = generate_quater_circle(frame, frame_width, frame_height, shape_min_size, shape_max_size, color)
            bg_n = random.randint(0, len(backgrounds) - 1)
            frame = blend_background(backgrounds[bg_n], frame)
            cv.imwrite(f"{shape_output_path}quater_circle_{color_name}_{i}.png", frame)

            # Triangle
            frame = np.zeros((frame_width, frame_height, channels), np.uint8)
            frame = generate_triagnle(frame, frame_width, frame_height, shape_min_size, shape_max_size, color)
            bg_n = random.randint(0, len(backgrounds) - 1)
            frame = blend_background(backgrounds[bg_n], frame)
            cv.imwrite(f"{shape_output_path}triangle_{color_name}_{i}.png", frame)

            # Rectangle
            frame = np.zeros((frame_width, frame_height, channels), np.uint8)
            frame = cv.resize(frame, (frame_width, frame_height))
            frame = generate_rectangle(frame, frame_width, frame_height, shape_min_size, shape_max_size, color)
            bg_n = random.randint(0, len(backgrounds) - 1)
            frame = blend_background(backgrounds[bg_n], frame)
            cv.imwrite(f"{shape_output_path}rectangle_{color_name}_{i}.png", frame)

            # Pentagon
            frame = np.zeros((frame_width, frame_height, channels), np.uint8)
            frame = generate_pentagon(frame, frame_width, frame_height, shape_min_size, shape_max_size, color)
            bg_n = random.randint(0, len(backgrounds) - 1)
            frame = blend_background(backgrounds[bg_n], frame)
            cv.imwrite(f"{shape_output_path}pentagon_{color_name}_{i}.png", frame)

            # Cross
            frame = np.zeros((frame_width, frame_height, channels), np.uint8)
            frame = generate_cross(frame, frame_width, frame_height, shape_min_size, shape_max_size, color)
            bg_n = random.randint(0, len(backgrounds) - 1)
            frame = blend_background(backgrounds[bg_n], frame)
            cv.imwrite(f"{shape_output_path}cross_{color_name}_{i}.png", frame)

            # Star
            frame = np.zeros((frame_width, frame_height, channels), np.uint8)
            frame = generate_star(frame, frame_width, frame_height, shape_min_size, shape_max_size, color)
            bg_n = random.randint(0, len(backgrounds) - 1)
            frame = blend_background(backgrounds[bg_n], frame)
            cv.imwrite(f"{shape_output_path}star_{color_name}_{i}.png", frame)

            # cv.imshow("frame", frame)
            # cv.waitKey(0)

if __name__ == "__main__":
    main()