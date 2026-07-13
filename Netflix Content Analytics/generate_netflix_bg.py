import numpy as np
from PIL import Image, ImageFilter

def generate_background():
    # Resolution: 1920 x 1080 (16:9 aspect ratio for Power BI)
    width, height = 1920, 1080
    
    # Base dark color (RGB: 20, 20, 20 - Netflix dark gray-black)
    base_color = np.array([20, 20, 20])
    
    # Create the base image array
    arr = np.zeros((height, width, 3), dtype=np.uint8)
    arr[:, :] = base_color
    
    # Create coordinates grid
    y, x = np.ogrid[:height, :width]
    
    # Glow 1: Vibrant Netflix Red (Center on the left: x=250, y=250)
    glow1_x, glow1_y = 250, 250
    glow1_radius = 550.0
    glow1_color = np.array([229, 9, 20])  # Netflix Red (RGB: 229, 9, 20)
    
    dist1_sq = (x - glow1_x)**2 + (y - glow1_y)**2
    # Radial falloff
    intensity1 = np.exp(-dist1_sq / (2 * glow1_radius**2))
    
    # Glow 2: Dark Crimson Red (Center on the right: x=1650, y=800)
    glow2_x, glow2_y = 1650, 800
    glow2_radius = 650.0
    glow2_color = np.array([178, 7, 16])  # Dark Crimson (RGB: 178, 7, 16)
    
    dist2_sq = (x - glow2_x)**2 + (y - glow2_y)**2
    intensity2 = np.exp(-dist2_sq / (2 * glow2_radius**2))
    
    # Combine glows into the base array
    for i in range(3):
        # Scale and add intensities
        glow_channel = (intensity1 * glow1_color[i] * 0.35) + (intensity2 * glow2_color[i] * 0.30)
        arr[:, :, i] = np.clip(arr[:, :, i] + glow_channel, 0, 255).astype(np.uint8)
        
    # Convert to PIL Image
    img = Image.fromarray(arr)
    
    # Apply a gentle Gaussian blur to smooth out the gradient glows
    img = img.filter(ImageFilter.GaussianBlur(radius=15))
    
    # Save the generated premium background image
    img.save("Netflix_Background.png", "PNG")
    print("Background image 'Netflix_Background.png' successfully generated!")

if __name__ == "__main__":
    generate_background()
