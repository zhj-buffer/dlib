import face_recognition
jobs_image = face_recognition.load_image_file("chuanpu.jpg");
obama_image = face_recognition.load_image_file("aobama.jpeg");
unknown_image = face_recognition.load_image_file("unknown.jpg");

jobs_encoding = face_recognition.face_encodings(jobs_image)[0]
obama_encoding = face_recognition.face_encodings(obama_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([jobs_encoding, obama_encoding], unknown_encoding )
labels = ['chuanpu', 'obama']

print('results:'+str(results))

for i in range(0, len(results)):
    if results[i] == True:
        print('The person is:'+labels[i])

