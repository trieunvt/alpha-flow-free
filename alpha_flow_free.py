## author:  trieunvt
## file:    alpha_flow_free.py
## date:    01 Aug 2024
## version: v1.0.0
## brief:   Alpha Flow Free.

import sys
import cv2
import source.data.image_processor as ip

## The main program
def main():
    ## Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("USAGE: python alpha_flow_free.py [puzzle_image_path]")
        return

    print("ALPHA FLOW FREE", end="\n\n")

    ## Read an input image
    input_image = cv2.imread(sys.argv[1])

    ## Process an input image
    output_image = ip.process(input_image)

    ## Save an output image
    cv2.imwrite("solution.png", output_image)

    print("Level complete!")

if __name__ == "__main__":
    main()
