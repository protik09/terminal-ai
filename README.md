# terminal-ai

![Python Language](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

![PyPI - Version](https://img.shields.io/pypi/v/protai) ![GitHub](https://img.shields.io/github/license/protik09/terminal-ai) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) ![Issues Open](https://img.shields.io/github/issues/protik09/terminal-ai.svg)
<!-- ![MintenanceNo](https://img.shields.io/badge/Maintained%3F-no-red.svg) -->

![Powershell](https://img.shields.io/badge/powershell-5391FE?style=for-the-badge&logo=powershell&logoColor=white) ![Bash](https://img.shields.io/badge/GNU%20Bash-4EAA25?style=for-the-badge&logo=GNU%20Bash&logoColor=white) ![WinTerm](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)


A zero-shot AI assistant in the terminal, backended by *GROQ AI*, for blazing fast responses.

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

![ProtAI Demo](https://github.com/protik09/terminal-ai/blob/master/assets/protai_demo.jpeg?raw=true "ProtAI Demo")


>[!Note]
> On first run you will be prompted to enter your Groq AI API key. You can get one at the [**Groq AI website**](https://console.groq.com/keys).

>[!IMPORTANT]
> You need to have a _**valid Groq AI API key**_ to use this application.

## Development

The *GROQ API* is using the _**llama3-8b-8192**_ model, as that has the fastest response time.

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

### Program Flow Chart

![Program Flow Chart](https://mermaid.ink/svg/pako:eNqNlFtzojAUx7_KmTyrI1Z64WFnrFrr2mpbWnvBTicDUZhCQkOwdcHvviFBLM7uzvKUk_xyLv9zSIZc5hFkoRXHsQ_3gwUF-fUcW2AuXqHZ_AHnWd8n7jtgvkojQkWy1dB5cZpP2f4gh75zwwMqIE3wigCmHpCvQLx-v9Bs-iSMcxj8D7omPAkYzWHo9HEYQmlfSjwk_AB2fUxXJIcLp69W0LsZwzvZ_Nn5Q0I4BDRORQ4jmQtzSZLIbHa7Etb4SKlw6fRS4csqAxcLAp-B8GF0N7stgpR-L5VfLdaQrmGOeQ7jrKDeJPU2GT5L10DoulRwrC48EyncT0fmUxztkn79jkxZDhNnRERV0pKzqFhICVclOlF5XmUTvVtUnFTNutqHulahyrsH4a6qcNNCkigWWpEl4wfkVEWbOXMcBl6hiOLqzEx5U0QON3KmGN83RSpRz1_TY7rW_G05H4RzGfyghd8Fv8BBmHLZd_tfNzRrp27R5hzunD4nRdojzj7ADQPZ2arjd6q2e8eWgiebRJAIYiVG6etenT84gyCJQ7yBJA4oldWXQyRLarVaJfug2HlmE5kPJx8pSQQIVs1O2Z95Pb1H1WxO4nCn5aPy81SIGFcBE80v07DinhT3XEqhPBRSX2P-7rFPWtU4r2v3UnesxnupD0vHL8pxr_c3kTXV19S5M9xLPyj3tDWsWRc1y65ZtzWr16tM1EAR4REOPPlyZcXxAsl_MyILZMmlR5Y4DcUCLehWojgVzN5QF1mCp6SBOEtXPrKWOEyklcbF9A4CLF_AaIcQL5Czeq2fRvVCNlCM6QtjFSJNZGXoC1lmq22enh6dnZ6Zxx3DPDLMBtogq9syzXbnpGN0u2emYZ6cmNsG-qU8GK22_jpHx912xzCOt78BWwa5ZA?raw=true "Program Flow Chart")

### Contributing

Contributions are welcome! If you'd like to contribute to this application, please fork the repository and submit a pull request.
>[!WARNING]
> WSL2 is not supported for development. Please use a native Linux or Windows environment. There are issues with keyring access in WSL2.

## License

This application is licensed under the MIT License. See [LICENSE](LICENSE) for details.
