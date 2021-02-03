# UI_for_Gesture_based_Controller

## Introduction ##
This is the UI I have designed for my project IOT Enabled Wearable Gesture-Based Controller. Inspired by the UWP Theme. The UI was designed using QT Designer.

## About ##
The UI was designed for actually as a Companion app for the Gesture Recogniser Device Created by my friends. The device used NodeMCU(ESP32) and MPU6050 (6 axis Accelerometer & Gyroscope). The raw sensor values are mapped to the movement of the cursor on the OS using a Special Algorithm. This process is done in the Nodemcu. The Mapped Values is sent to the  Computer using the MQTT protocol.

The companion app is made using Python. The Library used in python is PyQt5. PyQt5 is the 5th Iteration of the PyQt GUI Library.]. The app uses custom style sheets to make it look it like Windows 10 Application. It also comes with a dark mode which looks aesthetically pleasing and saves battery. Our Companion App has two tabs: Home page and Settings.

## Features ##
### Home Page ###
The Home page is the first page shown once the app is opened. The home page shows the basic stats and condition of the device. It shows the battery percentage and battery health. IT even shows the connection stats: The Connection speed, connection type, and connection id. The app even tells which mode the user is currently in. This page allows quick mode switching: Off, Normal and LabVIEW. The app also allows quickly to open LabVIEW files (*.vi).

### Settings Page ###
The settings page allows the users to customize their experience with the app. It allows the user to toggle on and off the custom text to speech engine used in the app. It also shows the data transmitted by the device. This page also works as debug screen where we could troubleshoot problems related to the device.

### Text to Speech ###
For visually impaired people, I have made the app easy to use by including a custom speech engine. The engine is called as Pyttsx3 This engine allows the user to know what he/she is pointing in the GUI. It also tells which mode the user is currently in. We allow the user to change the voice of the Text-to-Speech engine.


## Working ##

### Normal Mode ###
In this mode, the user can move the mouse cursor using the device. We implement this using a library called Pyautogui which creates a virtual mouse. As the device contains two buttons, we have emulated the left click and right functionality too. We have mapped the movement of the device to the movement of the cursor on the screen.

### Labview Mode ###
The LabVIEW mode is the speciality of this project. It allows the user to control parameters of various Virtual Instruments like (Amplitude, Frequency, etc). The device movement is mapped with sliders in the LabVIEW Front Panel. The applications write the data received from the broker to a text file. This text file is continuously read by the LabVIEW file for any changes. The two-push button on the device is mapped to the buttons on the LabVIEW front panel. This implementation ensures contactless interaction with the machine.
It has immense industrial application possibility and easily can be integrated with exisisting LabView based Control Panels in Industry for contactless interface and interaction, which is useful in hazardous industries and helps prevent spread of surface viruses or diseases through common work surfaces.

## Files and Folder Description ##
- icons folder contain the icons used in the python code
- 'main.py' It is the main python file which connects to all the other python modules.
- 'main.ui' THe .ui file created by the QT designer. The .ui file can be edited in QT Designer (Note: After any changes run 'pyuic5 -o ui_main.py main.ui' in the terminal/CMD)
- 'mqttbridge.py' This python module helps the user to connect to their MQTT Topic with the APP.
- 'requirements.txt' This file contains the required python packages to run the program smoothly.
- 'tes2.vi' It is the sample LabVIEW file created to show the use case of the program.
- 'UI_functions.py' Contains ui functions like updating the UI realtime and usage of buttons and sliders in the APP.
- 'UI_main.py' It is the converted form of 'main.ui'.

## Installation ##
- Open the Terminal/CMD to the cloned repository
- Run 'pip install -r requirements.txt'
- Users can connect to their MQTT topic by changing the topic name in the 'mqttbridge.py' file. Example change 'client.subscribe("Node_Data")' to 'client.subscribe("Ur topic name")'
- Run the main.py
