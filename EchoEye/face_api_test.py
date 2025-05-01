from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

# Replace with your Face API credentials
FACE_API_KEY = "A8hGyOxzSIxlMQwARZlsYdtkww0XGvhzKtebqralZEzmiwGGJFDyJQQJ99BDACrIdLPXJ3w3AAAKACOG21h8"

FACE_API_ENDPOINT = "https://faceapiee.cognitiveservices.azure.com/"

# Authenticate the client
face_client = FaceClient(FACE_API_ENDPOINT, CognitiveServicesCredentials(FACE_API_KEY))

# URL of an image or local file path (use online image for now)
image_url = "https://coruzant.com/wp-content/uploads/2024/03/63f902d89a33f71c826ce746_6390a10c3644738a41e9b528_Face-Recognition.jpeg"


# Call the API to detect faces
detected_faces = face_client.face.detect_with_url(
    url=image_url,
    return_face_id=True,
    return_face_attributes=['age', 'gender', 'emotion'],
    detection_model='detection_01',
    recognition_model='recognition_04'
    
)

# Print the results
if not detected_faces:
    print("No face detected.")
else:
    for face in detected_faces:
        print(f"Face ID: {face.face_id}")
        print(f"Age: {face.face_attributes.age}")
        print(f"Gender: {face.face_attributes.gender}")
        print(f"Emotion: {face.face_attributes.emotion.as_dict()}")