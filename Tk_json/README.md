# Tkinter JSON User Management

A simple desktop application built with Python's Tkinter library for managing user data in a JSON file. This application provides a graphical user interface for adding, viewing, and searching user records.

## Features

- Add new users with name and age
- Display all users in the system
- Search for specific users by name
- Data persistence using JSON file storage
- Simple and intuitive graphical interface

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- JSON module (built into Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/[your-username]/Tk_json.git
cd Tk_json
```

2. Run the application:
```bash
python tkJson.py
```

## How to Use

1. **Adding a User**:
   - Enter the user's name in the first input field
   - Enter the user's age in the second input field
   - Click the "add" button to save the user

2. **Viewing All Users**:
   - Click the "show" button to display all users in the text area
   - Each user will be shown in the format: `name:age`

3. **Searching for a User**:
   - Enter the user's name in the first input field
   - Click the "search" button
   - If found, the user's information will be displayed
   - If not found, "user not found!!!" message will appear

## Project Structure

- `tkJson.py` - Main application file containing the GUI and logic
- `list.json` - JSON file storing the user data

## Contributing

Feel free to fork this project and submit pull requests with improvements. You can also open issues if you find any bugs or have suggestions for new features.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT). 