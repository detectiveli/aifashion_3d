# Body Model Visualizer with Anthropometry Analysis

### Introduction

This is an enhanced Open3D-based GUI for SMPL-family body models, integrated with anthropometry analysis capabilities. This tool allows you to:

- Interactive editing of shape, expression, and pose parameters
- Visualize body model joints and joint names
- Simple IK solver to match an input pose
- Save edited model parameters
- View controls, lighting controls, and material settings
- Web visualization support
- Anthropometry data calculation and visualization

This tool is designed for researchers and developers working with 3D body models who need quick editing, visualization, and anthropometric analysis capabilities without installing complex graphics software.

## Installation

Clone the repo and install the requirements (use python3.9):

```shell
pip install -r requirements.txt
```

Download the SMPL, SMPL-X, MANO, FLAME body models:

- SMPL: https://smpl.is.tue.mpg.de/ (v1.1.0)
- SMPL-X: https://smpl-x.is.tue.mpg.de/ (v1.1)
- MANO: https://mano.is.tue.mpg.de/
- FLAME: https://flame.is.tue.mpg.de/
  - For landmarks: https://github.com/soubhiksanyal/RingNet/blob/master/flame_model/

Copy downloaded files under `data/body_models`, this folder should look like:

```shell
data
└── body_models
    ├── flame
    │   ├── FLAME_FEMALE.pkl
    │   ├── FLAME_MALE.pkl
    │   ├── FLAME_NEUTRAL.pkl
    │   ├── flame_dynamic_embedding.npy
    │   └── flame_static_embedding.pkl
    ├── mano
    │   ├── MANO_LEFT.pkl
    │   └── MANO_RIGHT.pkl
    ├── smpl
    │   ├── SMPL_FEMALE.pkl
    │   ├── SMPL_MALE.pkl
    │   └── SMPL_NEUTRAL.pkl
    └── smplx
        ├── SMPLX_FEMALE.npz
        ├── SMPLX_MALE.npz
        └── SMPLX_NEUTRAL.npz

```

Finally, run:
```shell
python main.py
```
If you want to enable web visualization, run:
```shell
python main.py --web
```

## Guidelines

### Saved model parameters
`File > Save Model Params` lets you save the edited body model parameters. Output is a pickled
python dictionary with below keys:
```shell
dict_keys(['betas', 'expression', 'gender', 'body_model', 
           'joints', 'body_pose', 'global_orient'])
```

### Anthropometry Analysis
This tool includes capabilities to calculate and visualize anthropometric measurements based on the body model. The measurements are calculated using the `SMPL-Anthropometry-master` module integrated into this project.

## Todo List

1. Add support for SMPLX files generated from the method provided in [https://github.com/vchoutas/smplx](https://github.com/vchoutas/smplx)
2. Improve the test result visualization page, add lines to connect joints
3. Optimize the calculation speed of body parameters
4. add manual point measurement

## Acknowledgements

This project is built upon two main code repositories:

1. **Body Model Visualizer**: Original code for visualizing SMPL-family body models. https://github.com/mkocabas/body-model-visualizer
2. **SMPL-Anthropometry**: Anthropometric measurement calculation module integrated into this project. https://github.com/DavidBoja/SMPL-Anthropometry

We would like to express our gratitude to the authors and contributors of these original code bases for their valuable work.
