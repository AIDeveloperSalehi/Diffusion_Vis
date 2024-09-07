from PIL import Image

def combine_gifs(graph_gif_path, image_gif_path, output_path):
    # Open both GIF files
    graph_gif = Image.open(graph_gif_path)
    image_gif = Image.open(image_gif_path)

    # Calculate the dimensions for each GIF in the combined frame
    target_width = 400  # You can adjust this value
    target_height = 400  # You can adjust this value

    # Create a list to store the combined frames
    combined_frames = []

    # Iterate through the frames of both GIFs
    while True:
        try:
            # Get the current frame from each GIF
            graph_frame = graph_gif.copy()
            image_frame = image_gif.copy()

            # Resize both frames to the target size
            graph_frame = graph_frame.resize((target_width, target_height), Image.LANCZOS)
            image_frame = image_frame.resize((target_width, target_height), Image.LANCZOS)

            # Create a new blank image for the combined frame
            combined_frame = Image.new('RGB', (target_width * 2, target_height), (255, 255, 255))

            # Paste the graph frame on the left
            combined_frame.paste(graph_frame, (0, 0))

            # Paste the image frame on the right
            combined_frame.paste(image_frame, (target_width, 0))

            # Append the combined frame to the list
            combined_frames.append(combined_frame)

            # Move to the next frame in both GIFs
            graph_gif.seek(graph_gif.tell() + 1)
            image_gif.seek(image_gif.tell() + 1)

        except EOFError:
            # End of one or both GIFs
            break

    # Save the combined frames as a new GIF
    combined_frames[0].save(
        output_path,
        save_all=True,
        append_images=combined_frames[1:],
        optimize=False,
        duration=200,  # Adjust this value to control animation speed
        loop=0
    )

    print(f"Combined GIF saved as {output_path}")

# Usage
combine_gifs('graph_animation.gif', 'image_animation.gif', 'combined_animation.gif')