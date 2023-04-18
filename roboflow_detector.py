import sys
print(sys.version)
from roboflow import Roboflow

rf = Roboflow(api_key="bF5GbCNfdQZlxYWcK2Yy")
project = rf.workspace().project("leaf_disease-puowt")
model = project.version(1).model


def image_details():

    resized_img_path = r"C:\Users\NITRO\Desktop\disease\resized_image"

    # file open in read mode
    file = open(r"C:\Users\NITRO\Desktop\disease\file_path.txt", 'r')
    # Python code to illustrate with() along with write()
    with file as f:
        count = 0
        s = f.readlines()
        for i in s:
            src = resized_img_path + (str(f'\\{i}').rstrip("\n"))
            img = (model.predict(src, confidence=50, overlap=50).json())

            print(img["predictions"])

            for item in img["predictions"]:
                confidence = round(item.get("confidence"), 3)
                classification = item.get("class")
                print(classification, f"{confidence*100}%")

            print(count)
            # visualize your prediction
            #model.predict(r"C:\Users\NITRO\Desktop\disease\resized_image\frame_41.jpg", confidence=70, overlap=50).save(r"C:\Users\NITRO\Desktop\disease\predicted_images"+(str(f'\\{i}').rstrip("\n")))

            model.predict(r"C:\Users\NITRO\Desktop\disease\resized_image.jpg", confidence=70, overlap=50).save(r"C:\Users\NITRO\Desktop\disease\predicted_images"+(str(f'\\{i}').rstrip("\n")))
            print("Saved Successfully")

            # infer on an image hosted elsewhere
            # print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
        count += 1


if __name__ == "__main__":
    image_details()



