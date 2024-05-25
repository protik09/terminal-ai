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

[![Program Flow Chart](https://mermaid.ink/img/pako:eNqNlNtu4jAQhl9l5GtAHMrxYqUUKGVpoS0tPYSqshIDURM7dRxaNuHdd-KE0KDd1XKV8Xyewz-DI2IJm5EeWUvqb-B-sOSAP8OcKyrVK5TLP-A86m-Y9Q5UrkOPcRXsU-g88cZTcXTE0DdvpMMVhAFdM6DcBvblqNfvF8rlDXP9GAb_g26ZDBzBYxiafeq6kNmXiLtMnsDWhvI1i-HC7OsvMG7G8M52fw7-EDAJDvdDFcMIaxEWCwKs5nCKcIqPtAqXphGqDXbpWFQx-HTUBkZ3s9skSRb3UsdNxRryLSyojGEcJdQbUm-T4TOGBsa3mYJjfeGZoXA_TawncR2Kfv2OTEUME3PEVN7SSgov-UAJ1xk60XVeRZP0NOk4yId1dUx1rVNld0_SXeXppokknq9SRVZCnpBTnW1mLqjr2IkimisyMx1NEzHc4E4JeRwKKlGsP6XHfJvyt9l-MCkx-ckIvwt-QR03lDj3-b9upOw8tJIxx3Bn9iVLyh5J8QGW6-Bk84nf6d7uzTkKHuwCxTzwtRhZrHvtfzAHTuC7dAeB73CO3WdLhC1VKpWMfdDsIpozrEeyj5AFCpTIdyebz6JY3qMetmS-e9DyUcd5SkT084RByq9CN-eeNPecSaEjJFJfU_lui0-e97goavdSDKzXe5U6s8AvOrBh_E3klOqn1Lk5PEo_yM5Sa1iwLgrWvGDdFizDyE1SIh6THnVsfLmixL0k-N_02JL08NPGXpdkyffI0VCJ-Y5bpKdkyEpEinC9Ib0VdQO0Qj9Z3YFD8fnz8lNmO7ip1-nDqN_HEvEpfxHCO4RBk_Qi8kV6nUal2-nWGrVau96sV89KZEd65Vaz0ui0m61OvXbWPWs36_sS-aXv1yrVerPbbLUa1Xa11e60978Bg-S3_A?type=png)](https://mermaid.live/edit#pako:eNqNlNtu4jAQhl9l5GtAHMrxYqUUKGVpoS0tPYSqshIDURM7dRxaNuHdd-KE0KDd1XKV8Xyewz-DI2IJm5EeWUvqb-B-sOSAP8OcKyrVK5TLP-A86m-Y9Q5UrkOPcRXsU-g88cZTcXTE0DdvpMMVhAFdM6DcBvblqNfvF8rlDXP9GAb_g26ZDBzBYxiafeq6kNmXiLtMnsDWhvI1i-HC7OsvMG7G8M52fw7-EDAJDvdDFcMIaxEWCwKs5nCKcIqPtAqXphGqDXbpWFQx-HTUBkZ3s9skSRb3UsdNxRryLSyojGEcJdQbUm-T4TOGBsa3mYJjfeGZoXA_TawncR2Kfv2OTEUME3PEVN7SSgov-UAJ1xk60XVeRZP0NOk4yId1dUx1rVNld0_SXeXppokknq9SRVZCnpBTnW1mLqjr2IkimisyMx1NEzHc4E4JeRwKKlGsP6XHfJvyt9l-MCkx-ckIvwt-QR03lDj3-b9upOw8tJIxx3Bn9iVLyh5J8QGW6-Bk84nf6d7uzTkKHuwCxTzwtRhZrHvtfzAHTuC7dAeB73CO3WdLhC1VKpWMfdDsIpozrEeyj5AFCpTIdyebz6JY3qMetmS-e9DyUcd5SkT084RByq9CN-eeNPecSaEjJFJfU_lui0-e97goavdSDKzXe5U6s8AvOrBh_E3klOqn1Lk5PEo_yM5Sa1iwLgrWvGDdFizDyE1SIh6THnVsfLmixL0k-N_02JL08NPGXpdkyffI0VCJ-Y5bpKdkyEpEinC9Ib0VdQO0Qj9Z3YFD8fnz8lNmO7ip1-nDqN_HEvEpfxHCO4RBk_Qi8kV6nUal2-nWGrVau96sV89KZEd65Vaz0ui0m61OvXbWPWs36_sS-aXv1yrVerPbbLUa1Xa11e60978Bg-S3_A)

### Contributing

Contributions are welcome! If you'd like to contribute to this application, please fork the repository and submit a pull request.
>[!WARNING]
> WSL2 is not supported for development. Please use a native Linux or Windows environment. There are issues with keyring access in WSL2.

## License

This application is licensed under the MIT License. See [LICENSE](LICENSE) for details.
