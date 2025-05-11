# Investigating Weak Non-Covalent Interactions in Secondary Structures

This repository contains Python code for automating the extraction and organization of alpha helices from PDB files, as part of the project "Investigating Weak Non-Covalent Interaction in Secondary Structures"
The script processes directories of PDB files, identifies helix regions, and saves each helix as a separate PDB file for further analysis.

Features

- Recursively scans a given directory for `.pdb` files.
- Extracts helix regions from each PDB file based on SEQRES and HELIX records.
- Saves each helix as an individual PDB file in organized subfolders.
- Handles errors and logs problematic files.

## Requirements

- Python 3.0
- Standard Libraries:`os`
- Third-party Libraries:
  - `pandas`
  - `numpy`

Install dependencies using:
```bash
pip install pandas numpy
```

## Usage

1. Set the PDB folder path:
   Edit the `pdb_folder` variable in `automate.py` to point to your directory containing PDB files.
   ```python
   pdb_folder = # path to the directory containing all the parent pdb structures
   ```

2. **Run the script:**
   ```bash
   python automate.py
   ```

3. Output:  
   - The script creates a `Helices` folder inside your PDB folder.
   - For each PDB file, it creates a subfolder named after the file and saves each extracted helix as a separate `.pdb` file within it.
   - Any files that could not be processed are listed in the `error_files` output.

## Example Directory Structure

```
newpdb/
├── 1abc.pdb
├── 2def.pdb
└── Helices/
    ├── 1abc/
    │   ├── helix_1.pdb
    │   └── helix_2.pdb
    └── 2def/
        ├── helix_1.pdb
        └── helix_2.pdb
```

## Notes

- Ensure your PDB files contain proper SEQRES and HELIX records for accurate extraction.
- The script is designed for Windows-style paths; minor changes may be needed for cross-platform compatibility.

## Author

Shalini Raman
---
