# Smart Scarecrow Project

## Table of Contents
- [Problem Statement](#problem-statement)
- [Project Overview](#project-overview)
- [Components](#components)
- [Programming](#programming)
- [Data Storage](#data-storage)
- [Event Handling](#event-handling)
- [Installation](#installation)
- [Conclusion](#conclusion)
- [Populating Calibration Fields Through APIs](#populating-calibration-fields-through-apis)

## Problem Statement

In many agricultural and urban settings, pigeons and other birds can become a significant nuisance. They are notorious for causing damage to crops, defecating on buildings and vehicles, and creating unsanitary conditions. Conventional methods for deterring these birds are often ineffective and can be harmful to the environment.

The Universidad Nacional Mayor de San Marcos in Lima, Peru, has recognized this problem, particularly in the context of urban agriculture and landscaping on campus. To address this issue, a team of  students embarked on a mission to create a more efficient, eco-friendly, and high-tech solution.

## Project Overview

The Smart Scarecrow is designed to detect the presence of birds, particularly pigeons, in its vicinity and emit signals to scare them away. The device is built primarly using an ESP32 microcontroller and a HC-SR04 Sonar Sensor.

## Components

The following components are essential for the Smart Scarecrow project:

- **ESP32 with Ethernet or Wireless Network Connection**: The ESP32 microcontroller, equipped with Ethernet or a wireless network connection, will serve as the brain of the scarecrow. It will process data from the motion sensor and trigger scare tactics when needed.

- **HC-SR04 Sonar Sensor**: This sensor will detect the motion of pigeons or other birds that come near the scarecrow.

- **Jumper Wires (At Least 4)**: Jumper wires will be used to establish connections between various components in the project.

- **LED**: An indicator LED will be used to show when an object or bird is detected.

- **Small Resistor (100 Ω – 1 kΩ)**: A small resistor will be used in the circuit, typically in series with the LED, to control the current and brightness of the LED.

- **USB Cable**: A USB cable will be needed for programming and powering the ESP32 microcontroller.

These components will be integral to the functioning of the Smart Scarecrow and its ability to detect and deter birds effectively.


## Programming

The ESP32 microcontroller will be programmed to perform the following tasks:

1. Monitor the ultrasonic motion sensor for any bird movement.
2. Activate scare tactics, which may include sounds, when birds are detected.
3. Log data for analysis and future improvements.

## Data Storage

Data collected by the Smart Scarecrow, such as bird detection events and scarecrow status, will be stored in the cloud using ThingSpeak. ThingSpeak is a cloud platform that allows data collection and analysis, making it possible to track the scarecrow's performance over time.

## Event Handling

The Smart Scarecrow will be equipped to handle various events, such as:

- Bird detection events: When a bird is detected, the scarecrow will trigger a scare tactic.
- Scarecrow status updates: Our ThingSpeak channel will provide real-time feedback on the scarecrow's status.

## Installation

To set up the Smart Scarecrow project, follow these steps:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/los-tamagotchi/smart-scarecrow.git
   
2. Open the Arduino IDE.
3. Load the project code from the repository.
4. Install the required libraries:
   ThingSpeak Communication Library: To enable communication with ThingSpeak for cloud data storage.
  WiFi Library: To establish a connection with your Wi-Fi network.
5. Connect the ESP32 microcontroller to your computer.
6. Configure your Wi-Fi network credentials, ThingSpeak channel ID, and API keys in the project code.
7. Upload the code to the ESP32.
8. Assemble the components, as per the project documentation.
9. Power on the Smart Scarecrow.

The device should now be operational, detecting birds and scaring them away while sending data to your ThingSpeak channel.

## Populating Calibration Fields Through APIs

To configure your Smart Scarecrow and set its calibration parameters, you can use ThingSpeak's APIs. This allows you to remotely adjust settings and optimize the scarecrow's performance. Follow these steps to populate your calibration fields using a web browser:

1. Open your web browser.

2. Access the following URLs by pasting them directly into the browser's address bar. Remember to replace "YOUR_WRITE_API_KEY" with your actual write API key for your ThingSpeak channel.

    a. Set the threshold for detecting an object (400 cm is our chosen starting point):
    ```
    https://api.thingspeak.com/update?api_key=YOUR_WRITE_API_KEY&field2=THRESHOLD
    ```

    b. Set the number of measurements to average:
    ```
    https://api.thingspeak.com/update?api_key=YOUR_WRITE_API_KEY&field3=NUMTOAVERAGE
    ```

    c. Set the control flag so the device checks for new settings periodically:
    ```
    https://api.thingspeak.com/update?api_key=YOUR_WRITE_API_KEY&field4=1
    ```

3. After accessing these URLs, the browser will return the number of entries in the channel. If you've just created the channel, you'll see entries for fields 1, 2, and 3 once you populate the required calibration fields.

By using these API URLs, you can conveniently adjust the scarecrow's settings and fine-tune its parameters to achieve the best results in deterring birds. This flexibility allows you to adapt the Smart Scarecrow to different conditions and challenges.


## Conclusion
The Smart Scarecrow project creates an efficient and environmentally friendly solution for deterring birds from specific areas. By integrating IoT technology, motion sensors, and cloud data storage through ThingSpeak, this project showcases the potential for innovative solutions in pest control and agriculture.

For further details on the project's implementation, code, and documentation, please refer to the project repository. Feel free to contact us for any additional information or inquiries.


**Project Contributors**:
- Dávila Raffo, Alwin Edu (Student ID: 22200081)
- Del Carpio Martinez, Damaris Marian (Student ID: 22200082)
- Monzon Argüelles, Oscar Sebastian (Student ID: 22200094)




**made with <3 by unmsm**
