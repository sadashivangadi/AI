#pip install transformers
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

processor=BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model=BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

image_path="test.jpg"
image = Image.open(image_path)

inputs = processor(image=image, return_tensors="pt")

out=model.generate(**inputs)
caption=processor.decode(out[0])
skip_special_tokens=True

print("generated caption:   ")
print(caption)  

                         