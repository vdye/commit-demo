import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def main():
    # Parse args
    parser = argparse.ArgumentParser(description='Manipulate and display images.')
    parser.add_argument('image', type=str,
                        help='the image to process')
    parser.add_argument('--output', '-o', metavar="path",
                        help='path to save the image')
    parser.add_argument('--invert', '-i', action='store_true',
                        help='invert the colors in the image')
    parser.add_argument('--grey', '--gray', '-g', action='store_true',
                        help='convert the image to greyscale')
    args = parser.parse_args()

    # Verify file validity
    if not os.path.isfile(args.image):
        parser.error(f'Specified file "{args.image}" does not exist!')

    # Read the image
    img = mpimg.imread(args.image)

    if args.invert:
        img = 255 - img

    if args.grey:
        img = np.average(img, axis=2)

    # Display the image
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    plt.show()

    if args.output:
        if not os.path.isdir(args.output):
            os.makedirs(args.output, exist_ok=True)
        img_basename = os.path.basename(args.image)
        plt.imsave(os.path.join(args.output, img_basename), img,
                   cmap='gray', vmin=0, vmax=255)

if __name__ == "__main__":
    main()
