from huggingface_hub import InferenceClient
from PIL import Image
from datetime import datetime
from config import HF_API_KEY


MODELS = [
    "ByteDance/SDXL-Lightning",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stabilityai/sdxl-turbo",
    "runwayml/stable-diffusion-v1-5",
]


client = InferenceClient(api_key=HF_API_KEY)

print(f"Primary model: {MODELS[0]}")
print("Type 'quit' to exit\n")


while True:

   
    prompt = input("Enter prompt: ").strip()

    
    if prompt.lower() in ["quit", "exit", "q"]:
        break

    
    if not prompt:
        continue

    print("Generating image... ⏳")

    image = None

    for model in MODELS:

        try:
            print(f"Using model: {model}")

            image = client.text_to_image(
                prompt=prompt,
                model=model,
                negative_prompt="ugly, blurry, distorted, low quality",
                guidance_scale=7.5,
                width=1024,
                height=1024,
            )
            print("✅ Image generated successfully!")
            break
        except Exception as e:
            print(f"❌ Error with {model}")
            print(e)
            print("Trying next model... ⏭\n")
    if image:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_{timestamp}.png"

        image.save(filename)

        print(f"✅ Saved as: {filename}")

        
        image.show()

        print()

    else:
        print("❌ Failed with all models.\n")

print("Thanks for using the image generator! Goodbye 👋")