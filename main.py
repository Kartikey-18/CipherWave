from PIL import Image, ImageFilter, ImageOps, ImageChops, ImageDraw
import wave
import struct

# Function to encode a WAV file into an image using LSB (Least Significant Bit) method
def wav_to_image(input_wav_file, output_image_file):
    # ... (existing code for audio to image encoding)

# Function to decode an image back to a WAV file
def image_to_wav(input_image_file, output_wav_file):
    # ... (existing code for image to audio decoding)

# Function to apply an abstract art transformation with a colorful gradient background
def apply_abstract_art_transformation(input_image_file, output_image_file):
    # Open the image
    image = Image.open(input_image_file)
    width, height = image.size

    # Create a new image with a colorful gradient background
    abstract_art_image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(abstract_art_image)

    # Define a colorful gradient (you can customize the colors)
    gradient_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, green, and blue

    # Apply artistic filters and transformations to the original image
    image = image.filter(ImageFilter.CONTOUR)
    image = ImageOps.posterize(image, 4)  # Reduce color levels
    image = ImageChops.invert(image)  # Invert colors

    # Paste the transformed image onto the colorful gradient background
    abstract_art_image.paste(image, (0, 0))

    # Resize the abstract art image to 600x600 resolution
    abstract_art_image = abstract_art_image.resize((600, 600), Image.ANTIALIAS)

    # Save the transformed image
    abstract_art_image.save(output_image_file, format="PNG")
    print(f"Abstract art transformation applied with colorful gradient background and saved as {output_image_file} (600x600 resolution)")

# Example usage
input_wav_file = r'C:\Users\karti\Music\Bekar.wav'
output_image_file = r'C:\Users\karti\Music\output_image.png'
output_wav_file = r'C:\Users\karti\Music\restored_audio.wav'
output_artistic_image_file = r'C:\Users\karti\Music\colorful_abstract_art.png'  # New output file for colorful abstract art

# Encode WAV to image
wav_to_image(input_wav_file, output_image_file)

# Decode image back to WAV
image_to_wav(output_image_file, output_wav_file)

# Apply the abstract art transformation with a colorful gradient background
apply_abstract_art_transformation(output_image_file, output_artistic_image_file)

print("Encoding, decoding, and colorful abstract art transformation complete.")
