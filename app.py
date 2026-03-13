from flask import Flask, render_template, request,jsonify,send_file
from visual import generate_binary_search_gif
from PyPDF2 import PdfMerger
import io

app = Flask("Local Website") 

@app.route("/")
def home():
    return render_template("start.html")

@app.route("/BinarySearch")
def binarySearch():
    return render_template("Blogs/BinarySearch.html")

@app.route("/MergeFiles")
def Merge():
    return render_template("MergeFiles.html")



@app.route('/merge', methods=['POST'])
def merge_pdfs():
    files = request.files.getlist('pdfs')
    if len(files) < 2:
        return "Please upload at least 2 PDFs!"

    merger = PdfMerger()
    for f in files:
        merger.append(f)  # Append file-like object directly

    # Create an in-memory bytes buffer
    merged_pdf = io.BytesIO()
    merger.write(merged_pdf)
    merger.close()
    merged_pdf.seek(0)  # Move to the beginning

    # Send merged PDF directly without saving
    return send_file(
        merged_pdf,
        as_attachment=True,
        download_name="merged.pdf",
        mimetype='application/pdf'
    )



@app.route("/generate-gif", methods=["POST"])
def generate_gif():
    try:
        data = request.get_json()

        numbers = data["numbers"]
        target = int(data["target"])

        arr = list(map(int, numbers.split(",")))
        arr.sort()


        generate_binary_search_gif(arr, target)
        return jsonify({
            "success": True,
            "gif_url": "/static/gifs/binary_search_animation.gif"
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "gif_url": ""
        })


def binary_search_iterative(arr,key):
    left=0
    right = len(arr) - 1   
    while (left <= right):
         mid = left + ((right-left)//2)
         if(arr[mid] == key ):
            return mid        # Key found
         elif(arr[mid] > key):
             right =  mid-1   # Search in left half
         else:
             left = mid+1     # Search in right half
    return -1                 # Key not found


def binary_search_recursive(arr, left, right, key):
    if left > right:
        return -1                                    # Key not found

    mid = left + ((right-left)//2)
    if arr[mid] == key:
        return mid                                   # Key found
    elif arr[mid] > key:
        return binary_search_recursive(arr, left, mid-1, key)  # Search in left half
    else:
        return binary_search_recursive(arr, mid+1, right, key) # Search in right half






# --- Routes ---
@app.route("/search-blog", methods=["GET", "POST"])
def search_blog():
    if request.method == "POST":
        array_input = request.form["array"]
        target = int(request.form["target"])
        search_type = request.form["search_type"]

        arr = [int(x.strip()) for x in array_input.split(",")]
        if search_type == "binary":
            arr.sort()  # Binary search requires sorted list

        return render_template("search_visual.html", arr=arr, target=target, search_type=search_type)

    return render_template("search_blog.html")

 
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
