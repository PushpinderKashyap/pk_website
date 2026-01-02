from flask import Flask, render_template, request,jsonify
from visual import generate_binary_search_gif

app = Flask("Local Website") 

@app.route("/")
def home():
    return render_template("start.html")

@app.route("/Blogs/BinarySearch")
def binarySearch():
    return render_template("Blogs/BinarySearch.html")


@app.route("/Blogs/Visual")
def dummyvisual():
    return render_template("search_visual.html")

@app.route("/generate-gif", methods=["POST"])
def generate_gif():
    data = request.get_json()

    numbers = data["numbers"]
    target = int(data["target"])

    arr = list(map(int, numbers.split(",")))
    arr.sort()


    generate_binary_search_gif(arr, target)

    return jsonify({
        "gif_url": "/static/gifs/binary_search_animation.gif"
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
