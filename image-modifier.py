import os
import argparse
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def main():
    # Parse args
    parser = argparse.ArgumentParser(description='Manipulate and display images.')
    parser.add_argument('image', type=str,
                        help='the image to process')
    args = parser.parse_args()

    # Verify file validity
    if not os.path.isfile(args.image):
        parser.error(f'Specified file "{args.image}" does not exist!')

    # Read the image
    img = mpimg.imread(args.image)

    # Display the image
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
