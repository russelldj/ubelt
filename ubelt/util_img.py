import cv2
import os
import argparse
import glob

def break_videos(video_folder, output_folder):
    if video_folder[-1] == '/':
        # make sure the formating is consistent
        video_folder = video_folder[0:-1]
    videos = sorted(glob.glob('{}/*'.format(video_folder)))
    for video in videos:
        basename = os.path.basename(video).split('.')[0]
        new_output_folder = '{}/{}'.format(output_folder, basename)
        if not os.path.isdir(new_output_folder):
            os.mkdir(new_output_folder)
        print(basename, new_output_folder)
        break_video(video, new_output_folder)

def break_video(video, output_folder):
    vid = cv2.VideoCapture(video)
    print("capture is open: {}".format(vid.isOpened()))
    if not os.path.isdir(args.output_folder):
        os.mkdir(args.output_folder)
    succ, frame = vid.read() # get the frame and whether it was successful
    frame_ind = 0
    while succ:
        cv2.imwrite('{}/{:06d}.jpeg'.format(output_folder, frame_ind), frame) # check whether this should be png
        succ, frame = vid.read()
        frame_ind += 1

def join_video(input_folder, output_file):
    images = sorted(glob.glob('{}/*'.format(input_folder)))
    img = cv2.imread(images[0])
    frame_height, frame_width = img.shape[:2]

    video_writer = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))
    for image_name in images:
        img = cv2.imread(image_name)
        video_writer.write(img)
    video_writer.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--function', type=str, default='break_video', help="select a functionality from the list: break_video, break_videos, join_video (others will be added eventually")
    parser.add_argument('--input_folder', type=str, default='', help='path to the video')
    parser.add_argument('--output_folder', type=str, default='~/temp/broken_video', help='path to write the output. Will be created if not present')
    parser.add_argument('--regex', type=str, help='An optional glob regex to filter the files in the input folder')

    args = parser.parse_args()
    if args.function == "break_video":
        break_video(args.input_folder, args.output_folder)
    elif args.function == "break_videos":
        break_videos(args.input_folder, args.output_folder)
    elif args.function == "join_video":
        join_video(args.input_folder, args.output_folder)

