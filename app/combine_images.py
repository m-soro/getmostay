from PIL import Image
import os

def combine_images(list_of_images, location, name=None, stack='h'):
        images = [Image.open(image) for image in list_of_images]
        widths, heights = zip(*(i.size for i in images))

        if stack == 'h':
            combined_image = Image.new('RGB', (sum(widths), max(heights)))
            x_pos = 0
            for im in images:
                combined_image.paste(im, (x_pos,0))
                x_pos += im.size[0]

        elif stack =='v':
            combined_image = Image.new('RGB', (widths[0], heights[0] + (sum(heights)-heights[0])))
            y_pos = 0
            for im in images:
                combined_image.paste(im, (0,y_pos))
                y_pos += im.size[1]

        for image in list_of_images:
            os.remove(image)

        return combined_image.save(location)
