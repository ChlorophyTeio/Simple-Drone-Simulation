# Quadcopter Simulation

This program simulates the motion of a quadcopter drone and provides a graphical user interface (GUI) to visualize the drone's state, including hovering, forward flight, backward flight, left flight, right flight, ascending, descending, clockwise rotation, and anticlockwise rotation. The program is implemented using Python and the Tkinter library for the GUI.

## Prerequisites
- Python 3.x

## Getting Started
1. Clone this repository or download the source code files.
2. Install the required dependencies using the following command:
```
pip install tkinter
```
3. Run the program using the following command:
```
python main.py
```
4. The GUI window will appear, showing the rotor speeds and thrusts for each of the four rotors of the quadcopter.

## Usage
The GUI provides the following buttons to control the drone's motion:
- **Hover**: Sets all rotor speeds to 4000 RPM and thrusts to 10N.
- **Forward**: Sets the rotor speeds and thrusts for forward flight.
- **Backward**: Sets the rotor speeds and thrusts for backward flight.
- **Left**: Sets the rotor speeds and thrusts for left flight.
- **Right**: Sets the rotor speeds and thrusts for right flight.
- **Up**: Sets the rotor speeds and thrusts for ascending.
- **Down**: Sets the rotor speeds and thrusts for descending.
- **Clockwise**: Sets the rotor speeds and thrusts for clockwise rotation.
- **Anti-clockwise**: Sets the rotor speeds and thrusts for anticlockwise rotation.

The GUI will update in real-time to display the rotor speeds and thrusts for each motion state.

## Notes
- This simulation does not consider any external forces such as air resistance or drag.
- The rotor speeds and thrusts are simplified and may not reflect real-world values. Adjustments may be required for accurate simulation.

Please note that this is a basic simulation and does not account for complex physics models or precise numerical calculations. In practical applications, more advanced algorithms and models would be needed to accurately simulate the motion of a quadcopter drone.

Feel free to customize the program according to your specific requirements and further enhance it with additional features or functionalities.

If you have any questions or issues, please feel free to contact the author.

Happy flying with your quadcopter drone simulation!