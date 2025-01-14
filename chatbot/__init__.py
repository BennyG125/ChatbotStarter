import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']


def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0,
                                 max_tokens=450):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

delimiter = "####"

system_message = f"""You will provide answers to customer service queries.
The customer service quieries and sequential reasoning steps will be delimited with the characters \
{delimiter}. 

{delimiter} Step 1:
First check whether the customer is asking about a product contained in the list below. 
Given that the product is included in the overview, then please output a python list with /
categories  For example like {{'category': 'Smartphones'}}. The categories to be included are /
Smartphones, Computers and accesories, Televisions and Home Theater Systems and /
Gaming Consoles and Accessories. 

Smartphones:
Apple iPhone 15 Pro
Samsung Galaxy S23 Ultra
Google Pixel 8
OnePlus 12
Xiaomi Mi 13 Pro

Computers and accesories:
MacBook Pro 16-inch
Dell XPS 13
Lenovo ThinkPad X1 Carbon
HP Spectre x360
ASUS ROG Zephyrus G15
Accessories:
External Hard Drives
Wireless Keyboards
Ergonomic Mice
USB-C Hubs
Laptop Cooling Pads

Televisions and Home Theater Systems:
Televisions:
LG OLED C3 Series
Samsung QLED QN90C
Sony Bravia XR A80L
TCL 6-Series Roku TV
Hisense U8H Mini-LED
Bose Lifestyle 650
Sony HT-A7000 Soundbar
Sonos Beam (Gen 2)
Samsung HW-Q990C
Klipsch Cinema 800

Gaming Consoles and Accessories:
Consoles:
PlayStation 5
Xbox Series X
Nintendo Switch OLED Model
Steam Deck
Meta Quest 3 (VR Headset)
Gaming Headsets
RGB Gaming Keyboards
Gaming Controllers
VR Accessories
Gaming Chairs

{delimiter} Step 2:
When you have an overview of the category the customer inqury pertains to, then you /
can move on to the next step. In the next step, can you figure out which /
product the customer is asking about. Moreover, check whether the customer are making /
any assumptions about the product. The product has to be in the list below. 

#product information
products = 
{{
    "Apple iPhone 15 Pro": {{
        "name": "Apple iPhone 15 Pro",
        "Processor": "A17 Pro Bionic",
        "Display": "6.1-inch Super Retina XDR",
        "Storage": "128GB, 256GB, 512GB, 1TB",
        "Camera": "48 MP main, 12 MP ultra-wide",
        "Battery Life": "23 hours video playback"
    }},
    "Samsung Galaxy S23 Ultra": {{
        "name": "Samsung Galaxy S23 Ultra",
        "Processor": "Snapdragon 8 Gen 2",
        "Display": "6.8-inch QHD+ AMOLED",
        "Storage": "256GB, 512GB, 1TB",
        "Camera": "200 MP main, 12 MP ultra-wide, 10 MP telephoto",
        "Battery Life": "5000mAh"
    }},
    "Google Pixel 8": {{
        "name": "Google Pixel 8",
        "Processor": "Google Tensor G3",
        "Display": "6.2-inch AMOLED",
        "Storage": "128GB, 256GB",
        "Camera": "50 MP main, 12 MP ultra-wide",
        "Battery Life": "4355mAh"
    }},
    "OnePlus 12": {{
        "name": "OnePlus 12",
        "Processor": "Snapdragon 8 Gen 3",
        "Display": "6.7-inch AMOLED",
        "Storage": "256GB, 512GB",
        "Camera": "50 MP main, 48 MP ultra-wide, 64 MP telephoto",
        "Battery Life": "5400mAh"
    }},
    "Xiaomi Mi 13 Pro": {{
        "name": "Xiaomi Mi 13 Pro",
        "Processor": "Snapdragon 8 Gen 2",
        "Display": "6.73-inch AMOLED",
        "Storage": "128GB, 256GB, 512GB",
        "Camera": "50 MP main, 50 MP ultra-wide, 50 MP telephoto",
        "Battery Life": "4820mAh"
    }},
    "MacBook Pro 16-inch": {{
        "name": "MacBook Pro 16-inch",
        "Processor": "Apple M2 Max",
        "Display": "16.2-inch Liquid Retina XDR",
        "Storage": "512GB, 1TB, 2TB, 4TB",
        "Battery Life": "22 hours video playback",
        "Weight": "2.15kg"
    }},
    "Dell XPS 13": {{
        "name": "Dell XPS 13",
        "Processor": "Intel Core i7 12th Gen",
        "Display": "13.4-inch FHD+ InfinityEdge",
        "Storage": "512GB, 1TB",
        "Battery Life": "12 hours",
        "Weight": "1.27kg"
    }},
    "Lenovo ThinkPad X1 Carbon": {{
        "name": "Lenovo ThinkPad X1 Carbon",
        "Processor": "Intel Core i7 12th Gen",
        "Display": "14-inch WUXGA",
        "Storage": "256GB, 512GB, 1TB",
        "Battery Life": "13 hours",
        "Weight": "1.12kg"
    }},
    "HP Spectre x360": {{
        "name": "HP Spectre x360",
        "Processor": "Intel Core i7 12th Gen",
        "Display": "13.5-inch OLED",
        "Storage": "512GB, 1TB",
        "Battery Life": "15 hours",
        "Weight": "1.34kg"
    }},
    "ASUS ROG Zephyrus G15": {{
        "name": "ASUS ROG Zephyrus G15",
        "Processor": "AMD Ryzen 9 6900HS",
        "Display": "15.6-inch QHD 165Hz",
        "Storage": "1TB",
        "Battery Life": "10 hours",
        "Weight": "1.9kg"
    }},
    "External Hard Drives": {{
        "name": "External Hard Drives",
        "Storage Capacity": "1TB, 2TB, 4TB",
        "Connection": "USB 3.0, USB-C",
        "Brands": "Seagate, Western Digital, Samsung"
    }},
    "Wireless Keyboards": {{
        "name": "Wireless Keyboards",
        "Connection": "Bluetooth, USB Receiver",
        "Features": "Backlit, Ergonomic, Rechargeable",
        "Brands": "Logitech, Microsoft, Razer"
    }},
    "Ergonomic Mice": {{
        "name": "Ergonomic Mice",
        "Connection": "Bluetooth, USB Receiver",
        "Features": "Programmable Buttons, Vertical Design",
        "Brands": "Logitech, Microsoft, Anker"
    }},
    "USB-C Hubs": {{
        "name": "USB-C Hubs",
        "Ports": "HDMI, USB 3.0, SD Card Slot",
        "Compatibility": "Mac, Windows, Chromebook",
        "Brands": "Anker, Satechi, Belkin"
    }},
    "Laptop Cooling Pads": {{
        "name": "Laptop Cooling Pads",
        "Fans": "1 to 5 adjustable fans",
        "Compatibility": "14-inch to 17-inch laptops",
        "Brands": "Cooler Master, Thermaltake, Havit"
    }}
    "LG OLED C3 Series": {{
        "name": "LG OLED C3 Series",
        "Display Technology": "OLED",
        "Screen Size": "55-inch, 65-inch, 77-inch",
        "Resolution": "4K UHD",
        "HDR Support": "Dolby Vision, HDR10",
        "Smart Features": "WebOS, voice control, streaming apps"
    }},
    "Samsung QLED QN90C": {{
        "name": "Samsung QLED QN90C",
        "Display Technology": "QLED",
        "Screen Size": "50-inch, 65-inch, 75-inch",
        "Resolution": "4K UHD",
        "HDR Support": "HDR10+, Quantum HDR",
        "Smart Features": "Tizen OS, voice control, streaming apps"
    }},
    "Sony Bravia XR A80L": {{
        "name": "Sony Bravia XR A80L",
        "Display Technology": "OLED",
        "Screen Size": "55-inch, 65-inch, 75-inch",
        "Resolution": "4K UHD",
        "HDR Support": "Dolby Vision, HDR10",
        "Smart Features": "Google TV, voice control, streaming apps"
    }},
    "TCL 6-Series Roku TV": {{
        "name": "TCL 6-Series Roku TV",
        "Display Technology": "Mini-LED",
        "Screen Size": "55-inch, 65-inch, 75-inch",
        "Resolution": "4K UHD",
        "HDR Support": "Dolby Vision, HDR10",
        "Smart Features": "Roku OS, voice control, streaming apps"
    }},
    "Hisense U8H Mini-LED": {{
        "name": "Hisense U8H Mini-LED",
        "Display Technology": "Mini-LED",
        "Screen Size": "55-inch, 65-inch",
        "Resolution": "4K UHD",
        "HDR Support": "Dolby Vision, HDR10",
        "Smart Features": "Google TV, voice control, streaming apps"
    }},
    "Bose Lifestyle 650": {{
        "name": "Bose Lifestyle 650",
        "Audio Type": "Home Theater System",
        "Components": "Soundbar, subwoofer, surround speakers",
        "Connectivity": "Bluetooth, Wi-Fi, HDMI ARC",
        "Features": "4K pass-through, ADAPTiQ audio calibration"
    }},
    "Sony HT-A7000 Soundbar": {{
        "name": "Sony HT-A7000 Soundbar",
        "Audio Type": "Soundbar",
        "Channels": "7.1.2",
        "Connectivity": "Bluetooth, Wi-Fi, HDMI eARC",
        "Features": "Dolby Atmos, DTS:X, 360 Spatial Sound"
    }},
    "Sonos Beam (Gen 2)": {{
        "name": "Sonos Beam (Gen 2)",
        "Audio Type": "Soundbar",
        "Channels": "5.0",
        "Connectivity": "Wi-Fi, Ethernet, HDMI eARC",
        "Features": "Dolby Atmos, Alexa/Google Assistant integration"
    }},
    "Samsung HW-Q990C": {{
        "name": "Samsung HW-Q990C",
        "Audio Type": "Soundbar",
        "Channels": "11.1.4",
        "Connectivity": "Bluetooth, Wi-Fi, HDMI eARC",
        "Features": "Dolby Atmos, Q-Symphony, SpaceFit Sound Pro"
    }},
    "Klipsch Cinema 800": {{
        "name": "Klipsch Cinema 800",
        "Audio Type": "Soundbar",
        "Channels": "3.1",
        "Connectivity": "Bluetooth, HDMI ARC",
        "Features": "Dolby Atmos, wireless subwoofer"
    }},
    "PlayStation 5": {{
        "name": "PlayStation 5",
        "Processor": "Custom AMD Zen 2",
        "Graphics": "Custom RDNA 2 GPU",
        "Storage": "825GB SSD",
        "Resolution": "4K UHD",
        "Features": "Ray tracing, DualSense controller"
    }},
    "Xbox Series X": {{
        "name": "Xbox Series X",
        "Processor": "Custom AMD Zen 2",
        "Graphics": "Custom RDNA 2 GPU",
        "Storage": "1TB SSD",
        "Resolution": "4K UHD, 8K capable",
        "Features": "Quick Resume, Xbox Game Pass"
    }},
    "Nintendo Switch OLED Model": {{
        "name": "Nintendo Switch OLED Model",
        "Processor": "NVIDIA Custom Tegra",
        "Display": "7-inch OLED",
        "Storage": "64GB",
        "Features": "Handheld and docked mode, Joy-Con controllers"
    }},
    "Steam Deck": {{
        "name": "Steam Deck",
        "Processor": "Custom AMD APU",
        "Graphics": "RDNA 2 GPU",
        "Storage": "64GB, 256GB, 512GB SSD",
        "Display": "7-inch touchscreen",
        "Features": "Portable PC gaming, SteamOS"
    }},
    "Meta Quest 3 (VR Headset)": {{
        "name": "Meta Quest 3 (VR Headset)",
        "Processor": "Qualcomm Snapdragon XR2 Gen 2",
        "Display": "High-resolution LCD",
        "Storage": "128GB, 256GB",
        "Features": "Standalone VR, hand tracking"
    }},
    "Gaming Headsets": {{
        "name": "Gaming Headsets",
        "Features": "Surround sound, noise cancellation, wireless options",
        "Connectivity": "Bluetooth, 3.5mm jack, USB",
        "Brands": "HyperX, SteelSeries, Razer"
    }},
    "RGB Gaming Keyboards": {{
        "name": "RGB Gaming Keyboards",
        "Features": "Mechanical keys, customizable RGB lighting",
        "Connection": "Wired, wireless",
        "Brands": "Corsair, Razer, Logitech"
    }},
    "Gaming Controllers": {{
        "name": "Gaming Controllers",
        "Compatibility": "PC, consoles",
        "Connection": "Wired, wireless",
        "Features": "Customizable buttons, haptic feedback"
    }},
    "VR Accessories": {{
        "name": "VR Accessories",
        "Components": "Controller straps, lens protectors, charging docks",
        "Compatibility": "Meta Quest, HTC Vive, PlayStation VR"
    }},
    "Gaming Chairs": {{
        "name": "Gaming Chairs",
        "Features": "Adjustable height, lumbar support, ergonomic design",
        "Material": "PU leather, fabric",
        "Brands": "Secretlab, DXRacer, Herman Miller"
    }}
}}

{delimiter} Step 3:

Once you now have an overview of both category and associated product information, can /
check whether the customer has made any assumptions about the product or category.


{delimiter} Step 4: 

First politely correct any mistaken assumptions the customer has made /
about the specification about the product if applicable. Only reference the/
any product mentioned in the list of categories and dictionary of products.
If the product or category mentioned is not among out selection, then please/
tell the customer politely it is not among our selection. 
Answer the customer in a friendly and polite manner.  

Use the following format:
Step 1:{delimiter} <step 1 reasoning> {delimiter}
Step 2:{delimiter} <step 2 reasoning> {delimiter}
Step 3:{delimiter} <step 3 reasoning> {delimiter}
Step 4:{delimiter} Response to user:{delimiter} 

"""

user_message = input("Please enter your query: ")

messages = [
    {'role': 'system', 'content': system_message}, 
    {'role': 'user', 'content': f"""{delimiter}{user_message}{delimiter}"""}

]

response = get_completion_from_messages(messages)

try: 
    final_response = response.split(delimiter)[-1].strip()
except Exception as e:
    final_response = "We dont have that product. We apologize for the inconvience"

print(final_response)