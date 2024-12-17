# Blendify-modified version
## Artefact replication
* Clone repository
* Open project with Pycharm (Python 3.10 required)
* Setup virtual environment <br/>
  - Create virtual env: <br/>
  ```bash
  python -m venv venv 
  ```
  - Activate virtual env: <br/>
  ```bash
  .\venv\Scripts\activate
  ```
* Install Blendify in editable mode with all dependencies <br/>
  ```bash
  pip install -e .[all]
  ```
## Artefact interaction
We reproduced the cube renderer script and one of the google colab demos. We also added a cylinder renderer script where we test materials.
## Artefact contributions
We added a text mesh class definition inside the primitives file and integrated it in the API for easier access.This class is used for rendering 3D text.
