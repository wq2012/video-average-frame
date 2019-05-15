# Video Average Frame [![Build Status](https://travis-ci.org/wq2012/video-average-frame.svg?branch=master)](https://travis-ci.org/wq2012/video-average-frame)

## Summary

This is a Python tool to compute the average frame of a video.

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
python3 average.py --video=example.mp4 --output_image=average_frame.jpg --max_frames=5000
```

Then you will be generating an image like the following from this [example video](example.mp4):

![average_frame.jpg](average_frame.jpg)