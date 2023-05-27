#importing the necessary libraries
import cv2
from transformers import BlipProcessor, BlipForConditionalGeneration

#defining the BlipProcessor class instance to process the input image
processor= BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

#defining the model BlipForConditionalGeneration to generate the captions
model= BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

#defining a predict function

def predict_caption(image_path):
    raw_img=cv2.imread(image_path) # reading the image as an numpy array
    
    inputs=processor(raw_img,return_tensors="pt") #fetching the tensors of the image for processing 
    
    out= model.generate(
        **inputs,
        num_beams=3, # generating 3 captions using beam search
        max_length=16,# maximum length of the generated caption
        num_return_sequences=3# generating 3 different caption for the input image
        
    )
    
    captions=[] #creating a list to store the caption as a list
    for i,caption in enumerate(out): # iterating over the generated list and appending it in the list
        captions.append(processor.decode(caption,skip_special_tokens=True)) # removing any specila tokens at the begining & at the end of the generated string
    a=captions[0]
    b=captions[1]
    c=captions[2]
    
    #returning the lines of the generated captions
    return f"{a}\n{b}\n{c}"
        

