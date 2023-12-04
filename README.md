# SE 1 Team Project - UML2Python

Submitted by: Stephanie Salgado, Tobi Oguntuase, and Adrian Perez

The UML2Python script creates a UML diagram by asking the user prompts relating to UML. After creating the UML, the user can generate Python code and it will create a new Python file after.

## Requirements

For **MacOS**:
- Homebrew Install
    - Run command in Terminal and follow prompts:
      
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- Graphviz Install
    - Run command in Terminal:
    `brew install graphviz`
    - Add Graphviz to PATH
    - Run command in Terminal:
    `export PATH="/opt/homebrew/bin:$PATH"`

For **Windows**:
- Latest Python installed
- Graphviz Install:
    - 64-bit: https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/9.0.0/windows_10_cmake_Release_graphviz-install-9.0.0-win64.exe
- Add Graphviz to the system PATH (current or all Users, screenshot below)
![InstallGraphviz](https://hackmd.io/_uploads/rk6XPT5rp.png)

- Click next and Install
- Finish Installation
- Open CMD and install Graphviz to Python
    - Use command: `pip install graphviz`
    ![pipinstall](https://hackmd.io/_uploads/B1q2Pp9Sp.png)
    
## Instructions

1. Open your IDE (e.g., VSCode, IntelliJ)
2. Open folder “UML2Python”
3. Run .py code
4. Create your UML by following prompts
5. Once done, press 8 to generate code
6. Name your file (make sure it ends with .py for Python)




## Video Walkthrough

Here's a walkthrough of implemented user stories:

<img src='https://github.com/adrianp336/BitFitPt1/blob/master/walkthrough.gif' width='' alt='Video Walkthrough' />

<!-- Replace this with whatever GIF tool you used! -->
GIF created with ScreenToGif
<!-- Recommended tools:
[Kap](https://getkap.co/) for macOS
[ScreenToGif](https://www.screentogif.com/) for Windows
[peek](https://github.com/phw/peek) for Linux. -->

