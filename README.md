# Terminal-AI

![Python Language](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

![PyPI - Version](https://img.shields.io/pypi/v/protai) ![GitHub](https://img.shields.io/github/license/protik09/terminal-ai) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) ![Issues Open](https://img.shields.io/github/issues/protik09/terminal-ai.svg)
<!-- ![MintenanceNo](https://img.shields.io/badge/Maintained%3F-no-red.svg) -->

![Powershell](https://img.shields.io/badge/powershell-5391FE?style=for-the-badge&logo=powershell&logoColor=white) ![Bash](https://img.shields.io/badge/GNU%20Bash-4EAA25?style=for-the-badge&logo=GNU%20Bash&logoColor=white) ![WinTerm](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

<!-- ![ProtAI Logo](assets/protai_logo.jpg) -->

A zero-shot AI assistant in the terminal, backended by the *GROQ AI*, for blazing fast responses. The **free** API key from *GROQ* can be obtained [here](https://console.groq.com/keys)

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
> On first run you will be prompted to enter your **free** *Groq AI* API key. You can get one at the [**Groq AI website**](https://console.groq.com/keys).

>[!IMPORTANT]
> You need to have a _**valid Groq AI API key**_ to use this application.

## Development

The application is using the _**llama-3.1-8b-instant**_ model for its instant inference, as that has the fastest response time.
The interactive version is using the  **llama-3.3-70b-versatile** for its 0-shot inference.

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

To generate the wheel and upload to PyPI, we use the following command:

```bash
python setup.py upload
```

> [!IMPORTANT]
> Only the current maintainer has access to the [**PyPI**](https://pypi.org/project/protai/) repository API key. If you wish to contribute, please fork the repository and submit a pull request.

### Prerequisites

>[!NOTE]
>* Python 3.10 or later 🐍
>* Groq AI API key (available at [Groq AI website](https://console.groq.com/keys))

### Program Flow Chart

![Program Flow Chart](https://mermaid.ink/svg/pako:eNqdVl1T6jAQ_SuZ3PENGBG4ah_uTPkQEUGlih_FcTIlhY5tWpNU5VL--92mpVLHO6PhKbs5Z3dzdunsGjvhnGIDLziJlui6O2MIfqZtScLlI6pW_6D2urOkzjMifBEHlEmxyUDt9DYZhx8XCerYl9xjEsWCLCgibI7ouycfdwnV6pL6UYK634G-Ui68kCWoZ3eI76PcPgW4T_knsLMkbEETdGJ31AmZlwP0TFdfB78RlCOPRbFMUB9qCR0qBFSz9QI4g_eVCqe2GcslvNJziKTozZNL1J9cXKVJ8rinKm4mVo-9oinhCRqsU9QToJ6GvXsIjSh7zRUcKMI9BeHObKgnvdoW_bgLGYcJGtp9KosnuTwM0gNIuMihQ1Xn-XqYedMXi6JZ5x-pRipVzv2U7rxIN04lCSKZKeKG_BNyrLJd2FPie_NUEYUrYy5UNIVI0CXMVMg_mgJKlOvP0AP2muGv8vmgnEPyTy3cFfyEeH7Moe_W14wS2IqdtM8JmtgdTtO6-zx8QY7vQWuz4Nu-T9QLr20LZBcrIWmAIiVJXsO1ur-xu56IfLJCIvIYAw3yUYKH1Wq1HHujsNO1RaEqTl9iKiSSYTFBeZem5RpvVcs5jfytorcqzl0qZVQkFBnejf0Cd6dw97kgKkIq-Ijw53n4xorZnpYVfCgHVkPuZpd54AcV2DT_15wM1clQbbv30bJu7susXsk6KVlWyboqWaZZmJljbw9ZcuWno8zgUyYyrwAXjBpyPd83frmuA7-KkDx8psavRqORn6tv3lwujYPofZfW3qEdH3-b1iloKfHbtK4erZfTHOdHtBM9Wl9PklM92kCPdrbzNtf9Nm2oRzvXK3Kkl22s17cLPdqlHu1K7_820ZPE0st2rZftRo821aPd6tHu9Pp2r0d70GuAqflZNts_4eEKDigPiDeH7Xadxplh2N8COsMGHOfUJbEvZ3jGNgAlsQytFXOwIXlMK5iH8WKJDZf4Aqw4SjecrkdgSw4KL517sNCMsv1ZrdEVHBH2EIbBNgyY2Fjjd2w067XfjUaz3jo6aDaOj_YPK3gF3lqrtX9weFBvNo9b9dbhYWtTwX9VgPrmH82NxJY?raw=true "Program Flow Chart")

### Contributing

Contributions are welcome! If you'd like to contribute to this application, please fork the repository and submit a pull request.
>[!WARNING]
> WSL2 is not supported for development. Please use a native Linux or Windows environment. There are issues with keyring access in WSL2.

## License

This application is licensed under the MIT License. See [LICENSE](LICENSE) for details.
