# Growing Neural Gas (GNG) Algorithm

Author: Roya Elisa Eskandani  
Last Update: January 24, 2024


## Overview

The Growing Neural Gas (GNG) algorithm is a self-organizing, unsupervised learning algorithm designed for data clustering and representation. Developed for the purpose of topological feature mapping, GNG is particularly useful for adapting to the underlying structure of input data in an incremental manner.

The algorithm begins with the initialization of a set of nodes representing prototypes in a high-dimensional space. These nodes are iteratively adjusted based on input data, with the network growing and adapting to the data distribution over time. GNG is capable of capturing the topological relationships and structures present in the input space.


## Application to Static Images

This implementation of the GNG algorithm is specifically tailored for processing static images. It leverages the algorithm's ability to discover and represent the spatial relationships between pixels in an image. The nodes in the neural gas network adapt to the color clusters and structures present in the image, providing a unique perspective on the organization of visual information.

The application allows for the exploration of the GNG algorithm's behavior in the context of image analysis and understanding. The algorithm's ability to capture the structure of static images makes it a valuable tool for image processing tasks, including segmentation and feature extraction.
![Growing Neural Gas](mosaic.mp4)


## Extension to Dynamic Images with Utility

Recent updates to the GNG algorithm introduce a novel functionality called "Utility." This enhancement enables the algorithm to be applied to dynamic images, where the underlying structures and features evolve over time. The Utility feature extends the adaptability of GNG to changing visual patterns, making it suitable for a broader range of applications, such as video analysis and real-time image processing.
![Growing Neural Gas with Utility](fish.mp4)

## Source (Images)

- Geometric Mosaic Pattern: [FreePik](https://www.freepik.com/free-vector/flat-design-geometric-mosaic-pattern_22376508.htm#query=geometric%20mosaic%20pattern&position=20&from_view=keyword&track=ais&uuid=68164815-dc32-41ab-a88e-9d9f63ccad7e)
- Fish: [Dribble](https://dribbble.com/shots/2865508-Swimming-Fish?utm_source=Clipboard_Shot&utm_campaign=ddebie&utm_content=Swimming%20Fish&utm_medium=Social_Share&utm_source=Clipboard_Shot&utm_campaign=ddebie&utm_content=Swimming%20Fish&utm_medium=Social_Share)