from PIL import Image

# Open image
img = Image.open("eg4.jpg")

# Resize to 200x200
img_resized = img.resize((200, 200))

# Save
img_resized.save("eg1_small.jpg")
