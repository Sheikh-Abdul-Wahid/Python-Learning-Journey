# Installation Errors for Older Python Package Versions in Virtual Environment:

(virtual_environment) PS F:\Python Learning Journey\WEEK 6> pip install pandas==2.1.0

metadata-generation-failed  
ERROR: Could not find C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe

# Solution: To resolve this issue, I followed these steps:

1. Install Microsoft C++ Build Tools from here, selecting C++ CMake tools and Windows SDK.

2. Installed meson and ninja using the following command:
   
```bash
pip install meson ninja 
```

3. Reinstalled pandas without building from the source:

```bash
pip install --only-binary :all: pandas==2.1.0
```
