import os
import cv2


def convert_from_video_to_img(video_path, image_dir, step):
    print(f"divide video by {step} steps")
    if not os.path.isdir(image_dir):
        os.makedirs(image_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    cnt = 1
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            if cnt % step == 0:
                filename = os.path.join(image_dir, f'{cnt//step}.jpg')
                cv2.imwrite(filename, frame)
            cnt += 1
        else:
            break

    
if __name__ == "__main__":
    video_path = r"C:\Users\user\Documents\GitHub\test_data\ITS_02.MP4"
    image_dir  = os.path.splitext(video_path)[0]
    step = 5
    
    convert_from_video_to_img(video_path, image_dir, step)