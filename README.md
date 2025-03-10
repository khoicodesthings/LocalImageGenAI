# Stable Diffusion WebUI (Automatic1111) Setup Guide

This guide provides instructions on how to set up and host your own image generation model using [Automatic1111's Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui).

## Prerequisites/Assumptions I Will Need To Make

- **Operating System:** Windows/Linux/Mac
- **GPU:** Either your system has a dedicated NVIDIA GPU with at least 8GB VRAM (higher VRAM recommended for larger models) OR you know how to get access to a virtual machine with similar specs (either through [Google Cloud](https://cloud.google.com/gpu) or [runpod](https://www.runpod.io/))
  - The A1111's repo has installation guide if you have an AMD or Intel GPU, but I have not tested those steps yet. We will be using the instructions for NVIDIA GPUs for this workshop.
- **Drivers:** Ensure you have the latest NVIDIA drivers installed
- **Some Other Requirements:**
  - Python 3.10.6 (if you have an older or newer Python version, you will need to uninstall and then reinstall this version)
  - Git

## Installation

This is how I do it on both Windows and Linux. The A1111's repo has very detailed instructions on how to install on different operating systems.

### 1. Clone the Repository
```sh
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui
```

### 2. Get Some Models
- Download a Stable Diffusion model (e.g., **v1.5, v2.1, SDXL**) from huggingface.
- Place the `.safetensors` file in the `models/Stable-diffusion` directory.
- Experiment with different model sizes to figure out what works best for your setup!

## Running the WebUI
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

- My prefered commandline arguments:
   ```sh
    --device-id=0 --port [whatever OPEN port number you prefer] --no-half-vae --xformers --listen --api
   ```

## Generate Some Images!

- Generate with whatever prompts you would like!
- Experiment with the different parameters in the UI!

## Advanced: Use the API in your own code

- With the `--api` tag, you can read the API documentations at the `/docs` subdirectory (i.e. `localhost:7860/docs`); or you can also click the `API` link at the bottom of the web UI.
- In your scripts, send requests to the `/sdapi/v1/txt2img` endpoint.
- For example, if you web UI is hosted at the default port 7860, you would point your requests to `http://localhost:7860/sdapi/v1/txt2img` with the appropriate json payload for parameters.
- See `generate.py` for an example (thanks Dr. Maiti for letting me steal your code)
- Before running the script, make sure you have:
  - A working Python environment (which you should already have if you are able to run the web ui)
  - The following Python packages:
    - `requests`
    - `Pillow`
- You can install these packages using `pip`
   ```sh
    pip install requests Pillow
    ```

---

### References
- [Automatic1111 WebUI GitHub](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [Stable Diffusion Models](https://huggingface.co/stabilityai)
