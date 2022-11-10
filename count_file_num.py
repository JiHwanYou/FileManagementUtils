import os
import natsort


def count_file_num(input_dir):
    """
    Args:
        input_dir (str): input directory
    
    Returns:
        bIsMatched: determine img_cnt & label_cnt is same
        dir : sub-directory name
        img_cnt : image count
        label_cnt : label (.txt) count
    """
    if not os.path.isdir(input_dir):
        print("Enter correct directory path")
        return

    dir_list = os.listdir(input_dir)
    dir_list = natsort.natsorted(dir_list)
    
    for dir in dir_list:
        dir_abs = os.path.join(input_dir, dir)

        jpg_list = []
        txt_list = []
        for (root, _, files) in os.walk(dir_abs):
            for file in files:
                if file.endswith('.jpg', 'png'):
                    jpg_list.append(file)
                elif file.endswith('.txt'):
                    txt_list.append(file)

        if len(jpg_list) != len(txt_list):
            yield (False, dir, len(jpg_list), len(txt_list))
        else:
            yield (True, dir, len(jpg_list), len(txt_list))


if __name__ == "__main__":
    input_dir = r"C:\Users\user\Documents\GitHub\test_data"

    print(f'{"file_path":<15s} {"SameNum":^8s} {"ImgCnt":^8s} {"LabelCnt":^8s}')
    for bIsMatched, dir, img_cnt, label_cnt in count_file_num(input_dir):
        print(f'{dir:<15s} {str(bIsMatched):^8s} {img_cnt:^8d} {label_cnt:^8d}')