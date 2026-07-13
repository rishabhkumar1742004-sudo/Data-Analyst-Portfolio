import numpy as np
from PIL import Image, ImageFilter

def generate_background():
    # Resolution: 1920 x 1080 (16:9 aspect ratio for Power BI)
    width, height = 1920, 1080
    
    # Base dark slate color (RGB: 11, 15, 25)
    base_color = np.array([11, 15, 25])
    
    # Create the base image array
    arr = np.zeros((height, width, 3), dtype=np.uint8)
    arr[:, :] = base_color
    
    # Create coordinates grid
    y, x = np.ogrid[:height, :width]
    
    # Glow 1: Workforce Blue (Center on the left: x=300, y=300)
    # Brightness, Radius, and Color
    glow1_x, glow1_y = 300, 300
    glow1_radius = 500.0
    glow1_color = np.array([14, 116, 144])  # Deep Teal-Blue (RGB: 14, 116, 144)
    
    dist1_sq = (x - glow1_x)**2 + (y - glow1_y)**2
    # Radial falloff function
    intensity1 = np.exp(-dist1_sq / (2 * glow1_radius**2))
    
    # Glow 2: Attrition Orange (Center on the right: x=1620, y=780)
    glow2_x, glow2_y = 1620, 780
    glow2_radius = 600.0
    glow2_color = np.array([194, 65, 12])  # Rust-Orange (RGB: 194, 65, 12)
    
    dist2_sq = (x - glow2_x)**2 + (y - glow2_y)**2
    intensity2 = np.exp(-dist2_sq / (2 * glow2_radius**2))
    
    # Combine glows into the base array
    for i in range(3):
        # Scale and add intensities, clip values to 255
        glow_channel = (intensity1 * glow1_color[i] * 0.45) + (intensity2 * glow2_color[i] * 0.40)
        arr[:, :, i] = np.clip(arr[:, :, i] + glow_channel, 0, 255).astype(np.uint8)
        
    # Convert to PIL Image
    img = Image.fromarray(arr)
    
    # Apply a gentle Gaussian blur to smooth out any gradients
    img = img.filter(ImageFilter.GaussianBlur(radius=15))
    
    # Save the generated premium background image
    img.save("HR_Analytics_Background.png", "PNG")
    print("Background image 'HR_Analytics_Background.png' successfully generated!")

if __name__ == "__main__":
    generate_background()
