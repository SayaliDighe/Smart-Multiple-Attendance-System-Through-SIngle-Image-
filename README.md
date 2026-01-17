# Smart-Multiple-Attendance-System-Through-SIngle-Image-
Smart Multiple Attendance System Through Single Image

Project Description
This project is a smart attendance system that automatically marks attendance of multiple students using face recognition from a single classroom image. It reduces manual work, saves time, and avoids proxy attendance.

Students are registered by capturing multiple face images using a webcam. These images are converted into face encodings and stored. During class, the system captures classroom images, detects and recognizes faces, and marks attendance automatically.

Features
Student registration using webcam
Multiple face image capture for better accuracy
Automatic face encoding using CNN model
Recognition of multiple students in a single image
Automatic attendance marking
Excel attendance report generation
Email report sent to teacher
SMS alerts sent to parents of absentees
User-friendly GUI using Tkinter
Local database using SQLite

Technologies Used
Python
OpenCV
face_recognition (CNN model)
Tkinter
SQLite
Pandas
Pillow
SMTP for email service
Twilio API for SMS service

Project Structure

Smart-Multiple-Attendance-System
code_final.py
student_table.py
encodings.pickle
students.db
dataset
attendance_reports
README.md

How the System Works
First, students are registered by capturing their face images.
Face encodings are generated and stored for recognition.
During class, classroom images are captured.
The system detects and recognizes student faces.
Attendance is marked automatically.
Attendance is saved in an Excel file.
Email report is sent to the teacher.
SMS alerts are sent to parents of absent students.

How to Run the Project

Step 1 Install required libraries
pip install opencv-python face-recognition pandas pillow twilio

Step 2 Run database setup
python student_table.py

Step 3 Run main program
python code_final.py

Future Improvements
Use cloud database for scalability
Convert into web application
Add mobile app integration
Improve accuracy using advanced deep learning
Enable real-time face recognition
