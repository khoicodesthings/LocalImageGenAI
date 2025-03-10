# Stable Diffusion WebUI (Automatic1111) Setup Guide

This guide provides instructions on how to set up and host your own image generation model using [Automatic1111's Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui).

## Prerequisites/Assumptions I will make about you

- **Operating System:** Windows/Linux/Mac
- **GPU:** Either your system has a dedicated NVIDIA GPU with at least 8GB VRAM (higher VRAM recommended for larger models) OR you know how to get access to a virtual machine with similar specs (either through [Google Cloud](https://cloud.google.com/gpu) or [runpod](https://www.runpod.io/))
- **Drivers:** Ensure you have the latest NVIDIA drivers installed
- **Some Other Requirements:**
  - Python 3.10 or higher
  - Git
  - CUDA (for NVIDIA GPUs)

## Installation

This is how I do it on both Windows and Linux. The A1111's repo has very detailed instructions on how to install on different operating systems.

### 1. Clone the Repository
```sh
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui
```

### 2. Download a Model Checkpoint
- Download a Stable Diffusion model (e.g., **v1.5, v2.1, SDXL**)
- Place the `.ckpt` or `.safetensors` file in the `models/Stable-diffusion` directory.

## 3. Running the WebUI
To start the server, use:
```sh
./webui.sh --listen  # For Linux/Mac
webui-user.bat       # For Windows
```
- By default, the WebUI runs on **http://localhost:7860**
- To make it accessible over a network, add the `--listen` flag:
  ```sh
  ./webui.sh --listen
  ```
- You can also configure other parameters inn the `webui-user.bat` file for Windows, or `webui-user.sh` file for Linux.

- My prefered commandline arguments: `--device-id=0 --port [whatever OPEN port number you prefer] --no-half-vae --xformers --listen --api`

---

### References
- [Automatic1111 WebUI GitHub](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [Stable Diffusion Models](https://huggingface.co/stabilityai)
