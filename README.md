# Video Average Frame [![Build Status](https://travis-ci.org/wq2012/video-average-frame.svg?branch=master)](https://travis-ci.org/wq2012/video-average-frame)

## Summary

This is a Python tool to compute the average frame of a video. It also supports computing min, max and median.

## Motivation

This is useful when you want to take **long exposure photos**, but your phone
does not have adjustable shutter speed and ISO.

In such cases, use a tripod stand to take a video,
and use this tool to generate an average frame image.

## Requirement

This tool requires OpenCV python. Install it by:

```bash
pip3 install opencv-python
```

## Example Usage

You can use it like this:

```bash
python3 process.py --video=example.mp4 --output_image=average_frame.jpg --max_frames=5000
```

Then you will be generating an image like the following from this [example video](example.mp4):

![average_frame.jpg](average_frame.jpg)

You can also use the max frame instead of the average frame with `--mode=max`, and you will be generating an image like this one:

![max_frame.jpg](max_frame.jpg)

The median is a robust measure of central tendency. In average mode every frame is used, resulting in blurry images if something moves quickly in 
the video stream (e.g. seagull flying, buoy moving in the background).

Median uses the most typical value of the given pixel, providing a sharper image `--mode=median`:

![median_frame.jpg](median_frame.jpg)

Zoomed in images, average on the left, median on the right:

![average_vs_median](average_vs_median.jpg)
