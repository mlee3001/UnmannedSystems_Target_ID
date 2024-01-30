import cv2
from depthai import Pipeline, Device, BoardConfig

# Define the Oak-D pipeline
pipeline = Pipeline()

board_config = BoardConfig()
board_config.setUSBLocation(True)
board_config.setCMOSImageResolution(depthai.CameraBoardSocket.RGB, depthai.ImageSize.Resolution1080p)

pipeline.setBoardConfig(board_config)

pipeline.setNeuralNetworkModel(
    location="./models/your_model.blob",  # Replace with the path to your model blob file
    modelType="yolov8n",  # Replace with your model type
    shaves=6,
    cmxGroups=1,
)

# Create a DepthAI device
with Device(pipeline) as device:
    # Get the neural network node
    nn = device.getOutputQueue("nn", 8, False)

    # Start the pipeline
    device.startPipeline()

    while True:
        # Get a frame from the camera
        frame = device.getOutputQueue("preview", 8, False).get().getCvFrame()

        # Run inference on the frame
        inference_data = nn.get().getFirstLayerInt32()

        # Process the inference data as needed
        # ...

        # Display the frame with inference results
        cv2.imshow("Oak-D Inference", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) == ord("q"):
            break

# Close all OpenCV windows
cv2.destroyAllWindows()
