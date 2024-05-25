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

[![](https://mermaid.ink/img/pako:eNqNlNtu4jAQhl9l5GtAUM5crJQCpSwttE1LD6GqrMSQqImdOg4tm_DuazshNGh3tVxlPJ_n8M_gBNnMIWiANhyHLtyPVhTkz7BMgbl4hWr1B5wnQ5fY74D5Jg4IFdE-g86VN52zoyOFoXXDPSogjvCGAKYOkC9PvH6_UK26xA9TGP0PuiU88hhNYWwNse9Dbl9K3Cf8BLZdTDckhQtrqL_AuJnCO9n9OfhDRDh4NIxFChNZC7NJFMlqDqcSzvCJVuHSMmLhyi49GwsCn55wYXK3uFVJ8riXOm4m1phuYYl5CtNEUW-SepuNn2VoIHSbKzjVF56JFO6nJetRrkPRr9-ROUthZk2IKFpacxaoDynhJkdnus6rZJadqo6jYlhXx1TXOlV-9yTdVZFuriQJQpEpsmb8hJzrbAtriX3PUYporswsdDRNpHAjd4rx41CkEuX6M3pKtxl_m-8H4VwmPxnhd8EvsOfHXM7d_NeNjDVjW405hTtryIkqe8LZB9i-JydbTPxO93ZvmVLwaBcJEkCoxchj3Wv_gzXyotDHO4hCj1LZfb5EsqVarZazD5pdJiaR9XDyEZNIgGDF7uTzWZbLe9TD5iT0D1o-6jhPSsSwSBhl_Dr2C-5Jc8-5FDqCkvoa83eHfdKix2VZu5dyYL3e68yZB37RgQ3jbyJn1DCjzq3xUfpRfpZZ45J1UbLMknVbsgyjMFEFBYQH2HPky5Uo9wrJ_2ZAVmggPx2yxrEvVmhF9xLFsWDmjtpoIHhMKoizeOMejDhUyzvysHwAg8MhcTy5qtfZy6gfyAoKMX1hrECkiQYJ-kKDxlm_dtZp9Zr1dr_ZaXY63QraoUG11audNeRpt9lr1Lv11r6CfukA9Vq_XW-0O71Ot11vNRr93v435xO5Aw?type=png)](https://mermaid.live/edit#pako:eNqNlNtu4jAQhl9l5GtAUM5crJQCpSwttE1LD6GqrMSQqImdOg4tm_DuazshNGh3tVxlPJ_n8M_gBNnMIWiANhyHLtyPVhTkz7BMgbl4hWr1B5wnQ5fY74D5Jg4IFdE-g86VN52zoyOFoXXDPSogjvCGAKYOkC9PvH6_UK26xA9TGP0PuiU88hhNYWwNse9Dbl9K3Cf8BLZdTDckhQtrqL_AuJnCO9n9OfhDRDh4NIxFChNZC7NJFMlqDqcSzvCJVuHSMmLhyi49GwsCn55wYXK3uFVJ8riXOm4m1phuYYl5CtNEUW-SepuNn2VoIHSbKzjVF56JFO6nJetRrkPRr9-ROUthZk2IKFpacxaoDynhJkdnus6rZJadqo6jYlhXx1TXOlV-9yTdVZFuriQJQpEpsmb8hJzrbAtriX3PUYporswsdDRNpHAjd4rx41CkEuX6M3pKtxl_m-8H4VwmPxnhd8EvsOfHXM7d_NeNjDVjW405hTtryIkqe8LZB9i-JydbTPxO93ZvmVLwaBcJEkCoxchj3Wv_gzXyotDHO4hCj1LZfb5EsqVarZazD5pdJiaR9XDyEZNIgGDF7uTzWZbLe9TD5iT0D1o-6jhPSsSwSBhl_Dr2C-5Jc8-5FDqCkvoa83eHfdKix2VZu5dyYL3e68yZB37RgQ3jbyJn1DCjzq3xUfpRfpZZ45J1UbLMknVbsgyjMFEFBYQH2HPky5Uo9wrJ_2ZAVmggPx2yxrEvVmhF9xLFsWDmjtpoIHhMKoizeOMejDhUyzvysHwAg8MhcTy5qtfZy6gfyAoKMX1hrECkiQYJ-kKDxlm_dtZp9Zr1dr_ZaXY63QraoUG11audNeRpt9lr1Lv11r6CfukA9Vq_XW-0O71Ot11vNRr93v435xO5Aw)

### Contributing

Contributions are welcome! If you'd like to contribute to this application, please fork the repository and submit a pull request.
>[!WARNING]
> WSL2 is not supported for development. Please use a native Linux or Windows environment. There are issues with keyring access in WSL2.

## License

This application is licensed under the MIT License. See [LICENSE](LICENSE) for details.
