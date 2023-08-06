# oneat

oneat = Open Network for Event as Action Topologies

[![PyPI version](https://img.shields.io/pypi/v/oneat.svg)](https://pypi.org/project/oneat)


This project provides static and action classification networks for LSTM/CNN based networks to recoganize cell events such as division, apoptosis, cell rearrangement for various imaging modalities.



## Installation & Usage

## Installation
This package can be installed by 


`pip install --user oneat`

If you are building this from the source, clone the repository and install via

```bash
git clone https://github.com/Kapoorlabs-caped/caped-ai-oneat/

cd caped-ai-oneat

pip install --user -e .

# or, to install in editable mode AND grab all of the developer tools
# (this is required if you want to contribute code back to NapaTrackMater)
pip install --user -r requirements.txt
```


### Pipenv install

Pipenv allows you to install dependencies in a virtual environment.

```bash
# install pipenv if you don't already have it installed
pip install --user pipenv

# clone the repository and sync the dependencies
git clone https://github.com/Kapoorlabs-caped/caped-ai-oneat/
cd caped-ai-oneat
pipenv sync

# make the current package available
pipenv run python setup.py develop

# you can run the example notebooks by starting the jupyter notebook inside the virtual env
pipenv run jupyter notebook
```

## Examples

oneat comes with different options to combine segmentation with classification or to just use classification independently of any segmentation during the model prediction step. We summarize this in the table below:

| Example Dataset   | DataSet | Trained Model | Notebook Code |
| --- |--- | --- |--- |
| <img src="https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/blob/main/images/Xenopus_example.jpg"  title="Xenopus nuclei in 3D/4D" width="200">| [Example timelapse](https://zenodo.org/record/6484966/files/C1-for_oneat_prediction.tif)| [Oneat model](https://zenodo.org/record/6484966/files/Cellsplitdetectorxenopus.h5) |  [Napari notebook](https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/blob/main/Demo/Mitosis_xenopus_withoutsegmentation.ipynb)|
|   |   |  | | 
| <img src="https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/blob/main/images/ch_2_crop.png"  title="Brightfield" width="200">| [Example timelapse](https://zenodo.org/record/6371249/files/20210904_TL2%20-%20R05-C03-F0_ch_2.tif)| [Oneat model](https://zenodo.org/record/6481021) | [Napari notebook](https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/blob/main/Demo/Mitosis_hela_cells_brightfield.ipynb)|
|   |   |  | | 
| <img src="https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/blob/main/images/ch_1_crop.png"  title="High DPC" width="200">| [Example timelapse](https://zenodo.org/record/6480142/files/20210904_TL2%20-%20R05-C03-F0_ch_2.tif)| [Oneat model](https://zenodo.org/record/6483483/files/Cellsplitdetectorhdpc.h5) | [Napari notebook](https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/blob/main/Demo/Mitosis_hela_cells_high_digitalphasecontrast.ipynb)|
## Troubleshooting & Support

- The [image.sc forum](https://forum.image.sc/tag/oneat) is the best place to start getting help and support. Make sure to use the tag `oneat`, since we are monitoring all questions with this tag.
- If you have technical questions or found a bug, feel free to [open an issue](https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/issues).

