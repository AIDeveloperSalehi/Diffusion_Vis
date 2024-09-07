from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_image_animation(image_path, x0, y0, width, height):
    # Load your image and flip it vertically
    img = Image.open(image_path)
    img_array = np.array(img).astype(np.float32) / 255.0  # Normalize to [0, 1]
    img_array = np.flipud(img_array)  # Flip the image vertically

    # Ensure the fixed part doesn't exceed image boundaries
    y0 = img_array.shape[0] - y0 - height  # Adjust y0 due to the flip
    y1 = min(y0 + height, img_array.shape[0])
    x1 = min(x0 + width, img_array.shape[1])

    # Define the fixed part of the image based on input parameters
    fixed_part = img_array[y0:y1, x0:x1, :]

    # Function to update the image
    def update(frame):
        # Create a noisy image
        noisy_img = np.random.random(img_array.shape)
        
        # Gradually blend the noisy image with the original image
        blend_factor = frame / 100  # Assuming 100 frames
        blended_img = (1 - blend_factor) * noisy_img + blend_factor * img_array
        
        # Combine fixed and changing parts
        combined = blended_img.copy()
        combined[y0:y1, x0:x1] = fixed_part
        
        # Ensure all values are in [0, 1] range
        combined = np.clip(combined, 0, 1)
        
        # Update the plot
        plt.clf()
        plt.imshow(combined)
        plt.axis('off')

    # Create the animation
    fig, ax = plt.subplots(figsize=(10, 8))
    ani = animation.FuncAnimation(fig, update, frames=100, interval=50, repeat=False)
    
    # Save the animation
    ani.save('image_animation.gif', writer='pillow')

# Example usage
create_image_animation('sunset_image.jpg', x0=2400, y0=1000, width=1000, height=1000)