# AI Caption Generator
This project is an AI-based image caption generator that utilizes the Transformer model of Salesforce BLIP (Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation). The model is pretrained on the COCO dataset with a base architecture and ViT base backbone.

# Overview
The AI Caption Generator project leverages the power of Salesforce BLIP, a state-of-the-art VLP (Vision-Language Pretraining) framework. BLIP is designed to excel in both vision-language understanding and generation tasks. It effectively utilizes noisy web data through a caption bootstrapping approach. This involves generating synthetic captions using a captioner and filtering out the noisy ones using a filtering mechanism.

# Key Features
Image Captioning: The AI Caption Generator is capable of generating descriptive captions for images, providing valuable insights into the visual content.
State-of-the-Art Performance: The project achieves state-of-the-art results on various vision-language tasks. It outperforms previous methods in image-text retrieval (with an average recall@1 improvement of +2.7%), image captioning (with a CIDEr improvement of +2.8%), and VQA (with a VQA score improvement of +1.6%).
Generalization and Transferability: BLIP demonstrates strong generalization ability when applied to video-language tasks in a zero-shot manner, showcasing its versatility and flexibility.
Code, Models, and Datasets: The project provides access to the code, pretrained models, and datasets, enabling researchers and developers to explore and utilize the AI Caption Generator.

# Usage
Input Image: Provide an image to the AI Caption Generator.
Caption Generation: The Transformer model processes the image using the Salesforce BLIP architecture and generates descriptive captions for the image.
Caption Display: The generated captions are displayed, providing valuable insights and descriptions of the visual content.
