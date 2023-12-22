from PIL import Image

def convert_to_bit_art(image_path, n_colors=8):
    try:
        # Open the image
        img = Image.open(image_path)

        # Convert the image to a fixed palette
        img = img.convert("P", palette=Image.ADAPTIVE, colors=n_colors)

        # Display the image
        img.show()

        # Save the converted image
        img.save("bit_art.png")

        print("Image converted to bit art successfully!")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")
    convert_to_bit_art(image_path)
