import os
import urllib.request

data_dir = r'C:\Users\Maciej\Desktop\test'
pages = [
    {"name": "jebzdzidy", "url": "https://jbzd.com.pl"},
    {"name": "Python Docs", "url": "https://docs.python.org/3/contents.html"},
    {"name": "Jupyter Notebook", "url": "https://jupyter-notebook.readthedocs.io"}
]

for page in pages:
    try:
        print(f"Processing url: {page["url"]}")
        file_name = f"{page["name"]}.html"
        path = os.path.join(data_dir, file_name)
        urllib.request.urlretrieve(page["url"], path)

    except:
        print("File processing failed.")
        print("Please try again later.")
        print("Quitting...")
        break
else:
    print("File processing has completed successfully!!!")
