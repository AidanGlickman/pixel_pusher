# Pixel Pusher

Some basic ways to interact with [pixel.acm.illinois.edu].

As of now, this script mainly consists of different rendering methods to put images on to pixel. More patterns and options will be added as I write them.
## Basic Usage

`./pixel.py -M 'render_method' -F 'filename'`

## Render Methods

### For Images

#### `image_linear`

This renderer just takes an image and draws it out to the screen row by row from the top to them bottom.

#### `image_grow`

This renderer grows the image out from the middle of the screen. It does this by drawing each subsequent ring of the image from the center.
