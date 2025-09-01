# 🚀 SD Params 2 Table

<!-- 
    👋 Welcome! Please replace the placeholder below with your project's logo!
    Example: <p align="center"><img src="path/to/your/logo.png" alt="Your Logo" width="200"></p> 
-->
<p align="center">
<img width="540" height="480" alt="2025-09-01_09-53-50 (Small)" src="https://github.com/user-attachments/assets/38b3c1a7-b409-4cff-bb09-f5bb75c12cea" />
</p>

---

## ✨ Overview

This utility provides a seamless way to transform the semi-structured text output from the Stable Diffusion into a clean, two-column CSV format. It automates the process of extracting headings and their corresponding values, making your data ready for analysis or import into other systems with a simple drag-and-drop.

[![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE) <!-- You might want to update or remove the license if this is purely internal -->

---

## 🌟 Features

*   **⚡ One-Click Execution:** Double-click a batch file to start the conversion process.
*   **📁 Drag-and-Drop Input:** Easily provide your `params.txt` source file by dragging it directly onto the command prompt window.
*   **📊 Clean CSV Output:** Transforms unformatted lines and comma-separated values into a simple two-column `Header | Value` structure.
*   **🖥️ Desktop Output:** Automatically saves the converted `.csv` file to your Desktop.
*   **⏰ Dynamic Filenaming:** Output files are named uniquely with the format `parameter-export-YYYY-MM-DD-timeinseconds.csv`, preventing overwrites and providing a clear timestamp.
*   **⚙️ Configurable Output Path:** The output directory (e.g., Desktop) is easily adjustable within the Python script.

---

## 🛠️ Setup & Installation

Before you can run the sd-params2table, you need to ensure Python is installed and then place the necessary files in a convenient location.

### Prerequisites

*   **Python 3.x:** If you don't have Python installed, please download and install it from the official website: [python.org/downloads/windows/](https://www.python.org/downloads/windows/).
    *   **💡 IMPORTANT:** During installation, make sure to check the box that says **"Add Python.exe to PATH"**. This allows the `.bat` file to find Python.

### Files

1.  **Clone this repository** (or download the `param-convert.py` and `run_converter.bat` files directly).
2.  **Place both files in the *same folder*** on your computer. This could be anywhere convenient, e.g., `C:\Users\YourUser\Scripts\sd-params2table` or a folder directly on your Desktop.

    Your folder structure should look something like this:

    ```
    📦 sd-params2table/
    ├── 🐍 param-convert.py
    └── ⚙️ run_converter.bat
    ```

---

## ➡️ How to Use

Using the converter is designed to be as simple as possible!

1.  **Double-click** the `run_converter.bat` file.
    A command prompt window will open, similar to this:

    ```
    SD Params 2 Table
    Please drag and drop your params.txt file onto this window, then press Enter.

    Source File: _
    ```

2.  **Drag and drop** your Params source `.txt` file onto the command prompt window.
    The full path to your file will appear next to "Source File:".

    ```
    SD Params 2 Table
    Please drag and drop your params.txt file onto this window, then press Enter.

    Source File: C:\Users\YourUser\Documents\Params_Export_001.txt_
    ```

3.  **Press Enter**.
    The script will process your file. You'll see success messages, and the command prompt will pause until you press any key to close it.

    ```
    ...
    Processing file...

    Success! Conversion complete.
    Output saved to: C:\Users\YourUser\Desktop\parameter-export-2023-10-27-1698432615.csv

    ---
    Process finished.
    Press any key to continue . . .
    ```

---

## 📄 Output

### Output Destination

All converted `.csv` files will be saved directly to your **Desktop**.

### Filename Format

The output file will follow this pattern: `parameter-export-YYYY-MM-DD-timeinseconds.csv`.
Example: `parameter-export-2023-10-27-1698432615.csv`

The `timeinseconds` portion ensures that each file is uniquely named, preventing accidental overwrites.

### Output Structure

The converted data will be presented in a clean two-column format, suitable for opening directly in Excel or any spreadsheet program.

**Example `output.csv` content:**

```
