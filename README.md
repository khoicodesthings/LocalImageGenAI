# Stable Diffusion WebUI (Automatic1111) Setup Guide

This guide provides instructions on how to set up and host your own image generation model using [Automatic1111's Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui).

## Prerequisites

- **Operating System:** Windows/Linux/Mac
- **GPU:** NVIDIA GPU with at least 4GB VRAM (higher VRAM recommended for larger models)
- **Drivers:** Ensure you have the latest NVIDIA drivers installed
- **Software Requirements:**
  - Python 3.10 or higher
  - Git
  - CUDA (for NVIDIA GPUs)

## Installation

This is how I do it, there are other ways to do it on A1111's repo

### 1. Clone the Repository
```sh
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui
```

### 2. Download a Model Checkpoint
- Download a Stable Diffusion model (e.g., **v1.5, v2.1, SDXL**)
- Place the `.ckpt` or `.safetensors` file in the `models/Stable-diffusion` directory.

### 3. Install Dependencies
#### Windows:
Run:
```sh
webui-user.bat
```
#### Linux/Mac:
Run:
```sh
bash webui.sh
```
This script will automatically install required dependencies and start the WebUI.

## Running the WebUI
To start the server, use:
```sh
./webui.sh --listen  # For Linux/Mac
webui-user.bat       # For Windows
```
- By default, the WebUI runs on **http://127.0.0.1:7860**
- To make it accessible over a network, add the `--listen` flag:
  ```sh
  ./webui.sh --listen
  ```

## Additional Features
- **Customizing UI:** Modify settings in `config.json`
- **Installing Extensions:** Use the "Extensions" tab to install community add-ons
- **Optimizing Performance:**
  - Enable `--medvram` or `--lowvram` for GPUs with limited VRAM
  - Use `--xformers` for improved efficiency

## Troubleshooting
- **WebUI not launching?** Ensure Python and Git are installed.
- **Black images?** Your model might be corrupted or missing a VAE file.
- **Slow generation?** Try reducing the resolution or using a more optimized sampler.

---

### References
- [Automatic1111 WebUI GitHub](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [Stable Diffusion Models](https://huggingface.co/stabilityai)
