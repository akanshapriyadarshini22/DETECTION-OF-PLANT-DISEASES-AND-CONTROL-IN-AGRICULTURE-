# Detection of Plant Diseases and Control in Agriculture

A prototype image-processing and machine-learning system for screening plant images, identifying the plant category and disease, estimating a simple spread-risk category, and presenting a budget-conscious control suggestion.

This repository is reconstructed from the project's original project document. The document describes collection of diseased-plant images, filtering/grouping by plant species, Naive Bayes classification, SVM-based grouping/categorization, disease-spread analysis, and control suggestions. The implementation below turns those described ideas into a runnable prototype.

## Workflow

```text
Plant Image
    ↓
Image preprocessing / feature extraction
    ↓
Plant species categorization (SVM)
    ↓
Disease classification (Gaussian Naive Bayes)
    ↓
Spread-risk category
    ↓
Control suggestion
```

## Project Structure

```text
plant-disease-detection-control/
├── data/
│   ├── images/
│   │   └── <species>/<disease>/*.jpg
│   └── README.md
├── models/
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── image_features.py
│   ├── train.py
│   └── predict.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Dataset Format

Add images using:

```text
data/images/
├── Tomato/
│   ├── Healthy/
│   └── Early_Blight/
└── Potato/
    ├── Healthy/
    └── Late_Blight/
```

The folder names become the labels.

## Installation

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Train

After adding images:

```powershell
python src/train.py
```

The trained artifacts are written to `models/`.

## Run the application

```powershell
python app.py
```

Enter an image path, for example:

```text
C:\Users\YourName\Desktop\plant.jpg
```

The application reports:

- Plant species
- Predicted disease
- Detection confidence
- Spread-risk category
- Control suggestion

## Technologies

- Python
- NumPy
- Pandas
- Pillow
- Scikit-learn
- Gaussian Naive Bayes
- Support Vector Machine (SVM)
- Image processing / handcrafted image features

## Important limitation

This repository does **not** claim a specific accuracy because the original project document does not provide a measured test result and no original image dataset was recovered. The included code is a reconstruction/prototype and should be evaluated on a proper labeled plant-disease dataset before reporting performance numbers.

The control suggestions are informational prototype rules, not prescriptions. For actual crop treatment, disease confirmation and advice from a qualified local agricultural expert should be used.

## Future Improvements

- Add a larger labeled crop-disease dataset.
- Replace handcrafted features with a CNN/deep-learning model.
- Add segmentation of infected leaf regions.
- Add richer disease-spread modelling.
- Add a web/mobile interface.
- Expand the control knowledge base using verified agricultural guidance.
