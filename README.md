# iTunes Duplicate Detector

A Python script to help clean up duplicated songs in your iTunes music library export. The script identifies duplicate entries based on the artist and song name, retaining the earliest added version and removing duplicates from the list. The output file can be imported back into iTunes for a streamlined library.

## Features

- Processes **TSV (Tab-Separated Values)** files exported from iTunes.
- Compatible with **Turkish date formats**.
- Detects and removes duplicate songs based on the addition date.
- Exports the cleaned list to a new file (Müzikler.txt → Temizlenmiş_Müzikler.txt).

## Requirements

- Python 3.x
- pandas library

## Installation

1. Clone the repository:
    - ```git clone <https://github.com/mvarr/itunes_duplicate_detecter.git>```
2. Navigate to the project directory:
    - ```cd itunes_duplicate_detecter```
3. Install the required Python package:
    - ```pip install pandas```

## Usage

1. Export your music library from iTunes:

    - Open iTunes and go to File > Library > Export Library.
    - Save the exported file as Müzikler.txt (default encoding is UTF-16).

2. Set the file paths:

    - Edit the file_path variable in duplicate.py to match the location of your exported file.
    - Alternatively, move your exported Müzikler.txt file to the script's directory.

3. Run the script:

    - ```python duplicate.py```

4. The cleaned file will be saved as Temizlenmiş_Müzikler.txt in the same directory.

## Notes

This script assumes the iTunes library is exported with Turkish date formatting. If you use a different locale, modify the date parsing line in the script:

- ```df['Eklenme Tarihi'] = pd.to_datetime(df['Eklenme Tarihi'], format='%d %b %Y', errors='coerce')```
The script only works with UTF-16 encoded files exported from iTunes.

## Contributing

Contributions are welcome! If you'd like to improve this script or add new features, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:

    - ```git checkout -b feature/your-feature-name```

3. Make your changes and commit them:

    - ```git commit -m "Add your commit message here"```

4. Push your changes to your forked repository:

    - ```git push origin feature/your-feature-name```

5. Open a pull request describing your changes.

Feel free to open an issue if you find a bug or have a suggestion for a new feature!

## Feedback

If you encounter any issues or have suggestions, you can:

Create an issue on the [GitHub repository](github.com/mvarr/itunes_duplicate_helper).
Contact me directly via email at mailto:melihvar@hotmail.com
Your feedback would improve the project!
