# Creating a simple Interface for our Caption generator model using Gradio

#importing the required libraries
from Caption_generator import predict_caption
from PIL import Image
import gradio as gr

# creating the input image layout box to store and display the image

with gr.Blocks() as demo:
    image = gr.inputs.Image(type='filepath', label='Image') # defining the filepath to upload the image
    
    #defining the ouput layout box where the generate captions will be displayed
    label = gr.Text(label='Generated Caption')
    
    #Configuring the upload image option
    image.upload(
        predict_caption,
        [image],
        [label])
    
if __name__=='__main__':
    demo.launch()    