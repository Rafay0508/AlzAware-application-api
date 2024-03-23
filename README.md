# Alzheimer's Disease Detection Model

This repository contains the source code for an Alzheimer's disease detection model. The model is trained to analyze neuroimaging data and predict the likelihood of Alzheimer's disease development.

## Getting Started

To run the model locally, follow these steps:

### Prerequisites

- Python 3.x
- TensorFlow
- Keras
- Flask

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/alzheimers-detection-model.git
```

2. Navigate to the project directory:

```bash
cd alzheimers-detection-model
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Usage

1. Download the pre-trained model file `updated_model.h5` from the following Google Drive link: [updated_model.h5](https://drive.google.com/file/d/1BjDFxw-qEmKY61SuENHsEpoTzLaYvYsy/view?usp=drive_link).

2. Place the downloaded `updated_model.h5` file in the `models` directory of the project.

3. Start the Flask web server:

```bash
python app.py
```

4. The server will start running locally. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the application.

### Using Ngrok for External Access

If you want to access the application externally using Ngrok, follow these additional steps:

1. Install Ngrok on your machine. You can download it from the official website: [Ngrok](https://ngrok.com/download).

2. Start Ngrok and expose your local server:

```bash
ngrok http --host-header=localhost 5000
```

3. Ngrok will generate a public URL that you can use to access the application from anywhere.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the contributors and developers of the libraries and frameworks used in this project.
