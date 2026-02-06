
#Security System Initializer

A lightweight Python utility designed for SOC (Security Operations Center) environments to initialize monitoring parameters and perform automated network segment validation.

##📌 Project Overview

This tool demonstrates the practical application of core Python concepts in a cybersecurity context. It allows a security analyst to:

Configure system parameters via an interactive Command Line Interface (CLI).

Calculate security thresholds dynamically based on custom risk multipliers.

Validate IP addresses and automatically categorize them into specific network segments (Local, Corporate, or External).

Handle privilege logic based on analyst roles (e.g., administrative access for "admin").

##🚀 Key Features

Data Validation: Implements robust error handling (try-except) to prevent system crashes during numerical input or unexpected stream interruptions.

Network Intelligence: Uses prefix-based logic (.startswith) to instantly identify asset locations within the infrastructure.

Dynamic Risk Assessment: Applies mathematical formulas to determine threat blocking thresholds based on login attempts and risk factors.

Clean Code Standards: Follows PEP 8 naming conventions and utilizes the ```python if __name__ == "__main__":``` entry point for modularity.

##🛠 Technical Stack

Language: Python 3.12+

Concepts Demonstrated:

Type Casting: Efficiently converting user input into int and float for calculations.

String Manipulation: Data cleaning using .strip(), .lower(), and pattern matching.

Conditional Logic: Advanced use of ```python if/elif/else``` blocks and boolean flags.

Exception Handling: Managing ValueError and EOFError to ensure script stability in various environments.

##📖 How to Use

Ensure you have Python 3.12 or higher installed.

Clone this repository or download the security_setup_tool.py file.

Run the script via your terminal:

```python python security_setup_tool.py```


Follow the on-screen prompts to enter analyst details and network data.

Created as part of a SOC Automation & Security Engineering training path.

