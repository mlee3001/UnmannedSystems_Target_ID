from PIL import Image, ImageDraw

# Image dimensions
width = 4056
height = 3040

# Create a new image with a white background
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Rectangle dimensions and color
rectangle_width = 35
rectangle_height = 28
rectangle_color = (0, 0, 255)  # RGB values for blue

# Calculate the position of the rectangle
rectangle_x = (width - rectangle_width) // 2
rectangle_y = (height - rectangle_height) // 2

# Draw the blue rectangle on the image
draw.rectangle(
    [rectangle_x, rectangle_y, rectangle_x + rectangle_width, rectangle_y + rectangle_height],
    fill=rectangle_color,
)

# Save the generated image
image.save("output_image.png")

# Display the image (optional)
image.show()