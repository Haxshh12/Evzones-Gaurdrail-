<p align="center">
  <img align="center" alt="logo" src="docs/static/img/branding/frigate.png">
</p>

# Harshjjj NVR - Realtime Object Detection for IP Cameras

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<a href="https://hosted.weblate.org/engage/frigate-nvr/">
<img src="https://hosted.weblate.org/widget/frigate-nvr/language-badge.svg" alt="Translation status" />
</a>

[English] | [简体中文](README_CN.md)

A complete and local NVR designed for [Home Assistant](https://www.home-assistant.io) with AI object detection. Uses OpenCV and Tensorflow to perform realtime object detection locally for IP cameras.

Use of a GPU or AI accelerator is highly recommended. AI accelerators will outperform even the best CPUs with very little overhead. See the documentation for supported [object detectors](docs/).

- Tight integration with Home Assistant via custom components
- Designed to minimize resource use and maximize performance by only looking for objects when and where it is necessary
- Leverages multiprocessing heavily with an emphasis on realtime over processing every frame
- Uses a very low overhead motion detection to determine where to run object detection
- Object detection with TensorFlow runs in separate processes for maximum FPS
- Communicates over MQTT for easy integration into other systems
- Records video with retention settings based on detected objects
- 24/7 recording
- Re-streaming via RTSP to reduce the number of connections to your camera
- WebRTC & MSE support for low-latency live view

## Documentation

View the documentation in the `docs/` folder.

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

**Copyright © 2026 Harshjjj**

## Screenshots

### Live dashboard

<div>
<img width="800" alt="Live dashboard" src="docs/static/img/screenshots/dashboard.png">
</div>

### Streamlined review workflow

<div>
<img width="800" alt="Streamlined review workflow" src="docs/static/img/screenshots/review.png">
</div>

### Multi-camera scrubbing

<div>
<img width="800" alt="Multi-camera scrubbing" src="docs/static/img/screenshots/scrubbing.png">
</div>

### Built-in mask and zone editor

<div>
<img width="800" alt="Built-in mask and zone editor" src="docs/static/img/screenshots/editor.png">
</div>

## Translations

We use [Weblate](https://hosted.weblate.org/projects/frigate-nvr/) to support language translations. Contributions are always welcome.

<a href="https://hosted.weblate.org/engage/frigate-nvr/">
<img src="https://hosted.weblate.org/widget/frigate-nvr/multi-auto.svg" alt="Translation status" />
</a>

---

**Copyright © 2026 Frigate, Inc.**
