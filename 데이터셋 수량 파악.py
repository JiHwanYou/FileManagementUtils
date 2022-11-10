import os
import natsort

def main(input_dir):
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
                if file.endswith('.jpg'):
                    jpg_list.append(file)
                elif file.endswith('.txt'):
                    txt_list.append(file)

        if len(jpg_list) != len(txt_list):
            print(f'[WRONG CASE] {dir}, {len(jpg_list), len(txt_list)}')
        else:
            print(f'{dir}, {len(jpg_list)}')


if __name__ == "__main__":
    input_dir = r"\\172.16.0.7\Next k\lab\Dataset\labelled\detection\Human\AI_HUB\Abandonment"

    main(input_dir)