from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("./yolov8s_playing_cards.pt")  # load a pretrained model (recommended for training)

# Use the model
# results = model.train(data="coco128.yaml", epochs=3)  # train the model
# results = model.val()  # evaluate model performance on the validation set
results = model("./assets/test.jpg", save=True, project="./", name="detect")  # predict on an image with specified output directory
# success = YOLO("yolov8n.pt").export(format="onnx")  # export a model to ONNX format
print([x for x in results])