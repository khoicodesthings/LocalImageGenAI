import random
import requests
import io
import base64
from PIL import Image

def generate_images(ip, port, model_params, prompt="cat", num_images=5):
    filenames = []
    for i in range(num_images):
        # Generate a random seed for each image
        seed = random.randint(0, 4294967295)
        
        # Build the payload for the txt2img API endpoint
        payload = {
            "prompt": prompt,
            "negative_prompt": "",  # Modify if needed
            "steps": model_params["steps"],
            "cfg_scale": model_params["cfg_scale"],
            "width": model_params["width"],
            "height": model_params["height"],
            "sampler_index": model_params["sampler"],
            "seed": seed
        }
        
        try:
            # Include the custom port in the URL
            response = requests.post(
                url=f'http://{ip}:{port}/sdapi/v1/txt2img', 
                json=payload, 
                timeout=30
            )
            response.raise_for_status()  # Check for HTTP errors
            r = response.json()
            
            # Process returned images (the API returns a list in r['images'])
            for img_data in r['images']:
                # Remove any header if present (e.g., "data:image/png;base64,")
                image = Image.open(io.BytesIO(base64.b64decode(img_data.split(",",1)[0])))
                
                # Save the image with a unique filename
                filename = f"cat_{i}.png"
                image.save(filename)
                print(f"Saved {filename}")
                filenames.append(filename)
        except requests.exceptions.Timeout:
            print(f"Timeout occurred while generating image {i}")
        except Exception as e:
            print(f"An error occurred on iteration {i}: {e}")
    return filenames

if __name__ == "__main__":
    ip = "localhost" # or whatever url on your network
    port = 7860  # or whatever port number you chose
  
    # Define your model parameters (update as needed)
    model_params = {
        "steps": 20,
        "cfg_scale": 7,
        "width": 1024,
        "height": 1024,
        "sampler": "Euler"
    }

    # Define a prompt
    prompt = "cat, cute, perfect, anime, ghibli, detailed, 4k, ultra hd"
    
    # Generate cat images and get the list of filenames
    image_files = generate_images(ip, port, model_params, prompt=prompt, num_images=5)
