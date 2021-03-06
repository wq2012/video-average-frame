import argparse
import cv2
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(
        description='Arguments for the video frame averaging tool.')

    parser.add_argument(
        '--video',
        type=str,
        help='Path to the source video.')

    parser.add_argument(
        '--output_image',
        default='',
        type=str,
        help='Path to the output averaged frame.')

    parser.add_argument(
        '--max_frames',
        default=1000000,
        type=int,
        help='Max number of frames to use.')

    parser.add_argument(
        '--mode',
        default='average',
        type=str,
        help='How to generate output image. Currently it can be either '
             '`average` or `max`')

    return parser.parse_args()


def main():
    args = parse_args()

    if args.mode not in {'average', 'max'}:
        raise ValueError('Unexpected mode {}'.format(args.mode))

    cap = cv2.VideoCapture(args.video)

    num_frames = 0
    average_frame = None
    max_frame = None

    while(cap.isOpened()):
        _, frame = cap.read()
        if frame is None:
            break
        if average_frame is None:
            average_frame = frame.astype(float)
            max_frame = frame
        else:
            average_frame += frame.astype(float)
            max_frame = np.maximum(frame, max_frame)
        num_frames += 1
        if num_frames >= args.max_frames:
            break

    average_frame /= num_frames
    average_frame = average_frame.astype('uint8')
    if not args.output_image:
        output_image = args.video + '.jpg'
    else:
        output_image = args.output_image
    if args.mode == 'average':
        cv2.imwrite(output_image, average_frame)
    else:
        cv2.imwrite(output_image, max_frame)

    cap.release()
    print('Output image saved to {}, {} frames used.'.format(
        output_image, num_frames))


if __name__ == '__main__':
    main()
