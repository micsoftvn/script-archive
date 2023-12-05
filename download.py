import os
import requests

url_base = 'https://ia804609.us.archive.org/BookReader/BookReaderImages.php?zip=/2/items/sintesiscursoint0000belc/sintesiscursoint0000belc_jp2.zip&file=sintesiscursoint0000belc_jp2/sintesiscursoint0000belc_00{}.jp2&id=sintesiscursoint0000belc&scale=2&rotate=0'

cookies = {
    'donation-identifier': '3613a062301611935f90186b293920b8',
    'abtest-identifier': 'b8fd01bf680280f0a177c404100fbf35',
    'donation': 'x',
    'test-cookie': '1',
    'PHPSESSID': '1ons4pbeg545543534evkevg0fe76793a2m',
    'logged-in-sig': '1733296643%201701760643%20nUh%2FH16%2F4milR2ugm1sL9vGFnSDZuS4m2e0BC345435345345PN5OUagiyNmuEF1LnkG9EpBRCyDEbQ479lEupUJR9IRIRjPlRt0DCIR2lKftUPP%2FXI%2BlFMdfWj0txGyHHcKcPzgxVX6X8tWkBIq94IL%2FSezUeKPU1D1MTnGg2qfPS7gmxprO2M%3D',
    'logged-in-user': 'vuanhquang%40gmail.com',
    'br-loan-sintesiscursoint0000belc': '1',
    'br-loan-': '1',
    'loan-': '1701762850-82add89a03454534b751886a6f532637a0bc31d',
    'ol-auth-url': '%2F%2Farchive.org%2Fservices%2Fborrow%2FXXX%3Fmode%3Dauth',
    'loan-sintesiscursoint0000belc': '1701767493-2e0f6d6b4b11659d884e18f9a2b7ff63',
}

headers = {
    'authority': 'ia804609.us.archive.org',
    'accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://archive.org/details/sintesiscursoint0000belc/page/7/mode/1up',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
}

# Create a folder to save the images
output_folder = "downloaded_images"
os.makedirs(output_folder, exist_ok=True)

# Loop through each leaf page
for leaf_num in range(10, 15):
    # Construct the URL for the current leaf page
    url = url_base.format(leaf_num)

    # Send a request to the page
    response = requests.get(url, headers=headers, cookies=cookies)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the image binary content to a file
        with open(os.path.join(output_folder, f'page_{leaf_num}.jpg'), 'wb') as f:
            f.write(response.content)
        
        print(f"Page {leaf_num} downloaded successfully.")
    else:
        print(f"Failed to retrieve page {leaf_num}. Status code: {response.status_code}")

print("Download completed.")
