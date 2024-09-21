# Video Average Frame [![Python application](https://github.com/wq2012/video-average-frame/actions/workflows/python-app.yml/badge.svg)](https://github.com/wq2012/video-average-frame/actions/workflows/python-app.yml)

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
pip3 install numpy opencv-python
```

## Install the package

You can install the package:

```
pip3 install "video-average-frame @ git+https://github.com/wq2012/video-average-frame.git"
```

After install the package, you can use the binary tool `video-average-frame`directly from your command line terminal:

```
video-average-frame --video=example.mp4 --output_image=average_frame.jpg --max_frames=5000
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
