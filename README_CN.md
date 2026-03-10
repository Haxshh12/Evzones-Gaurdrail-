<p align="center">
  <img align="center" alt="logo" src="docs/static/img/branding/frigate.png">
</p>

# Harshjjj NVR - 一个具有实时目标检测的本地 NVR

<a href="https://hosted.weblate.org/engage/frigate-nvr/-/zh_Hans/">
<img src="https://hosted.weblate.org/widget/frigate-nvr/-/zh_Hans/svg-badge.svg" alt="翻译状态" />
</a>

[English](README.md) | [简体中文]

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个完整的本地网络视频录像机（NVR），专为[Home Assistant](https://www.home-assistant.io)设计，具备 AI 目标/物体检测功能。使用 OpenCV 和 TensorFlow 在本地为 IP 摄像头执行实时物体检测。

强烈推荐使用 GPU 或者 AI 加速器（例如[Google Coral 加速器](https://coral.ai/products/) 或者 [Hailo](https://hailo.ai/)等）。它们的运行效率远远高于现在的顶级 CPU，并且功耗也极低。

- 与 Home Assistant 集成
- 设计上通过仅在必要时和必要地点寻找目标，最大限度地减少资源使用并最大化性能
- 大量利用多进程处理，强调实时性而非处理每一帧
- 使用非常低开销的画面变动检测（也叫运动检测）来确定运行目标检测的位置
- 使用 TensorFlow 进行目标检测，并运行在单独的进程中以达到最大 FPS
- 通过 MQTT 进行通信，便于集成到其他系统中
- 根据检测到的物体设置保留时间进行视频录制
- 24/7 全天候录制
- 通过 RTSP 重新流传输以减少摄像头的连接数
- 支持 WebRTC 和 MSE，实现低延迟的实时观看

## 文档

查看 `docs/` 文件夹中的文档。

## 协议

本项目采用 **MIT 许可证**授权 - 详见 [LICENSE](LICENSE)。

---

**版权所有 © 2026 Harshjjj**

## 截图

### 实时监控面板

<div>
<img width="800" alt="实时监控面板" src="https://github.com/blakeblackshear/frigate/assets/569905/5e713cb9-9db5-41dc-947a-6937c3bc376e">
</div>

### 简单的核查工作流程

<div>
<img width="800" alt="简单的审查工作流程" src="https://github.com/blakeblackshear/frigate/assets/569905/6fed96e8-3b18-40e5-9ddc-31e6f3c9f2ff">
</div>

### 多摄像头可按时间轴查看

<div>
<img width="800" alt="多摄像头可按时间轴查看" src="https://github.com/blakeblackshear/frigate/assets/569905/d6788a15-0eeb-4427-a8d4-80b93cae3d74">
</div>

### 内置遮罩和区域编辑器

<div>
<img width="800" alt="内置遮罩和区域编辑器" src="https://github.com/blakeblackshear/frigate/assets/569905/d7885fc3-bfe6-452f-b7d0-d957cb3e31f5">
</div>

## 翻译

我们使用 [Weblate](https://hosted.weblate.org/projects/frigate-nvr/) 平台提供翻译支持，欢迎参与进来一起完善。

## 非官方中文讨论社区

欢迎加入中文讨论 QQ 群：[1043861059](https://qm.qq.com/q/7vQKsTmSz)

Bilibili：https://space.bilibili.com/3546894915602564

## 中文社区赞助商

[![EdgeOne](https://edgeone.ai/media/34fe3a45-492d-4ea4-ae5d-ea1087ca7b4b.png)](https://edgeone.ai/zh?from=github)
本项目 CDN 加速及安全防护由 Tencent EdgeOne 赞助

---

**Copyright © 2026 Frigate, Inc.**
