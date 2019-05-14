import argparse
import cv2


def parse_args():
    parser = argparse.ArgumentParser(
        description='Arguments for the video frame averaging tool.')

    parser.add_argument(
        '--video',
        type=str,
        help='Path to the source video.')

    parser.add_argument(
        '--output_image',
        type=str,
        help='Path to the output averaged frame.')

    parser.add_argument(
        '--max_frames',
        default=1000000,
        type=int,
        help='Max number of frames to use.')

    return parser.parse_args()


def main():
    args = parse_args()

    cap = cv2.VideoCapture(args.video)

    num_frames = 0
    average_frame = None

    while(cap.isOpened()):
        _, frame = cap.read()
        if frame is None:
            break
        if average_frame is None:
            average_frame = frame.astype(float)
        else:
            average_frame += frame.astype(float)
        num_frames += 1
        if num_frames >= args.max_frames:
            break

    average_frame /= num_frames
    average_frame = average_frame.astype('uint8')
    cv2.imwrite(args.output_image, average_frame)

    cap.release()
    print('Average frame image saved to {}, {} frames used.'.format(
        args.output_image, num_frames))


if __name__ == '__main__':
    main()
