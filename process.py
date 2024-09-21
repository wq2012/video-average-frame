import argparse
import cv2
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(
        description="Arguments for the video frame averaging tool."
    )

    parser.add_argument("--video", type=str, help="Path to the source video.")

    parser.add_argument(
        "--output_image",
        default="",
        type=str,
        help="Path to the output averaged frame.",
    )

    parser.add_argument(
        "--max_frames",
        type=int,
        help="Max number of frames to use.",
    )

    parser.add_argument(
        "--mode",
        default="average",
        type=str,
        help="How to generate output image. Currently it can be "
        "`average` or `max` or `min` or `median`",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if not args.video:
        raise ValueError("Video file path is missing")

    if args.mode not in ["average", "max", "min", "median"]:
        raise ValueError("Unexpected mode {}".format(args.mode))

    cap = cv2.VideoCapture(args.video)

    if args.max_frames:
        max_frames = args.max_frames
    else:
        max_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    num_frames = 0
    average_frame = None
    max_frame = None
    min_frame = None
    median_frame = None
    median_median_frame = None

    while cap.isOpened():
        _, frame = cap.read()
        if frame is None:
            break
        if args.mode == "median":
            if median_frame is None:
                median_frame = np.array([frame])
            else:
                median_frame = np.append(
                    median_frame, np.array([frame]), axis=0
                )
                if num_frames % 50 == 0:
                    if median_median_frame is None:
                        median_median_frame = np.array(
                            [np.median(median_frame, axis=0)]
                        )
                        median_frame = None
                    else:
                        median_median_frame = np.append(
                            median_median_frame,
                            np.array([np.median(median_frame, axis=0)]),
                            axis=0,
                        )
                        median_frame = None
        else:
            if average_frame is None:
                average_frame = frame.astype(float)
                max_frame = frame
                min_frame = frame
            else:
                average_frame += frame.astype(float)
                max_frame = np.maximum(frame, max_frame)
                min_frame = np.minimum(frame, min_frame)
        num_frames += 1
        if (num_frames == 1 or num_frames % 1000 == 0 or
                num_frames >= max_frames):
            print(f"Processed frame {num_frames}/{max_frames}")
        if num_frames >= max_frames:
            break

    if not args.output_image:
        output_image = args.video + "." + args.mode + ".jpg"
    else:
        output_image = args.output_image
    if args.mode == "average":
        average_frame /= num_frames
        average_frame = average_frame.astype("uint8")
        cv2.imwrite(output_image, average_frame)
    elif args.mode == "max":
        cv2.imwrite(output_image, max_frame)
    elif args.mode == "min":
        cv2.imwrite(output_image, min_frame)
    else:
        if median_median_frame is None:
            median_median_frame = np.array([np.median(median_frame, axis=0)])
        elif num_frames % 50 > 25:
            median_median_frame = np.append(
                median_median_frame,
                np.array([np.median(median_frame, axis=0)]),
                axis=0,
            )
        cv2.imwrite(output_image, np.median(median_median_frame, axis=0))

    cap.release()
    print(
        "Output image saved to {}, {} frames used.".format(
            output_image, num_frames
        )
    )


if __name__ == "__main__":
    main()
