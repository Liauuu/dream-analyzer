import os
import requests

def scrape_gutenberg_txt(url, output_path):
   
    response = requests.get(url)
    response.raise_for_status()
    text = response.text

 
    start_marker = "*** START OF"
    end_marker = "*** END OF"

    start_idx = text.find(start_marker)
    end_idx = text.find(end_marker)

    if start_idx != -1 and end_idx != -1:
        clean_text = text[start_idx:end_idx]
    else:
        print(f"[!] Markers not found in {url}, saving full text instead.")
        clean_text = text  

 
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(clean_text)

    print(f"[+] Saved: {output_path}")


if __name__ == "__main__":
  
    os.makedirs("data", exist_ok=True)

   
    urls = {
        # Freud – The Interpretation of Dreams (Brill translation, 1913)
        "freud_interpretation_of_dreams.txt":
            "https://www.gutenberg.org/files/66048/66048-0.txt",

        # Freud – Dream Psychology: Psychoanalysis for Beginners
        "freud_dream_psychology_for_beginners.txt":
            "https://www.gutenberg.org/files/15489/15489-0.txt",

        # Gustavus Hindman Miller – Ten Thousand Dreams Interpreted
        "miller_ten_thousand_dreams_interpreted.txt":
            "https://www.gutenberg.org/cache/epub/926/pg926.txt",

        # Henri Bergson – Dreams
        "bergson_dreams.txt":
            "https://www.gutenberg.org/files/20842/20842-0.txt",

        # Yacki Raizizun – The Secret of Dreams
        "raizizun_secret_of_dreams.txt":
            "https://www.gutenberg.org/cache/epub/13137/pg13137.txt",

        # Anonymous – Guide to Fortune-Telling by Dreams
        "anonymous_guide_to_fortune_telling_by_dreams.txt":
            "https://www.gutenberg.org/cache/epub/65367/pg65367.txt",
    }

   
    for filename, link in urls.items():
        output_file = os.path.join("data", filename)
        try:
            scrape_gutenberg_txt(link, output_file)
        except Exception as e:
            print(f"[!] Failed to download {link}: {e}")
