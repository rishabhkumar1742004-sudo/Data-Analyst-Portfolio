import numpy as np
from PIL import Image

def generate_background():
    width, height = 1920, 1080
    sidebar_width = 300
    
    # Base canvas array
    arr = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Fill main content area with dark charcoal/black (RGB: 15, 15, 18)
    arr[:, sidebar_width:] = [15, 15, 18]
    
    # Fill left sidebar area with solid dark charcoal (RGB: 24, 24, 27)
    arr[:, :sidebar_width] = [24, 24, 27]
    
    # Add a thin separator line between sidebar and main content (Blinkit Green: 12, 131, 70)
    arr[:, sidebar_width:sidebar_width+4] = [12, 131, 70]
    
    # Convert to PIL Image and save
    img = Image.fromarray(arr)
    img.save("Blinkit_Background.png", "PNG")
    print("Background image 'Blinkit_Background.png' successfully generated in Dark mode!")

if __name__ == "__main__":
    generate_background()
