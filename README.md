# terminal-ai

![PyPI - Version](https://img.shields.io/pypi/v/protai)

A zero-shot AI assistant in the terminal, backended by GROQ AI, for blazing fast responses.

## Installation

To install protai, simply run the following command in your terminal:

```bash
pip install --upgrade protai
```

## Usage

To use this application, simply run the following command in your terminal:

```bash
protai <query>
```

*For example:*

```bash
protai What is the capital of France?
```

>[!Note]
> On first run you will be prompted to enter your Groq AI API key. You can get one at the [**Groq AI website**](https://console.groq.com/keys).

>[!IMPORTANT]
> You need to have a _**valid Groq AI API key**_ to use this application.

## Development

If you wish to develop for this application, you can clone the repository and install the dependencies using the scripts given:

```bash
git clone https://github.com/protik09/terminal-ai.git
cd terminal-ai
./activate_venv.sh
```

or

```powershell
git clone https://github.com/protik09/terminal-ai.git
cd terminal-ai
.\activate_venv.ps1
```

### Prerequisites

>[!NOTE]
>* Python 3.10 or later 🐍
>* Groq AI API key (available at [Groq AI website](https://console.groq.com/keys))

### Contributing

Contributions are welcome! If you'd like to contribute to this application, please fork the repository and submit a pull request.
>[!WARNING]
> WSL2 is not supported for development. Please use a native Linux or Windows environment. There are issues with keyring access in WSL2.

## License

This application is licensed under the MIT License. See [LICENSE](LICENSE) for details.
