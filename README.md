# Random Fact Generator

The Random Fact Generator is a simple Python application that displays interesting facts every time you run the program. It can be run as a command-line application or as a GUI application using Tkinter.

## Features

- Read facts from a text file
- Randomly display a fact from the list
- (Optional) Simple GUI using Tkinter

## Installation

1. Clone this repository or download it as a zip file.

   ```bash
   git clone https://github.com/yourusername/random-fact-generator.git
   ```

2. (Optional) If you want to use the GUI version, ensure that you have Tkinter installed. Tkinter comes pre-installed with most Python installations. If you don't have it, you can install it using the following command:

   ```bash
   pip install tk
   ```

## Usage

### Command-line version

1. Add more facts to the `facts.txt` file if you want. Make sure to add one fact per line.
2. Run the `random_fact_generator.py` script.

   ```bash
   python random_fact_generator.py
   ```

   This will display a random fact from the `facts.txt` file.

### GUI version (Optional)

1. Add more facts to the `facts.txt` file if you want. Make sure to add one fact per line.
2. Run the `random_fact_generator_gui.py` script.

   ```bash
   python random_fact_generator_gui.py
   ```

   This will open a window with a button. Click the button to display a random fact.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to this project, please feel free to submit a pull request or open an issue on GitHub.

1. Fork the repository on GitHub.
2. Clone your fork locally.

   ```bash
   git clone https://github.com/yourusername/random-fact-generator.git
   ```

3. Create a new branch for your feature or bugfix.

   ```bash
   git checkout -b my-feature-branch
   ```

4. Commit your changes and push your branch to GitHub.

   ```bash
   git add .
   git commit -m "Add my feature"
   git push origin my-feature-branch
   ```

5. Open a pull request on GitHub to merge your changes into the main repository.
