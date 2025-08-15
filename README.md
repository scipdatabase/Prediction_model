```markdown
# Combined stress

This repository contains a model that predicts the impact of combined stress in plants.

## Getting Started

To use this model, you'll need to follow these steps:

### Prerequisites

Make sure you have the following libraries installed:

```sh
pip install pandas numpy keras scikit-learn
```

### Installation
Create an environment locally
##CREATE CONDA ENVIORNMENT###

```bash
conda create --name model_env python=3.12.4 joblib=1.4.2 numpy=1.26.4 pandas=2.2.2
```

##ACTIVATE ENVIORNMET##
```bash
conda activate model_env
```
##INSTALL PACKAGES##
```bash
pip install tensorflow==2.17.0 keras==3.4.1
pip install scikit-learn==1.4.2
```
##EDIT INPUT FILES##

#Open model_prediction.py in a text editor and replace file names as mentioned in the script 

Clone the repository:
```bash
git clone https://github.com/<your_repo>/your-model.git
cd your-model
```
or To download the code directly from the repository, you can follow these steps:

1. Look for the green "Code" button on the right side of the page.
2. Click on the "Code" button.
3. In the dropdown that appears, select "Download ZIP".
4. Save the ZIP file to your computer and extract the contents.

This will download the entire repository as a ZIP file; the folder can then be unzipped to extract and run the code.
### Examples
Your data looks like this 
| TREATMENT |Temprature | Drought | Plant |
|-----------|-----------|---------|-------|
| Control   | 28.00     | None    | Rice  |
| Drought   | 28.00     | Mild    | Rice  |
| D+H       | 36.00     | Mild    | Rice |
| Heat      | 36.00     | None    | Rice  |

In the table above, Control, Drought, D+H, and Heat represent the various treatments, where Control represents no stress, ‘Drought’ and ‘Heat’ refer to the individual stresses, and D+H refers to the combined stress. The column “Temperature” refers to the temperature the plants were exposed to under the respective treatments. The column 'Drought' specifies the intensity of drought stress applied. The perception and impact of drought stress can vary depending on the plant species, as different plants respond uniquely to water scarcity. The column 'Plant' denotes the common name of the plant species studied.


Convert this table to the format given in example.csv

<div style="overflow-x:auto;">
  <table style="width:100%;">
    <thead>
      <tr>
        <th>Simultaneous</th>
        <th>Sequential</th>
        <th>Average temperature</th>
        <th>Salt</th>
        <th>Drought</th>
        <th>Boron</th>
        <th>Cd</th>
        <th>UV</th>
        <th>Ozone</th>
        <th>Waterlogging</th>
        <th>Bacteria</th>
        <th>Fungus</th>
        <th>Oomycete</th>
        <th>Virus</th>
        <th>Nematode</th>
        <th>Insect</th>
        <th>Mn</th>
        <th>Pb</th>
        <th>Zinc</th>
        <th>Ni</th>
        <th>Weed</th>
        <th>Light intensity</th>
        <th>Shade</th>
        <th>Lead</th>
        <th>Family_Aizoaceae</th>
        <th>Family_Amaranthaceae</th>
        <th>Family_Araliaceae</th>
        <th>Family_Asteraceae</th>
        <th>Family_Brassicaceae</th>
        <th>Family_Caricaceae</th>
        <th>Family_Caryophyllaceae</th>
        <th>Family_Cucurbitaceae</th>
        <th>Family_Euphorbiaceae</th>
        <th>Family_Fabaceae</th>
        <th>Family_Lamiaceae</th>
        <th>Family_Linaceae</th>
        <th>Family_Malvaceae</th>
        <th>Family_Piperaceae</th>
        <th>Family_Poaceae</th>
        <th>Family_Rosaceae</th>
        <th>Family_Solanaceae</th>
        <th>Family_Theaceae</th>
        <th>Family_Vitaceae</th>
        <th>Type_Abiotic-biotic</th>
        <th>Type_Biotic-biotic</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>28</td>
        <td>0</td>
        <td>0</td>
        <td>30</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
      </tr>
      <tr>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>28</td>
        <td>0</td>
        <td>0</td>
        <td>30</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
      </tr>
      <tr>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>36</td>
        <td>0</td>
        <td>0</td>
        <td>30</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
      </tr>
      <tr>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>36</td>
        <td>0</td>
        <td>0</td>
        <td>30</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
      </tr>
    </tbody>
  </table>
</div>




### Default values for each Parameter

| Parameter            | Default |
|----------------------|---------|
| Simultaneous         | 0       |
| Sequential           | 0       |
| Average temperature  | 0       |
| Salt                 | 0       |
| Drought              | 0       |
| Boron                | 30      |
| Cd                   | 0       |
| UV                   | 1       |
| Ozone                | 0       |
| Waterlogging         | 0       |
| Bacteria             | 0       |
| Fungus               | 0       |
| Oomycete             | 0       |
| Virus                | 0       |
| Nematode             | 0       |
| Insect               | 0       |
| Mn                   | 0       |
| Pb                   | 0       |
| Zinc                 | 0       |
| Ni                   | 0       |
| Weed                 | 0       |
| Light intensity      | 0       |
| Shade                | 0       |
| Lead                 | 0       |
| Family_Aizoaceae     | 0       |
| Family_Amaranthaceae | 0       |
| Family_Araliaceae    | 0       |
| Family_Asteraceae    | 0       |
| Family_Brassicaceae  | 0       |
| Family_Caricaceae    | 0       |
| Family_Caryophyllaceae | 0     |
| Family_Cucurbitaceae | 0       |
| Family_Euphorbiaceae | 0       |
| Family_Fabaceae      | 0       |
| Family_Lamiaceae     | 0       |
| Family_Linaceae      | 0       |
| Family_Malvaceae     | 0       |
| Family_Piperaceae    | 0       |
| Family_Poaceae       | 0       |
| Family_Rosaceae      | 0       |
| Family_Solanaceae    | 0       |
| Family_Theaceae      | 0       |
| Family_Vitaceae      | 0       |
| Type_Abiotic-biotic  | 0       |
| Type_Biotic-biotic   | 0       |

<b>The table above outlines the parameters used as inputs for the model</b>. 
<li>Stress combination refers to the combinations of abiotic or biotic stresses (e.g., drought + salinity, heat + pathogens) applied to plants in experiments.</li><li>Plant Species refers to the focus species or the specific plant being studied, such as Arabidopsis thaliana, Zea mays (maize), or Oryza sativa (rice). </li><li> Family refers to the taxonomic family of the plant (e.g., Poaceae for grasses, Fabaceae for legumes).</li> <li>Treatments refers to experimental conditions applied to plants, including stresses like salinity, heat, drought, and others.</li><li>Plant Performance (% Reduction) refers to the percentage decrease in plant performance due to the applied stress (biomass, yield, growth).</li><li>Plant Performance Parameter refers to the specific aspect of plant performance being measured, such as biomass, yield, shoot length, root length and others (Please refer to the list in Table 1 in the manuscript).</li><li>Salt refers to the intensity of salinity stress, wherever applied. If no salinity stress is imposed, the term ‘No salt stress applied’ was used .</li><li>Temperature (ºC) refers to the specific temperature condition during the experiment. It also represents the heat or cold stress levels applied to plants, in case the temperature is higher or lower than the ambient temperature for growth of a specific plant.</li><li> Average Temperature refers to the mean ambient temperature for a particular plant species.</li> <li>Drought refers to the water deficit stress imposed on plants, often through controlled reduction of irrigation. If no drought stress is imposed, the term ‘No drought stress applied’ was used.</li> <li>Boron (parts per million or ppm) refers to the concentration of boron (in parts per million) applied as a stress factor. For all cases, except for the one where Boron was a stressor, the concentration was taken as 30 ppm.</li> <li>Cd (ppm) refers to the concentration of cadmium, a heavy metal, applied as a stress factor. For all cases, except for the one where cadmium was a stressor, the concentration was taken as 0 ppm.</li> <li>Mn (ppm) refers to the concentration of manganese, a trace element, applied in the experiment. For all cases, except for the one where manganese was a stressor, the concentration was taken as 0 ppm.</li><li> Pb (ppm) refers to the lead concentration applied to plants as a stress factor. For all cases, except for the one where lead was a stressor, the concentration was taken as 0 ppm. </li> <li>Zinc (ppm) refers to the zinc concentration applied, either as a nutrient or stressor. For all cases, except for the one where Zinc was a stressor, the concentration was taken as 0 ppm.</li> <li>Ni (ppm) refers to the concentration of nickel applied to plants. For all cases, except for the one where Nickel was a stressor, the concentration was taken as 0 ppm.</li> <li>UV (kj/m²) refers to the ultraviolet radiation levels applied, measured in kilojoules per square meter. For all cases, except for the one where UV was a stressor, the concentration was taken as 1 kj/m²).</li> <li>Ozone (ppb) refers to the concentration of ozone in parts per billion. For all cases, except for the one where ozone was a stressor, the concentration was taken as 0 kj/m²).</li> <li>Waterlogging refers to the stress caused by excess water around plant roots, leading to oxygen deprivation. If no waterlogging stress was imposed, the term ‘no waterlogging’ was used.</li><li> Bacteria refers to presence or absence of bacterial stress, which could be due to a pathogenic (causing disease) bacterium. If no bacterial infection was present, the term ‘NA (not applicable)’ was used.</li> <li>Fungus refers to the presence or absence of pathogenic fungal infection, either pathogenic. If no fungal infection was present, the term ‘NA (not applicable)’ was used.</li><li> Oomycete refers to the presence or absence of pathogenic oomycetes. If no oomycete infection was present, the term ‘NA (not applicable)’ was used.</li><li> Virus refers to the presence or absence of viral pathogens. If no viral infection was present, the term ‘NA (not applicable)’ was used. </li><li>Insect refers to the presence or absence of stress caused by insect herbivory or infestation. If no insect infection was present, the term ‘NA (not applicable)’ was used.</li><li> Nematode refers to the presence or absence of nematode infestation, often root-feeding species. If no nematode infection was present, the term ‘NA (not applicable)’ was used.</li><li> Weed refers to the presence or absence of stress caused by competition with weeds for resources (light, water, nutrients). If no weed were present, the term ‘NA (not applicable)’ was used.</li><li>  Light intensity refers to the amount of light energy (measured in units such as μmol photons/m²/s or lux) available to plants. If not light intensity stress (high or low light intensity) was applied the term ‘optimum light intensity’ was used.</li><li> Shade refers to the reduced light availability caused by shading, whether from natural (canopy cover) or artificial sources. If shading was applied, the term 'Shading treatment' was used. In the absence of shading, the term ‘No shading' was used. </li><li>The columns ‘simultaneous’ and ‘sequential’ refer to the timing and interaction of multiple abiotic or biotic stressors affecting plants. Simultaneous refers to combined stress conditions wherein a plant experiences two or more stressors at the same time. (e.g. a combination of heat and drought stress during a dry and hot growing season, and exposure to salinity and heavy metal toxicity in polluted soils). </li><li>Sequential refers to a combined stress condition wherein a plant experiences multiple stressors in a specific temporal sequence, with one stressor followed by another (e.g. heat stress during the day followed by cold stress at night, pathogen attack following physical damage caused by insect herbivory).</li>



### Running the Model

Make sure to have the required libraries installed and upload your data in the same format as `example.csv`. Then, run the `model.py` script.

```bash
python model.py example.csv
```

### Model Creation

The Python code for complete model creation can be found in the Jupyter Notebook file `Combined_stress.ipynb`. The required data for training is available in `X_train.csv` and `y_train.csv`.

### Files

- `model.py`: Python script to run the model.
- `Combined_stress.ipynb`: Jupyter Notebook containing the model creation code.
- `example.csv`: An example file to show the required data format.

### Model Files

- `model_elu.json`: JSON file containing the model architecture.
- `model_elu.h5`: HDF5 file containing the model weights.
- `label_encoder.pkl`: Pickle file containing the LabelEncoder.


```

