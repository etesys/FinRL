{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "V1ofncK2cYhs"
      },
      "source": [
        "Disclaimer: Nothing herein is financial advice, and NOT a recommendation to trade real money. Many platforms exist for simulated trading (paper trading) which can be used for building and developing the methods discussed. Please use common sense and always first consult a professional before trading or investing."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lZpyg1Anea4G"
      },
      "source": [
        "<a target=\"_blank\" href=\"https://colab.research.google.com/github/AI4Finance-Foundation/FinRL-Tutorials/blob/master/3-Practical/FinRL_PaperTrading_Demo.ipynb\">\n",
        "  <img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/>\n",
        "</a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "j3mbRu3s1YlD"
      },
      "source": [
        "# Part 1: Install FinRL"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 211,
      "metadata": {
        "id": "0gkmsPgbvNf6",
        "outputId": "c425a1c8-dd7e-4b94-b95b-a51d66cc27ba",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: wrds in /usr/local/lib/python3.10/site-packages (3.1.6)\n",
            "Requirement already satisfied: sqlalchemy<2 in /usr/local/lib/python3.10/site-packages (from wrds) (1.4.51)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/site-packages (from wrds) (1.26.3)\n",
            "Requirement already satisfied: psycopg2-binary in /usr/local/lib/python3.10/site-packages (from wrds) (2.9.9)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.10/site-packages (from wrds) (1.11.4)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/site-packages (from wrds) (2.1.4)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/site-packages (from sqlalchemy<2->wrds) (3.0.3)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/site-packages (from pandas->wrds) (2023.3.post1)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/site-packages (from pandas->wrds) (2023.4)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/site-packages (from pandas->wrds) (2.8.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/site-packages (from python-dateutil>=2.8.2->pandas->wrds) (1.16.0)\n",
            "\u001b[33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\u001b[0m\u001b[33m\n",
            "\u001b[0mRequirement already satisfied: swig in /usr/local/lib/python3.10/site-packages (4.1.1.post1)\n",
            "\u001b[33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\u001b[0m\u001b[33m\n",
            "\u001b[0m\u001b[33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\u001b[0m\u001b[33m\n",
            "\u001b[0m✨🍰✨ Everything looks OK!\n",
            "Collecting git+https://github.com/AI4Finance-Foundation/FinRL.git\n",
            "  Cloning https://github.com/AI4Finance-Foundation/FinRL.git to /tmp/pip-req-build-ecanjlyx\n",
            "  Running command git clone --filter=blob:none --quiet https://github.com/AI4Finance-Foundation/FinRL.git /tmp/pip-req-build-ecanjlyx\n",
            "  Resolved https://github.com/AI4Finance-Foundation/FinRL.git to commit 754bd1bb560a90d98494e116e734998353f02a34\n",
            "  Installing build dependencies ... \u001b[?25l\u001b[?25hdone\n",
            "  Getting requirements to build wheel ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting elegantrl@ git+https://github.com/AI4Finance-Foundation/ElegantRL.git#egg=elegantrl\n",
            "  Cloning https://github.com/AI4Finance-Foundation/ElegantRL.git to /tmp/pip-install-0k3lbnsm/elegantrl_8c9c08ae5b1d4cc7bc16f136918e7f4e\n",
            "  Running command git clone --filter=blob:none --quiet https://github.com/AI4Finance-Foundation/ElegantRL.git /tmp/pip-install-0k3lbnsm/elegantrl_8c9c08ae5b1d4cc7bc16f136918e7f4e\n",
            "  Resolved https://github.com/AI4Finance-Foundation/ElegantRL.git to commit b4b9d662b9f9cb7cc368ac2b1036b5119eb20be4\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: ray[default,tune]<3,>=2 in /usr/local/lib/python3.10/site-packages (from finrl==0.3.6) (2.9.0)\n",
            "Requirement already satisfied: pyportfolioopt<2,>=1 in /usr/local/lib/python3.10/site-packages (from finrl==0.3.6) (1.5.5)\n",
            "Requirement already satisfied: ccxt<4,>=3 in /usr/local/lib/python3.10/site-packages (from finrl==0.3.6) (3.1.60)\n",
            "Requirement already satisfied: pyfolio<0.10,>=0.9 in /usr/local/lib/python3.10/site-packages (from finrl==0.3.6) (0.9.2)\n",
            "Requirement already satisfied: alpaca-trade-api<4,>=3 in /usr/local/lib/python3.10/site-packages (from finrl==0.3.6) (3.0.2)\n",
            "Requirement already satisfied: scikit-learn<2,>=1 in /usr/local/lib/python3.10/site-packages (from finrl==0.3.6) (1.3.2)\n",
            "Requirement already satisfied: stockstats<0.6,>=0.5 in /usr/local/lib/python3.10/site-packages (from finrl==0.3.6) (0.5.4)\n",
            "Requirement already satisfied: yfinance<0.3,>=0.2 in /usr/local/lib/python3.10/site-packages (from finrl==0.3.6) (0.2.35)\n",
            "Requirement already satisfied: jqdatasdk<2,>=1 in /usr/local/lib/python3.10/site-packages (from finrl==0.3.6) (1.9.2)\n",
            "Requirement already satisfied: stable-baselines3[extra]>=2.0.0a5 in /usr/local/lib/python3.10/site-packages (from finrl==0.3.6) (2.2.1)\n",
            "Requirement already satisfied: wrds<4,>=3 in /usr/local/lib/python3.10/site-packages (from finrl==0.3.6) (3.1.6)\n",
            "Requirement already satisfied: exchange-calendars<5,>=4 in /usr/local/lib/python3.10/site-packages (from finrl==0.3.6) (4.5.1)\n",
            "Requirement already satisfied: numpy>=1.11.1 in /usr/local/lib/python3.10/site-packages (from alpaca-trade-api<4,>=3->finrl==0.3.6) (1.26.3)\n",
            "Requirement already satisfied: websockets<11,>=9.0 in /usr/local/lib/python3.10/site-packages (from alpaca-trade-api<4,>=3->finrl==0.3.6) (10.4)\n",
            "Requirement already satisfied: msgpack==1.0.3 in /usr/local/lib/python3.10/site-packages (from alpaca-trade-api<4,>=3->finrl==0.3.6) (1.0.3)\n",
            "Requirement already satisfied: requests<3,>2 in /usr/local/lib/python3.10/site-packages (from alpaca-trade-api<4,>=3->finrl==0.3.6) (2.31.0)\n",
            "Requirement already satisfied: deprecation==2.1.0 in /usr/local/lib/python3.10/site-packages (from alpaca-trade-api<4,>=3->finrl==0.3.6) (2.1.0)\n",
            "Requirement already satisfied: aiohttp==3.8.2 in /usr/local/lib/python3.10/site-packages (from alpaca-trade-api<4,>=3->finrl==0.3.6) (3.8.2)\n",
            "Requirement already satisfied: PyYAML==6.0 in /usr/local/lib/python3.10/site-packages (from alpaca-trade-api<4,>=3->finrl==0.3.6) (6.0)\n",
            "Requirement already satisfied: pandas>=0.18.1 in /usr/local/lib/python3.10/site-packages (from alpaca-trade-api<4,>=3->finrl==0.3.6) (2.1.4)\n",
            "Requirement already satisfied: websocket-client<2,>=0.56.0 in /usr/local/lib/python3.10/site-packages (from alpaca-trade-api<4,>=3->finrl==0.3.6) (1.7.0)\n",
            "Requirement already satisfied: urllib3<2,>1.24 in /usr/local/lib/python3.10/site-packages (from alpaca-trade-api<4,>=3->finrl==0.3.6) (1.26.15)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/site-packages (from aiohttp==3.8.2->alpaca-trade-api<4,>=3->finrl==0.3.6) (1.9.4)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/site-packages (from aiohttp==3.8.2->alpaca-trade-api<4,>=3->finrl==0.3.6) (1.4.1)\n",
            "Requirement already satisfied: charset-normalizer<3.0,>=2.0 in /usr/local/lib/python3.10/site-packages (from aiohttp==3.8.2->alpaca-trade-api<4,>=3->finrl==0.3.6) (2.1.1)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/site-packages (from aiohttp==3.8.2->alpaca-trade-api<4,>=3->finrl==0.3.6) (23.2.0)\n",
            "Requirement already satisfied: multidict<6.0,>=4.5 in /usr/local/lib/python3.10/site-packages (from aiohttp==3.8.2->alpaca-trade-api<4,>=3->finrl==0.3.6) (5.2.0)\n",
            "Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /usr/local/lib/python3.10/site-packages (from aiohttp==3.8.2->alpaca-trade-api<4,>=3->finrl==0.3.6) (4.0.3)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/site-packages (from aiohttp==3.8.2->alpaca-trade-api<4,>=3->finrl==0.3.6) (1.3.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.10/site-packages (from deprecation==2.1.0->alpaca-trade-api<4,>=3->finrl==0.3.6) (23.2)\n",
            "Requirement already satisfied: setuptools>=60.9.0 in /usr/local/lib/python3.10/site-packages (from ccxt<4,>=3->finrl==0.3.6) (65.6.3)\n",
            "Requirement already satisfied: cryptography>=2.6.1 in /usr/local/lib/python3.10/site-packages (from ccxt<4,>=3->finrl==0.3.6) (40.0.1)\n",
            "Requirement already satisfied: certifi>=2018.1.18 in /usr/local/lib/python3.10/site-packages (from ccxt<4,>=3->finrl==0.3.6) (2022.12.7)\n",
            "Requirement already satisfied: aiodns>=1.1.1 in /usr/local/lib/python3.10/site-packages (from ccxt<4,>=3->finrl==0.3.6) (3.1.1)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/site-packages (from exchange-calendars<5,>=4->finrl==0.3.6) (0.12.0)\n",
            "Requirement already satisfied: korean-lunar-calendar in /usr/local/lib/python3.10/site-packages (from exchange-calendars<5,>=4->finrl==0.3.6) (0.3.1)\n",
            "Requirement already satisfied: pyluach in /usr/local/lib/python3.10/site-packages (from exchange-calendars<5,>=4->finrl==0.3.6) (2.2.0)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.10/site-packages (from exchange-calendars<5,>=4->finrl==0.3.6) (2.8.2)\n",
            "Requirement already satisfied: tzdata in /usr/local/lib/python3.10/site-packages (from exchange-calendars<5,>=4->finrl==0.3.6) (2023.4)\n",
            "Requirement already satisfied: thriftpy2>=0.3.9 in /usr/local/lib/python3.10/site-packages (from jqdatasdk<2,>=1->finrl==0.3.6) (0.4.17)\n",
            "Requirement already satisfied: SQLAlchemy>=1.2.8 in /usr/local/lib/python3.10/site-packages (from jqdatasdk<2,>=1->finrl==0.3.6) (1.4.51)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.10/site-packages (from jqdatasdk<2,>=1->finrl==0.3.6) (1.16.0)\n",
            "Requirement already satisfied: pymysql>=0.7.6 in /usr/local/lib/python3.10/site-packages (from jqdatasdk<2,>=1->finrl==0.3.6) (1.1.0)\n",
            "Requirement already satisfied: scipy>=0.14.0 in /usr/local/lib/python3.10/site-packages (from pyfolio<0.10,>=0.9->finrl==0.3.6) (1.11.4)\n",
            "Requirement already satisfied: empyrical>=0.5.0 in /usr/local/lib/python3.10/site-packages (from pyfolio<0.10,>=0.9->finrl==0.3.6) (0.5.5)\n",
            "Requirement already satisfied: matplotlib>=1.4.0 in /usr/local/lib/python3.10/site-packages (from pyfolio<0.10,>=0.9->finrl==0.3.6) (3.8.2)\n",
            "Requirement already satisfied: ipython>=3.2.3 in /usr/local/lib/python3.10/site-packages (from pyfolio<0.10,>=0.9->finrl==0.3.6) (8.19.0)\n",
            "Requirement already satisfied: pytz>=2014.10 in /usr/local/lib/python3.10/site-packages (from pyfolio<0.10,>=0.9->finrl==0.3.6) (2023.3.post1)\n",
            "Requirement already satisfied: seaborn>=0.7.1 in /usr/local/lib/python3.10/site-packages (from pyfolio<0.10,>=0.9->finrl==0.3.6) (0.13.1)\n",
            "Requirement already satisfied: cvxpy<2.0.0,>=1.1.19 in /usr/local/lib/python3.10/site-packages (from pyportfolioopt<2,>=1->finrl==0.3.6) (1.4.1)\n",
            "Requirement already satisfied: protobuf!=3.19.5,>=3.15.3 in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (4.23.4)\n",
            "Requirement already satisfied: jsonschema in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (4.20.0)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (8.1.7)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (3.13.1)\n",
            "Requirement already satisfied: prometheus-client>=0.7.1 in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (0.19.0)\n",
            "Requirement already satisfied: py-spy>=0.2.0 in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (0.3.14)\n",
            "Requirement already satisfied: aiohttp-cors in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (0.7.0)\n",
            "Requirement already satisfied: grpcio>=1.42.0 in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (1.60.0)\n",
            "Requirement already satisfied: opencensus in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (0.11.4)\n",
            "Requirement already satisfied: virtualenv<20.21.1,>=20.0.24 in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (20.21.0)\n",
            "Requirement already satisfied: pydantic!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,<3 in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (2.5.3)\n",
            "Requirement already satisfied: gpustat>=1.0.0 in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (1.1.1)\n",
            "Requirement already satisfied: colorful in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (0.5.6)\n",
            "Requirement already satisfied: smart-open in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (6.4.0)\n",
            "Requirement already satisfied: pyarrow>=6.0.1 in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (14.0.2)\n",
            "Requirement already satisfied: tensorboardX>=1.9 in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (2.6.2.2)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.10/site-packages (from ray[default,tune]<3,>=2->finrl==0.3.6) (2023.12.2)\n",
            "Requirement already satisfied: threadpoolctl>=2.0.0 in /usr/local/lib/python3.10/site-packages (from scikit-learn<2,>=1->finrl==0.3.6) (3.2.0)\n",
            "Requirement already satisfied: joblib>=1.1.1 in /usr/local/lib/python3.10/site-packages (from scikit-learn<2,>=1->finrl==0.3.6) (1.3.2)\n",
            "Requirement already satisfied: gymnasium<0.30,>=0.28.1 in /usr/local/lib/python3.10/site-packages (from stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (0.29.1)\n",
            "Requirement already satisfied: torch>=1.13 in /usr/local/lib/python3.10/site-packages (from stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (2.1.2)\n",
            "Requirement already satisfied: cloudpickle in /usr/local/lib/python3.10/site-packages (from stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (3.0.0)\n",
            "Requirement already satisfied: opencv-python in /usr/local/lib/python3.10/site-packages (from stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (4.9.0.80)\n",
            "Requirement already satisfied: pygame in /usr/local/lib/python3.10/site-packages (from stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (2.1.0)\n",
            "Requirement already satisfied: autorom[accept-rom-license]~=0.6.1 in /usr/local/lib/python3.10/site-packages (from stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (0.6.1)\n",
            "Requirement already satisfied: shimmy[atari]~=1.3.0 in /usr/local/lib/python3.10/site-packages (from stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (1.3.0)\n",
            "Requirement already satisfied: pillow in /usr/local/lib/python3.10/site-packages (from stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (10.2.0)\n",
            "Requirement already satisfied: tensorboard>=2.9.1 in /usr/local/lib/python3.10/site-packages (from stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (2.15.1)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.10/site-packages (from stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (4.65.0)\n",
            "Requirement already satisfied: rich in /usr/local/lib/python3.10/site-packages (from stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (13.7.0)\n",
            "Requirement already satisfied: psutil in /usr/local/lib/python3.10/site-packages (from stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (5.9.7)\n",
            "Requirement already satisfied: psycopg2-binary in /usr/local/lib/python3.10/site-packages (from wrds<4,>=3->finrl==0.3.6) (2.9.9)\n",
            "Requirement already satisfied: appdirs>=1.4.4 in /usr/local/lib/python3.10/site-packages (from yfinance<0.3,>=0.2->finrl==0.3.6) (1.4.4)\n",
            "Requirement already satisfied: frozendict>=2.3.4 in /usr/local/lib/python3.10/site-packages (from yfinance<0.3,>=0.2->finrl==0.3.6) (2.4.0)\n",
            "Requirement already satisfied: multitasking>=0.0.7 in /usr/local/lib/python3.10/site-packages (from yfinance<0.3,>=0.2->finrl==0.3.6) (0.0.11)\n",
            "Requirement already satisfied: html5lib>=1.1 in /usr/local/lib/python3.10/site-packages (from yfinance<0.3,>=0.2->finrl==0.3.6) (1.1)\n",
            "Requirement already satisfied: beautifulsoup4>=4.11.1 in /usr/local/lib/python3.10/site-packages (from yfinance<0.3,>=0.2->finrl==0.3.6) (4.12.2)\n",
            "Requirement already satisfied: peewee>=3.16.2 in /usr/local/lib/python3.10/site-packages (from yfinance<0.3,>=0.2->finrl==0.3.6) (3.17.0)\n",
            "Requirement already satisfied: lxml>=4.9.1 in /usr/local/lib/python3.10/site-packages (from yfinance<0.3,>=0.2->finrl==0.3.6) (5.0.1)\n",
            "Requirement already satisfied: gym in /usr/local/lib/python3.10/site-packages (from elegantrl@ git+https://github.com/AI4Finance-Foundation/ElegantRL.git#egg=elegantrl->finrl==0.3.6) (0.26.2)\n",
            "Requirement already satisfied: pycares>=4.0.0 in /usr/local/lib/python3.10/site-packages (from aiodns>=1.1.1->ccxt<4,>=3->finrl==0.3.6) (4.4.0)\n",
            "Requirement already satisfied: AutoROM.accept-rom-license in /usr/local/lib/python3.10/site-packages (from autorom[accept-rom-license]~=0.6.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (0.6.1)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/site-packages (from beautifulsoup4>=4.11.1->yfinance<0.3,>=0.2->finrl==0.3.6) (2.5)\n",
            "Requirement already satisfied: cffi>=1.12 in /usr/local/lib/python3.10/site-packages (from cryptography>=2.6.1->ccxt<4,>=3->finrl==0.3.6) (1.15.1)\n",
            "Requirement already satisfied: clarabel>=0.5.0 in /usr/local/lib/python3.10/site-packages (from cvxpy<2.0.0,>=1.1.19->pyportfolioopt<2,>=1->finrl==0.3.6) (0.6.0)\n",
            "Requirement already satisfied: osqp>=0.6.2 in /usr/local/lib/python3.10/site-packages (from cvxpy<2.0.0,>=1.1.19->pyportfolioopt<2,>=1->finrl==0.3.6) (0.6.3)\n",
            "Requirement already satisfied: pybind11 in /usr/local/lib/python3.10/site-packages (from cvxpy<2.0.0,>=1.1.19->pyportfolioopt<2,>=1->finrl==0.3.6) (2.11.1)\n",
            "Requirement already satisfied: scs>=3.0 in /usr/local/lib/python3.10/site-packages (from cvxpy<2.0.0,>=1.1.19->pyportfolioopt<2,>=1->finrl==0.3.6) (3.2.4.post1)\n",
            "Requirement already satisfied: ecos>=2 in /usr/local/lib/python3.10/site-packages (from cvxpy<2.0.0,>=1.1.19->pyportfolioopt<2,>=1->finrl==0.3.6) (2.0.12)\n",
            "Requirement already satisfied: pandas-datareader>=0.2 in /usr/local/lib/python3.10/site-packages (from empyrical>=0.5.0->pyfolio<0.10,>=0.9->finrl==0.3.6) (0.10.0)\n",
            "Requirement already satisfied: nvidia-ml-py>=11.450.129 in /usr/local/lib/python3.10/site-packages (from gpustat>=1.0.0->ray[default,tune]<3,>=2->finrl==0.3.6) (12.535.133)\n",
            "Requirement already satisfied: blessed>=1.17.1 in /usr/local/lib/python3.10/site-packages (from gpustat>=1.0.0->ray[default,tune]<3,>=2->finrl==0.3.6) (1.20.0)\n",
            "Requirement already satisfied: typing-extensions>=4.3.0 in /usr/local/lib/python3.10/site-packages (from gymnasium<0.30,>=0.28.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (4.9.0)\n",
            "Requirement already satisfied: farama-notifications>=0.0.1 in /usr/local/lib/python3.10/site-packages (from gymnasium<0.30,>=0.28.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (0.0.4)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.10/site-packages (from html5lib>=1.1->yfinance<0.3,>=0.2->finrl==0.3.6) (0.5.1)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.10/site-packages (from ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (5.1.1)\n",
            "Requirement already satisfied: matplotlib-inline in /usr/local/lib/python3.10/site-packages (from ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (0.1.6)\n",
            "Requirement already satisfied: traitlets>=5 in /usr/local/lib/python3.10/site-packages (from ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (5.14.1)\n",
            "Requirement already satisfied: stack-data in /usr/local/lib/python3.10/site-packages (from ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (0.6.3)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.10/site-packages (from ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (0.19.1)\n",
            "Requirement already satisfied: pygments>=2.4.0 in /usr/local/lib/python3.10/site-packages (from ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (2.17.2)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/site-packages (from ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (1.2.0)\n",
            "Requirement already satisfied: prompt-toolkit<3.1.0,>=3.0.41 in /usr/local/lib/python3.10/site-packages (from ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (3.0.43)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.10/site-packages (from ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (4.9.0)\n",
            "Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.10/site-packages (from matplotlib>=1.4.0->pyfolio<0.10,>=0.9->finrl==0.3.6) (1.4.5)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/site-packages (from matplotlib>=1.4.0->pyfolio<0.10,>=0.9->finrl==0.3.6) (1.2.0)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.10/site-packages (from matplotlib>=1.4.0->pyfolio<0.10,>=0.9->finrl==0.3.6) (0.12.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/site-packages (from matplotlib>=1.4.0->pyfolio<0.10,>=0.9->finrl==0.3.6) (4.47.0)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.10/site-packages (from matplotlib>=1.4.0->pyfolio<0.10,>=0.9->finrl==0.3.6) (3.1.1)\n",
            "Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/site-packages (from pydantic!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,<3->ray[default,tune]<3,>=2->finrl==0.3.6) (0.6.0)\n",
            "Requirement already satisfied: pydantic-core==2.14.6 in /usr/local/lib/python3.10/site-packages (from pydantic!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,<3->ray[default,tune]<3,>=2->finrl==0.3.6) (2.14.6)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/site-packages (from requests<3,>2->alpaca-trade-api<4,>=3->finrl==0.3.6) (3.4)\n",
            "Requirement already satisfied: ale-py~=0.8.1 in /usr/local/lib/python3.10/site-packages (from shimmy[atari]~=1.3.0->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (0.8.1)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/site-packages (from SQLAlchemy>=1.2.8->jqdatasdk<2,>=1->finrl==0.3.6) (3.0.3)\n",
            "Requirement already satisfied: werkzeug>=1.0.1 in /usr/local/lib/python3.10/site-packages (from tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (3.0.1)\n",
            "Requirement already satisfied: absl-py>=0.4 in /usr/local/lib/python3.10/site-packages (from tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (2.0.0)\n",
            "Requirement already satisfied: google-auth<3,>=1.6.3 in /usr/local/lib/python3.10/site-packages (from tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (2.26.1)\n",
            "Requirement already satisfied: markdown>=2.6.8 in /usr/local/lib/python3.10/site-packages (from tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (3.5.1)\n",
            "Requirement already satisfied: google-auth-oauthlib<2,>=0.5 in /usr/local/lib/python3.10/site-packages (from tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (1.2.0)\n",
            "Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in /usr/local/lib/python3.10/site-packages (from tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (0.7.2)\n",
            "Requirement already satisfied: ply<4.0,>=3.4 in /usr/local/lib/python3.10/site-packages (from thriftpy2>=0.3.9->jqdatasdk<2,>=1->finrl==0.3.6) (3.11)\n",
            "Requirement already satisfied: nvidia-cufft-cu12==11.0.2.54 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (11.0.2.54)\n",
            "Requirement already satisfied: nvidia-cuda-cupti-cu12==12.1.105 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (12.1.105)\n",
            "Requirement already satisfied: nvidia-cusparse-cu12==12.1.0.106 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (12.1.0.106)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (1.12)\n",
            "Requirement already satisfied: nvidia-cusolver-cu12==11.4.5.107 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (11.4.5.107)\n",
            "Requirement already satisfied: triton==2.1.0 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (2.1.0)\n",
            "Requirement already satisfied: nvidia-nccl-cu12==2.18.1 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (2.18.1)\n",
            "Requirement already satisfied: nvidia-cublas-cu12==12.1.3.1 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (12.1.3.1)\n",
            "Requirement already satisfied: nvidia-curand-cu12==10.3.2.106 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (10.3.2.106)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (3.2.1)\n",
            "Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.1.105 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (12.1.105)\n",
            "Requirement already satisfied: nvidia-nvtx-cu12==12.1.105 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (12.1.105)\n",
            "Requirement already satisfied: nvidia-cuda-runtime-cu12==12.1.105 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (12.1.105)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (3.1.2)\n",
            "Requirement already satisfied: nvidia-cudnn-cu12==8.9.2.26 in /usr/local/lib/python3.10/site-packages (from torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (8.9.2.26)\n",
            "Requirement already satisfied: nvidia-nvjitlink-cu12 in /usr/local/lib/python3.10/site-packages (from nvidia-cusolver-cu12==11.4.5.107->torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (12.3.101)\n",
            "Requirement already satisfied: distlib<1,>=0.3.6 in /usr/local/lib/python3.10/site-packages (from virtualenv<20.21.1,>=20.0.24->ray[default,tune]<3,>=2->finrl==0.3.6) (0.3.8)\n",
            "Requirement already satisfied: platformdirs<4,>=2.4 in /usr/local/lib/python3.10/site-packages (from virtualenv<20.21.1,>=20.0.24->ray[default,tune]<3,>=2->finrl==0.3.6) (3.11.0)\n",
            "Requirement already satisfied: gym-notices>=0.0.4 in /usr/local/lib/python3.10/site-packages (from gym->elegantrl@ git+https://github.com/AI4Finance-Foundation/ElegantRL.git#egg=elegantrl->finrl==0.3.6) (0.0.8)\n",
            "Requirement already satisfied: swig==4.* in /usr/local/lib/python3.10/site-packages (from gym->elegantrl@ git+https://github.com/AI4Finance-Foundation/ElegantRL.git#egg=elegantrl->finrl==0.3.6) (4.1.1.post1)\n",
            "Requirement already satisfied: box2d-py==2.3.5 in /usr/local/lib/python3.10/site-packages (from gym->elegantrl@ git+https://github.com/AI4Finance-Foundation/ElegantRL.git#egg=elegantrl->finrl==0.3.6) (2.3.5)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/site-packages (from jsonschema->ray[default,tune]<3,>=2->finrl==0.3.6) (2023.12.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/site-packages (from jsonschema->ray[default,tune]<3,>=2->finrl==0.3.6) (0.16.2)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/site-packages (from jsonschema->ray[default,tune]<3,>=2->finrl==0.3.6) (0.32.1)\n",
            "Requirement already satisfied: google-api-core<3.0.0,>=1.0.0 in /usr/local/lib/python3.10/site-packages (from opencensus->ray[default,tune]<3,>=2->finrl==0.3.6) (2.15.0)\n",
            "Requirement already satisfied: opencensus-context>=0.1.3 in /usr/local/lib/python3.10/site-packages (from opencensus->ray[default,tune]<3,>=2->finrl==0.3.6) (0.1.3)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/site-packages (from rich->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (3.0.0)\n",
            "Requirement already satisfied: importlib-resources in /usr/local/lib/python3.10/site-packages (from ale-py~=0.8.1->shimmy[atari]~=1.3.0->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (6.1.1)\n",
            "Requirement already satisfied: wcwidth>=0.1.4 in /usr/local/lib/python3.10/site-packages (from blessed>=1.17.1->gpustat>=1.0.0->ray[default,tune]<3,>=2->finrl==0.3.6) (0.2.13)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.10/site-packages (from cffi>=1.12->cryptography>=2.6.1->ccxt<4,>=3->finrl==0.3.6) (2.21)\n",
            "Requirement already satisfied: googleapis-common-protos<2.0.dev0,>=1.56.2 in /usr/local/lib/python3.10/site-packages (from google-api-core<3.0.0,>=1.0.0->opencensus->ray[default,tune]<3,>=2->finrl==0.3.6) (1.62.0)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.10/site-packages (from google-auth<3,>=1.6.3->tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (5.3.2)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.10/site-packages (from google-auth<3,>=1.6.3->tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (4.9)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.10/site-packages (from google-auth<3,>=1.6.3->tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (0.3.0)\n",
            "Requirement already satisfied: requests-oauthlib>=0.7.0 in /usr/local/lib/python3.10/site-packages (from google-auth-oauthlib<2,>=0.5->tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (1.3.1)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.3 in /usr/local/lib/python3.10/site-packages (from jedi>=0.16->ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (0.8.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/site-packages (from markdown-it-py>=2.2.0->rich->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (0.1.2)\n",
            "Requirement already satisfied: qdldl in /usr/local/lib/python3.10/site-packages (from osqp>=0.6.2->cvxpy<2.0.0,>=1.1.19->pyportfolioopt<2,>=1->finrl==0.3.6) (0.1.7.post0)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.10/site-packages (from pexpect>4.3->ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (0.7.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib/python3.10/site-packages (from werkzeug>=1.0.1->tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (2.1.3)\n",
            "Requirement already satisfied: pure-eval in /usr/local/lib/python3.10/site-packages (from stack-data->ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (0.2.2)\n",
            "Requirement already satisfied: asttokens>=2.1.0 in /usr/local/lib/python3.10/site-packages (from stack-data->ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (2.4.1)\n",
            "Requirement already satisfied: executing>=1.2.0 in /usr/local/lib/python3.10/site-packages (from stack-data->ipython>=3.2.3->pyfolio<0.10,>=0.9->finrl==0.3.6) (2.0.1)\n",
            "Requirement already satisfied: mpmath>=0.19 in /usr/local/lib/python3.10/site-packages (from sympy->torch>=1.13->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (1.3.0)\n",
            "Requirement already satisfied: pyasn1<0.6.0,>=0.4.6 in /usr/local/lib/python3.10/site-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (0.5.1)\n",
            "Requirement already satisfied: oauthlib>=3.0.0 in /usr/local/lib/python3.10/site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<2,>=0.5->tensorboard>=2.9.1->stable-baselines3[extra]>=2.0.0a5->finrl==0.3.6) (3.2.2)\n",
            "\u001b[33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\u001b[0m\u001b[33m\n",
            "\u001b[0m"
          ]
        }
      ],
      "source": [
        "## install finrl library\n",
        "!pip install wrds\n",
        "!pip install swig\n",
        "!pip install -q condacolab\n",
        "import condacolab\n",
        "condacolab.install()\n",
        "!apt-get update -y -qq && apt-get install -y -qq cmake libopenmpi-dev python3-dev zlib1g-dev libgl1-mesa-glx swig\n",
        "!pip install git+https://github.com/AI4Finance-Foundation/FinRL.git"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 211,
      "metadata": {
        "id": "DDsLT5a8ea4L"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "--6Kx8I21erH"
      },
      "source": [
        "## Import related modules"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 212,
      "metadata": {
        "id": "H7I7zsyYfoLJ"
      },
      "outputs": [],
      "source": [
        "from finrl.config_tickers import DOW_30_TICKER\n",
        "from finrl.config import INDICATORS\n",
        "from finrl.meta.env_stock_trading.env_stocktrading_np import StockTradingEnv\n",
        "from finrl.meta.env_stock_trading.env_stock_papertrading import AlpacaPaperTrading\n",
        "from finrl.meta.data_processor import DataProcessor\n",
        "from finrl.plot import backtest_stats, backtest_plot, get_daily_return, get_baseline\n",
        "\n",
        "import numpy as np\n",
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0EVJIQUR6_fu"
      },
      "source": [
        "## PPO"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 213,
      "metadata": {
        "id": "-EYx40S84tzo"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "import time\n",
        "import gym\n",
        "import numpy as np\n",
        "import numpy.random as rd\n",
        "import torch\n",
        "import torch.nn as nn\n",
        "from copy import deepcopy\n",
        "from torch import Tensor\n",
        "from torch.distributions.normal import Normal\n",
        "\n",
        "\n",
        "class ActorPPO(nn.Module):\n",
        "    def __init__(self, dims: [int], state_dim: int, action_dim: int):\n",
        "        super().__init__()\n",
        "        self.net = build_mlp(dims=[state_dim, *dims, action_dim])\n",
        "        self.action_std_log = nn.Parameter(torch.zeros((1, action_dim)), requires_grad=True)  # trainable parameter\n",
        "\n",
        "    def forward(self, state: Tensor) -> Tensor:\n",
        "        return self.net(state).tanh()  # action.tanh()\n",
        "\n",
        "    def get_action(self, state: Tensor) -> (Tensor, Tensor):  # for exploration\n",
        "        action_avg = self.net(state)\n",
        "        action_std = self.action_std_log.exp()\n",
        "\n",
        "        dist = Normal(action_avg, action_std)\n",
        "        action = dist.sample()\n",
        "        logprob = dist.log_prob(action).sum(1)\n",
        "        return action, logprob\n",
        "\n",
        "    def get_logprob_entropy(self, state: Tensor, action: Tensor) -> (Tensor, Tensor):\n",
        "        action_avg = self.net(state)\n",
        "        action_std = self.action_std_log.exp()\n",
        "\n",
        "        dist = Normal(action_avg, action_std)\n",
        "        logprob = dist.log_prob(action).sum(1)\n",
        "        entropy = dist.entropy().sum(1)\n",
        "        return logprob, entropy\n",
        "\n",
        "    @staticmethod\n",
        "    def convert_action_for_env(action: Tensor) -> Tensor:\n",
        "        return action.tanh()\n",
        "\n",
        "\n",
        "class CriticPPO(nn.Module):\n",
        "    def __init__(self, dims: [int], state_dim: int, _action_dim: int):\n",
        "        super().__init__()\n",
        "        self.net = build_mlp(dims=[state_dim, *dims, 1])\n",
        "\n",
        "    def forward(self, state: Tensor) -> Tensor:\n",
        "        return self.net(state)  # advantage value\n",
        "\n",
        "\n",
        "def build_mlp(dims: [int]) -> nn.Sequential:  # MLP (MultiLayer Perceptron)\n",
        "    net_list = []\n",
        "    for i in range(len(dims) - 1):\n",
        "        net_list.extend([nn.Linear(dims[i], dims[i + 1]), nn.ReLU()])\n",
        "    del net_list[-1]  # remove the activation of output layer\n",
        "    return nn.Sequential(*net_list)\n",
        "\n",
        "\n",
        "class Config:\n",
        "    def __init__(self, agent_class=None, env_class=None, env_args=None):\n",
        "        self.env_class = env_class  # env = env_class(**env_args)\n",
        "        self.env_args = env_args  # env = env_class(**env_args)\n",
        "\n",
        "        if env_args is None:  # dummy env_args\n",
        "            env_args = {'env_name': None, 'state_dim': None, 'action_dim': None, 'if_discrete': None}\n",
        "        self.env_name = env_args['env_name']  # the name of environment. Be used to set 'cwd'.\n",
        "        self.state_dim = env_args['state_dim']  # vector dimension (feature number) of state\n",
        "        self.action_dim = env_args['action_dim']  # vector dimension (feature number) of action\n",
        "        self.if_discrete = env_args['if_discrete']  # discrete or continuous action space\n",
        "\n",
        "        self.agent_class = agent_class  # agent = agent_class(...)\n",
        "\n",
        "        '''Arguments for reward shaping'''\n",
        "        self.gamma = 0.99  # discount factor of future rewards\n",
        "        self.reward_scale = 1.0  # an approximate target reward usually be closed to 256\n",
        "\n",
        "        '''Arguments for training'''\n",
        "        self.gpu_id = int(0)  # `int` means the ID of single GPU, -1 means CPU\n",
        "        self.net_dims = (64, 32)  # the middle layer dimension of MLP (MultiLayer Perceptron)\n",
        "        self.learning_rate = 6e-5  # 2 ** -14 ~= 6e-5\n",
        "        self.soft_update_tau = 5e-3  # 2 ** -8 ~= 5e-3\n",
        "        self.batch_size = int(128)  # num of transitions sampled from replay buffer.\n",
        "        self.horizon_len = int(2000)  # collect horizon_len step while exploring, then update network\n",
        "        self.buffer_size = None  # ReplayBuffer size. Empty the ReplayBuffer for on-policy.\n",
        "        self.repeat_times = 8.0  # repeatedly update network using ReplayBuffer to keep critic's loss small\n",
        "\n",
        "        '''Arguments for evaluate'''\n",
        "        self.cwd = None  # current working directory to save model. None means set automatically\n",
        "        self.break_step = +np.inf  # break training if 'total_step > break_step'\n",
        "        self.eval_times = int(32)  # number of times that get episodic cumulative return\n",
        "        self.eval_per_step = int(2e4)  # evaluate the agent per training steps\n",
        "\n",
        "    def init_before_training(self):\n",
        "        if self.cwd is None:  # set cwd (current working directory) for saving model\n",
        "            self.cwd = f'./{self.env_name}_{self.agent_class.__name__[5:]}'\n",
        "        os.makedirs(self.cwd, exist_ok=True)\n",
        "\n",
        "\n",
        "def get_gym_env_args(env, if_print: bool) -> dict:\n",
        "    if {'unwrapped', 'observation_space', 'action_space', 'spec'}.issubset(dir(env)):  # isinstance(env, gym.Env):\n",
        "        env_name = env.unwrapped.spec.id\n",
        "        state_shape = env.observation_space.shape\n",
        "        state_dim = state_shape[0] if len(state_shape) == 1 else state_shape  # sometimes state_dim is a list\n",
        "\n",
        "        if_discrete = isinstance(env.action_space, gym.spaces.Discrete)\n",
        "        if if_discrete:  # make sure it is discrete action space\n",
        "            action_dim = env.action_space.n\n",
        "        elif isinstance(env.action_space, gym.spaces.Box):  # make sure it is continuous action space\n",
        "            action_dim = env.action_space.shape[0]\n",
        "\n",
        "    env_args = {'env_name': env_name, 'state_dim': state_dim, 'action_dim': action_dim, 'if_discrete': if_discrete}\n",
        "    print(f\"env_args = {repr(env_args)}\") if if_print else None\n",
        "    return env_args\n",
        "\n",
        "\n",
        "def kwargs_filter(function, kwargs: dict) -> dict:\n",
        "    import inspect\n",
        "    sign = inspect.signature(function).parameters.values()\n",
        "    sign = {val.name for val in sign}\n",
        "    common_args = sign.intersection(kwargs.keys())\n",
        "    return {key: kwargs[key] for key in common_args}  # filtered kwargs\n",
        "\n",
        "\n",
        "def build_env(env_class=None, env_args=None):\n",
        "    if env_class.__module__ == 'gym.envs.registration':  # special rule\n",
        "        env = env_class(id=env_args['env_name'])\n",
        "    else:\n",
        "        env = env_class(**kwargs_filter(env_class.__init__, env_args.copy()))\n",
        "    for attr_str in ('env_name', 'state_dim', 'action_dim', 'if_discrete'):\n",
        "        setattr(env, attr_str, env_args[attr_str])\n",
        "    return env\n",
        "\n",
        "\n",
        "class AgentBase:\n",
        "    def __init__(self, net_dims: [int], state_dim: int, action_dim: int, gpu_id: int = 0, args: Config = Config()):\n",
        "        self.state_dim = state_dim\n",
        "        self.action_dim = action_dim\n",
        "\n",
        "        self.gamma = args.gamma\n",
        "        self.batch_size = args.batch_size\n",
        "        self.repeat_times = args.repeat_times\n",
        "        self.reward_scale = args.reward_scale\n",
        "        self.soft_update_tau = args.soft_update_tau\n",
        "\n",
        "        self.states = None  # assert self.states == (1, state_dim)\n",
        "        self.device = torch.device(f\"cuda:{gpu_id}\" if (torch.cuda.is_available() and (gpu_id >= 0)) else \"cpu\")\n",
        "\n",
        "        act_class = getattr(self, \"act_class\", None)\n",
        "        cri_class = getattr(self, \"cri_class\", None)\n",
        "        self.act = self.act_target = act_class(net_dims, state_dim, action_dim).to(self.device)\n",
        "        self.cri = self.cri_target = cri_class(net_dims, state_dim, action_dim).to(self.device) \\\n",
        "            if cri_class else self.act\n",
        "\n",
        "        self.act_optimizer = torch.optim.Adam(self.act.parameters(), args.learning_rate)\n",
        "        self.cri_optimizer = torch.optim.Adam(self.cri.parameters(), args.learning_rate) \\\n",
        "            if cri_class else self.act_optimizer\n",
        "\n",
        "        self.criterion = torch.nn.SmoothL1Loss()\n",
        "\n",
        "    @staticmethod\n",
        "    def optimizer_update(optimizer, objective: Tensor):\n",
        "        optimizer.zero_grad()\n",
        "        objective.backward()\n",
        "        optimizer.step()\n",
        "\n",
        "    @staticmethod\n",
        "    def soft_update(target_net: torch.nn.Module, current_net: torch.nn.Module, tau: float):\n",
        "        for tar, cur in zip(target_net.parameters(), current_net.parameters()):\n",
        "            tar.data.copy_(cur.data * tau + tar.data * (1.0 - tau))\n",
        "\n",
        "\n",
        "class AgentPPO(AgentBase):\n",
        "    def __init__(self, net_dims: [int], state_dim: int, action_dim: int, gpu_id: int = 0, args: Config = Config()):\n",
        "        self.if_off_policy = False\n",
        "        self.act_class = getattr(self, \"act_class\", ActorPPO)\n",
        "        self.cri_class = getattr(self, \"cri_class\", CriticPPO)\n",
        "        AgentBase.__init__(self, net_dims, state_dim, action_dim, gpu_id, args)\n",
        "\n",
        "        self.ratio_clip = getattr(args, \"ratio_clip\", 0.25)  # `ratio.clamp(1 - clip, 1 + clip)`\n",
        "        self.lambda_gae_adv = getattr(args, \"lambda_gae_adv\", 0.95)  # could be 0.80~0.99\n",
        "        self.lambda_entropy = getattr(args, \"lambda_entropy\", 0.01)  # could be 0.00~0.10\n",
        "        self.lambda_entropy = torch.tensor(self.lambda_entropy, dtype=torch.float32, device=self.device)\n",
        "\n",
        "    def explore_env(self, env, horizon_len: int) -> [Tensor]:\n",
        "        states = torch.zeros((horizon_len, self.state_dim), dtype=torch.float32).to(self.device)\n",
        "        actions = torch.zeros((horizon_len, self.action_dim), dtype=torch.float32).to(self.device)\n",
        "        logprobs = torch.zeros(horizon_len, dtype=torch.float32).to(self.device)\n",
        "        rewards = torch.zeros(horizon_len, dtype=torch.float32).to(self.device)\n",
        "        dones = torch.zeros(horizon_len, dtype=torch.bool).to(self.device)\n",
        "\n",
        "        ary_state = self.states[0]\n",
        "\n",
        "        get_action = self.act.get_action\n",
        "        convert = self.act.convert_action_for_env\n",
        "        for i in range(horizon_len):\n",
        "            #state = torch.as_tensor(ary_state, dtype=torch.float32, device=self.device) # HSG added unsqueeze\n",
        "            state = torch.as_tensor(ary_state, dtype=torch.float32, device=self.device).unsqueeze(0)\n",
        "            action, logprob = [t.squeeze(0) for t in get_action(state.unsqueeze(0))[:2]]\n",
        "\n",
        "            ary_action = convert(action).detach().cpu().numpy()\n",
        "            #ary_state, reward, done, _ = env.step(ary_action)  # HSG\n",
        "            ary_state, reward, done, _, _ = env.step(ary_action)\n",
        "            if done:\n",
        "                ary_state = env.reset()\n",
        "\n",
        "            states[i] = state\n",
        "            actions[i] = action\n",
        "            logprobs[i] = logprob\n",
        "            rewards[i] = reward\n",
        "            dones[i] = done\n",
        "\n",
        "        self.states[0] = ary_state\n",
        "        rewards = (rewards * self.reward_scale).unsqueeze(1)\n",
        "        undones = (1 - dones.type(torch.float32)).unsqueeze(1)\n",
        "        return states, actions, logprobs, rewards, undones\n",
        "\n",
        "    def update_net(self, buffer) -> [float]:\n",
        "        with torch.no_grad():\n",
        "            states, actions, logprobs, rewards, undones = buffer\n",
        "            buffer_size = states.shape[0]\n",
        "\n",
        "            '''get advantages reward_sums'''\n",
        "            bs = 2 ** 10  # set a smaller 'batch_size' when out of GPU memory.\n",
        "            values = [self.cri(states[i:i + bs]) for i in range(0, buffer_size, bs)]\n",
        "            values = torch.cat(values, dim=0).squeeze(1)  # values.shape == (buffer_size, )\n",
        "\n",
        "            advantages = self.get_advantages(rewards, undones, values)  # advantages.shape == (buffer_size, )\n",
        "            reward_sums = advantages + values  # reward_sums.shape == (buffer_size, )\n",
        "            del rewards, undones, values\n",
        "\n",
        "            advantages = (advantages - advantages.mean()) / (advantages.std(dim=0) + 1e-5)\n",
        "        assert logprobs.shape == advantages.shape == reward_sums.shape == (buffer_size,)\n",
        "\n",
        "        '''update network'''\n",
        "        obj_critics = 0.0\n",
        "        obj_actors = 0.0\n",
        "\n",
        "        update_times = int(buffer_size * self.repeat_times / self.batch_size)\n",
        "        assert update_times >= 1\n",
        "        for _ in range(update_times):\n",
        "            indices = torch.randint(buffer_size, size=(self.batch_size,), requires_grad=False)\n",
        "            state = states[indices]\n",
        "            action = actions[indices]\n",
        "            logprob = logprobs[indices]\n",
        "            advantage = advantages[indices]\n",
        "            reward_sum = reward_sums[indices]\n",
        "\n",
        "            value = self.cri(state).squeeze(1)  # critic network predicts the reward_sum (Q value) of state\n",
        "            obj_critic = self.criterion(value, reward_sum)\n",
        "            self.optimizer_update(self.cri_optimizer, obj_critic)\n",
        "\n",
        "            new_logprob, obj_entropy = self.act.get_logprob_entropy(state, action)\n",
        "            ratio = (new_logprob - logprob.detach()).exp()\n",
        "            surrogate1 = advantage * ratio\n",
        "            surrogate2 = advantage * ratio.clamp(1 - self.ratio_clip, 1 + self.ratio_clip)\n",
        "            obj_surrogate = torch.min(surrogate1, surrogate2).mean()\n",
        "\n",
        "            obj_actor = obj_surrogate + obj_entropy.mean() * self.lambda_entropy\n",
        "            self.optimizer_update(self.act_optimizer, -obj_actor)\n",
        "\n",
        "            obj_critics += obj_critic.item()\n",
        "            obj_actors += obj_actor.item()\n",
        "        a_std_log = getattr(self.act, 'a_std_log', torch.zeros(1)).mean()\n",
        "        return obj_critics / update_times, obj_actors / update_times, a_std_log.item()\n",
        "\n",
        "    def get_advantages(self, rewards: Tensor, undones: Tensor, values: Tensor) -> Tensor:\n",
        "        advantages = torch.empty_like(values)  # advantage value\n",
        "\n",
        "        masks = undones * self.gamma\n",
        "        horizon_len = rewards.shape[0]\n",
        "\n",
        "        next_state = torch.tensor(self.states, dtype=torch.float32).to(self.device)\n",
        "        next_value = self.cri(next_state).detach()[0, 0]\n",
        "\n",
        "        advantage = 0  # last_gae_lambda\n",
        "        for t in range(horizon_len - 1, -1, -1):\n",
        "            delta = rewards[t] + masks[t] * next_value - values[t]\n",
        "            advantages[t] = advantage = delta + masks[t] * self.lambda_gae_adv * advantage\n",
        "            next_value = values[t]\n",
        "        return advantages\n",
        "\n",
        "\n",
        "class PendulumEnv(gym.Wrapper):  # a demo of custom gym env\n",
        "    def __init__(self):\n",
        "        gym.logger.set_level(40)  # Block warning\n",
        "        gym_env_name = \"Pendulum-v0\" if gym.__version__ < '0.18.0' else \"Pendulum-v1\"\n",
        "        super().__init__(env=gym.make(gym_env_name))\n",
        "\n",
        "        '''the necessary env information when you design a custom env'''\n",
        "        self.env_name = gym_env_name  # the name of this env.\n",
        "        self.state_dim = self.observation_space.shape[0]  # feature number of state\n",
        "        self.action_dim = self.action_space.shape[0]  # feature number of action\n",
        "        self.if_discrete = False  # discrete action or continuous action\n",
        "\n",
        "    def reset(self) -> np.ndarray:  # reset the agent in env\n",
        "        return self.env.reset()\n",
        "\n",
        "    def step(self, action: np.ndarray) -> (np.ndarray, float, bool, dict):  # agent interacts in env\n",
        "        # We suggest that adjust action space to (-1, +1) when designing a custom env.\n",
        "        #state, reward, done, info_dict = self.env.step(action * 2) # HSG\n",
        "        state, reward, done, _, info_dict = self.env.step(action * 2)\n",
        "        #done = done.all()  # HSG added line\n",
        "        return state.reshape(self.state_dim), float(reward), done, info_dict\n",
        "\n",
        "\n",
        "def train_agent(args: Config):\n",
        "    args.init_before_training()\n",
        "\n",
        "    env = build_env(args.env_class, args.env_args)\n",
        "    agent = args.agent_class(args.net_dims, args.state_dim, args.action_dim, gpu_id=args.gpu_id, args=args)\n",
        "    #agent.states = env.reset()[np.newaxis, :]\n",
        "    env_reset = env.reset()[:-1] # HSG - exclude last state in env.reset() as it is None.\n",
        "    agent.states = env_reset[0][np.newaxis, :]\n",
        "\n",
        "    evaluator = Evaluator(eval_env=build_env(args.env_class, args.env_args),\n",
        "                          eval_per_step=args.eval_per_step,\n",
        "                          eval_times=args.eval_times,\n",
        "                          cwd=args.cwd)\n",
        "    torch.set_grad_enabled(False)\n",
        "    while True: # start training\n",
        "        buffer_items = agent.explore_env(env, args.horizon_len)\n",
        "\n",
        "        torch.set_grad_enabled(True)\n",
        "        logging_tuple = agent.update_net(buffer_items)\n",
        "        torch.set_grad_enabled(False)\n",
        "\n",
        "        evaluator.evaluate_and_save(agent.act, args.horizon_len, logging_tuple)\n",
        "        if (evaluator.total_step > args.break_step) or os.path.exists(f\"{args.cwd}/stop\"):\n",
        "            torch.save(agent.act.state_dict(), args.cwd + '/actor.pth')\n",
        "            break  # stop training when reach `break_step` or `mkdir cwd/stop`\n",
        "\n",
        "\n",
        "def render_agent(env_class, env_args: dict, net_dims: [int], agent_class, actor_path: str, render_times: int = 8):\n",
        "    env = build_env(env_class, env_args)\n",
        "\n",
        "    state_dim = env_args['state_dim']\n",
        "    action_dim = env_args['action_dim']\n",
        "    agent = agent_class(net_dims, state_dim, action_dim, gpu_id=-1)\n",
        "    actor = agent.act\n",
        "\n",
        "    print(f\"| render and load actor from: {actor_path}\")\n",
        "    actor.load_state_dict(torch.load(actor_path, map_location=lambda storage, loc: storage))\n",
        "    for i in range(render_times):\n",
        "        cumulative_reward, episode_step = get_rewards_and_steps(env, actor, if_render=True)\n",
        "        print(f\"|{i:4}  cumulative_reward {cumulative_reward:9.3f}  episode_step {episode_step:5.0f}\")\n",
        "\n",
        "\n",
        "class Evaluator:\n",
        "    def __init__(self, eval_env, eval_per_step: int = 1e4, eval_times: int = 8, cwd: str = '.'):\n",
        "        self.cwd = cwd\n",
        "        self.env_eval = eval_env\n",
        "        self.eval_step = 0\n",
        "        self.total_step = 0\n",
        "        self.start_time = time.time()\n",
        "        self.eval_times = eval_times  # number of times that get episodic cumulative return\n",
        "        self.eval_per_step = eval_per_step  # evaluate the agent per training steps\n",
        "\n",
        "        self.recorder = []\n",
        "        print(f\"\\n| `step`: Number of samples, or total training steps, or running times of `env.step()`.\"\n",
        "              f\"\\n| `time`: Time spent from the start of training to this moment.\"\n",
        "              f\"\\n| `avgR`: Average value of cumulative rewards, which is the sum of rewards in an episode.\"\n",
        "              f\"\\n| `stdR`: Standard dev of cumulative rewards, which is the sum of rewards in an episode.\"\n",
        "              f\"\\n| `avgS`: Average of steps in an episode.\"\n",
        "              f\"\\n| `objC`: Objective of Critic network. Or call it loss function of critic network.\"\n",
        "              f\"\\n| `objA`: Objective of Actor network. It is the average Q value of the critic network.\"\n",
        "              f\"\\n| {'step':>8}  {'time':>8}  | {'avgR':>8}  {'stdR':>6}  {'avgS':>6}  | {'objC':>8}  {'objA':>8}\")\n",
        "\n",
        "    def evaluate_and_save(self, actor, horizon_len: int, logging_tuple: tuple):\n",
        "        self.total_step += horizon_len\n",
        "        if self.eval_step + self.eval_per_step > self.total_step:\n",
        "            return\n",
        "        self.eval_step = self.total_step\n",
        "\n",
        "        rewards_steps_ary = [get_rewards_and_steps(self.env_eval, actor) for _ in range(self.eval_times)]\n",
        "        rewards_steps_ary = np.array(rewards_steps_ary, dtype=np.float32)\n",
        "        avg_r = rewards_steps_ary[:, 0].mean()  # average of cumulative rewards\n",
        "        std_r = rewards_steps_ary[:, 0].std()  # std of cumulative rewards\n",
        "        avg_s = rewards_steps_ary[:, 1].mean()  # average of steps in an episode\n",
        "\n",
        "        used_time = time.time() - self.start_time\n",
        "        self.recorder.append((self.total_step, used_time, avg_r))\n",
        "\n",
        "        print(f\"| {self.total_step:8.2e}  {used_time:8.0f}  \"\n",
        "              f\"| {avg_r:8.2f}  {std_r:6.2f}  {avg_s:6.0f}  \"\n",
        "              f\"| {logging_tuple[0]:8.2f}  {logging_tuple[1]:8.2f}\")\n",
        "\n",
        "\n",
        "def get_rewards_and_steps(env, actor, if_render: bool = False) -> (float, int):  # cumulative_rewards and episode_steps\n",
        "    device = next(actor.parameters()).device  # net.parameters() is a Python generator.\n",
        "\n",
        "    state = env.reset()\n",
        "    episode_steps = 0\n",
        "    cumulative_returns = 0.0  # sum of rewards in an episode\n",
        "    for episode_steps in range(12345):\n",
        "        tensor_state = torch.as_tensor(state, dtype=torch.float32, device=device).unsqueeze(0)\n",
        "        tensor_action = actor(tensor_state)\n",
        "        action = tensor_action.detach().cpu().numpy()[0]  # not need detach(), because using torch.no_grad() outside\n",
        "        state, reward, done, _ = env.step(action)\n",
        "        cumulative_returns += reward\n",
        "\n",
        "        if if_render:\n",
        "            env.render()\n",
        "        if done:\n",
        "            break\n",
        "    return cumulative_returns, episode_steps + 1"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9tzAw9k26nAC"
      },
      "source": [
        "##DRL Agent Class"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 214,
      "metadata": {
        "id": "pwCbbocm6PHM"
      },
      "outputs": [],
      "source": [
        "from __future__ import annotations\n",
        "\n",
        "import torch\n",
        "# from elegantrl.agents import AgentA2C\n",
        "\n",
        "MODELS = {\"ppo\": AgentPPO}\n",
        "OFF_POLICY_MODELS = [\"ddpg\", \"td3\", \"sac\"]\n",
        "ON_POLICY_MODELS = [\"ppo\"]\n",
        "# MODEL_KWARGS = {x: config.__dict__[f\"{x.upper()}_PARAMS\"] for x in MODELS.keys()}\n",
        "#\n",
        "# NOISE = {\n",
        "#     \"normal\": NormalActionNoise,\n",
        "#     \"ornstein_uhlenbeck\": OrnsteinUhlenbeckActionNoise,\n",
        "# }\n",
        "\n",
        "\n",
        "class DRLAgent:\n",
        "    \"\"\"Implementations of DRL algorithms\n",
        "    Attributes\n",
        "    ----------\n",
        "        env: gym environment class\n",
        "            user-defined class\n",
        "    Methods\n",
        "    -------\n",
        "        get_model()\n",
        "            setup DRL algorithms\n",
        "        train_model()\n",
        "            train DRL algorithms in a train dataset\n",
        "            and output the trained model\n",
        "        DRL_prediction()\n",
        "            make a prediction in a test dataset and get results\n",
        "    \"\"\"\n",
        "\n",
        "    def __init__(self, env, price_array, tech_array, turbulence_array):\n",
        "        self.env = env\n",
        "        self.price_array = price_array\n",
        "        self.tech_array = tech_array\n",
        "        self.turbulence_array = turbulence_array\n",
        "\n",
        "    def get_model(self, model_name, model_kwargs):\n",
        "        env_config = {\n",
        "            \"price_array\": self.price_array,\n",
        "            \"tech_array\": self.tech_array,\n",
        "            \"turbulence_array\": self.turbulence_array,\n",
        "            \"if_train\": True,\n",
        "        }\n",
        "        environment = self.env(config=env_config)\n",
        "        env_args = {'config': env_config,\n",
        "              'env_name': environment.env_name,\n",
        "              'state_dim': environment.state_dim,\n",
        "              'action_dim': environment.action_dim,\n",
        "              'if_discrete': False}\n",
        "        agent = MODELS[model_name]\n",
        "        if model_name not in MODELS:\n",
        "            raise NotImplementedError(\"NotImplementedError\")\n",
        "        model = Config(agent_class=agent, env_class=self.env, env_args=env_args)\n",
        "        model.if_off_policy = model_name in OFF_POLICY_MODELS\n",
        "        if model_kwargs is not None:\n",
        "            try:\n",
        "                model.learning_rate = model_kwargs[\"learning_rate\"]\n",
        "                model.batch_size = model_kwargs[\"batch_size\"]\n",
        "                model.gamma = model_kwargs[\"gamma\"]\n",
        "                model.seed = model_kwargs[\"seed\"]\n",
        "                model.net_dims = model_kwargs[\"net_dimension\"]\n",
        "                model.target_step = model_kwargs[\"target_step\"]\n",
        "                model.eval_gap = model_kwargs[\"eval_gap\"]\n",
        "                model.eval_times = model_kwargs[\"eval_times\"]\n",
        "            except BaseException:\n",
        "                raise ValueError(\n",
        "                    \"Fail to read arguments, please check 'model_kwargs' input.\"\n",
        "                )\n",
        "        return model\n",
        "\n",
        "    def train_model(self, model, cwd, total_timesteps=5000):\n",
        "        model.cwd = cwd\n",
        "        model.break_step = total_timesteps\n",
        "        train_agent(model)\n",
        "\n",
        "    @staticmethod\n",
        "    def DRL_prediction(model_name, cwd, net_dimension, environment):\n",
        "        if model_name not in MODELS:\n",
        "            raise NotImplementedError(\"NotImplementedError\")\n",
        "        agent_class = MODELS[model_name]\n",
        "        environment.env_num = 1\n",
        "        agent = agent_class(net_dimension, environment.state_dim, environment.action_dim)\n",
        "        actor = agent.act\n",
        "        # load agent\n",
        "        try:\n",
        "            cwd = cwd + '/actor.pth'\n",
        "            print(f\"| load actor from: {cwd}\")\n",
        "            actor.load_state_dict(torch.load(cwd, map_location=lambda storage, loc: storage))\n",
        "            act = actor\n",
        "            device = agent.device\n",
        "        except BaseException:\n",
        "            raise ValueError(\"Fail to load agent!\")\n",
        "\n",
        "        # test on the testing env\n",
        "        _torch = torch\n",
        "        state = environment.reset()\n",
        "        episode_returns = []  # the cumulative_return / initial_account\n",
        "        episode_total_assets = [environment.initial_total_asset]\n",
        "        with _torch.no_grad():\n",
        "            for i in range(environment.max_step):\n",
        "                s_tensor = _torch.as_tensor((state,), device=device)\n",
        "                a_tensor = act(s_tensor)  # action_tanh = act.forward()\n",
        "                action = (\n",
        "                    a_tensor.detach().cpu().numpy()[0]\n",
        "                )  # not need detach(), because with torch.no_grad() outside\n",
        "                state, reward, done, _ = environment.step(action)\n",
        "\n",
        "                total_asset = (\n",
        "                    environment.amount\n",
        "                    + (\n",
        "                        environment.price_ary[environment.day] * environment.stocks\n",
        "                    ).sum()\n",
        "                )\n",
        "                episode_total_assets.append(total_asset)\n",
        "                episode_return = total_asset / environment.initial_total_asset\n",
        "                episode_returns.append(episode_return)\n",
        "                if done:\n",
        "                    break\n",
        "        print(\"Test Finished!\")\n",
        "        # return episode total_assets on testing data\n",
        "        print(\"episode_return\", episode_return)\n",
        "        return episode_total_assets\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zjLda8No6pvI"
      },
      "source": [
        "## Train & Test Functions"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 215,
      "metadata": {
        "id": "j8-e03ev32oz"
      },
      "outputs": [],
      "source": [
        "from __future__ import annotations\n",
        "\n",
        "from finrl.config import ERL_PARAMS\n",
        "from finrl.config import INDICATORS\n",
        "from finrl.config import RLlib_PARAMS\n",
        "from finrl.config import SAC_PARAMS\n",
        "from finrl.config import TRAIN_END_DATE\n",
        "from finrl.config import TRAIN_START_DATE\n",
        "from finrl.config_tickers import DOW_30_TICKER\n",
        "from finrl.meta.data_processor import DataProcessor\n",
        "\n",
        "# construct environment\n",
        "\n",
        "\n",
        "def train(\n",
        "    start_date,\n",
        "    end_date,\n",
        "    ticker_list,\n",
        "    data_source,\n",
        "    time_interval,\n",
        "    technical_indicator_list,\n",
        "    drl_lib,\n",
        "    env,\n",
        "    model_name,\n",
        "    if_vix=True,\n",
        "    **kwargs,\n",
        "):\n",
        "    # download data\n",
        "    dp = DataProcessor(data_source, **kwargs)\n",
        "    data = dp.download_data(ticker_list, start_date, end_date, time_interval)\n",
        "    data = dp.clean_data(data)\n",
        "    data = dp.add_technical_indicator(data, technical_indicator_list)\n",
        "    if if_vix:\n",
        "        data = dp.add_vix(data)\n",
        "    else:\n",
        "        data = dp.add_turbulence(data)\n",
        "    price_array, tech_array, turbulence_array = dp.df_to_array(data, if_vix)\n",
        "    env_config = {\n",
        "        \"price_array\": price_array,\n",
        "        \"tech_array\": tech_array,\n",
        "        \"turbulence_array\": turbulence_array,\n",
        "        \"if_train\": True,\n",
        "    }\n",
        "    env_instance = env(config=env_config)\n",
        "\n",
        "    # read parameters\n",
        "    cwd = kwargs.get(\"cwd\", \"./\" + str(model_name))\n",
        "\n",
        "    if drl_lib == \"elegantrl\":\n",
        "        DRLAgent_erl = DRLAgent\n",
        "        break_step = kwargs.get(\"break_step\", 1e6)\n",
        "        erl_params = kwargs.get(\"erl_params\")\n",
        "        agent = DRLAgent_erl(\n",
        "            env=env,\n",
        "            price_array=price_array,\n",
        "            tech_array=tech_array,\n",
        "            turbulence_array=turbulence_array,\n",
        "        )\n",
        "        model = agent.get_model(model_name, model_kwargs=erl_params)\n",
        "        trained_model = agent.train_model(\n",
        "            model=model, cwd=cwd, total_timesteps=break_step\n",
        "        )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 216,
      "metadata": {
        "id": "Evsg8QtEDHDO"
      },
      "outputs": [],
      "source": [
        "from __future__ import annotations\n",
        "\n",
        "from finrl.config import INDICATORS\n",
        "from finrl.config import RLlib_PARAMS\n",
        "from finrl.config import TEST_END_DATE\n",
        "from finrl.config import TEST_START_DATE\n",
        "from finrl.config_tickers import DOW_30_TICKER\n",
        "\n",
        "def test(\n",
        "    start_date,\n",
        "    end_date,\n",
        "    ticker_list,\n",
        "    data_source,\n",
        "    time_interval,\n",
        "    technical_indicator_list,\n",
        "    drl_lib,\n",
        "    env,\n",
        "    model_name,\n",
        "    if_vix=True,\n",
        "    **kwargs,\n",
        "):\n",
        "\n",
        "    # import data processor\n",
        "    from finrl.meta.data_processor import DataProcessor\n",
        "\n",
        "    # fetch data\n",
        "    dp = DataProcessor(data_source, **kwargs)\n",
        "    data = dp.download_data(ticker_list, start_date, end_date, time_interval)\n",
        "    data = dp.clean_data(data)\n",
        "    data = dp.add_technical_indicator(data, technical_indicator_list)\n",
        "\n",
        "    if if_vix:\n",
        "        data = dp.add_vix(data)\n",
        "    else:\n",
        "        data = dp.add_turbulence(data)\n",
        "    price_array, tech_array, turbulence_array = dp.df_to_array(data, if_vix)\n",
        "\n",
        "    env_config = {\n",
        "        \"price_array\": price_array,\n",
        "        \"tech_array\": tech_array,\n",
        "        \"turbulence_array\": turbulence_array,\n",
        "        \"if_train\": False,\n",
        "    }\n",
        "    env_instance = env(config=env_config)\n",
        "\n",
        "    # load elegantrl needs state dim, action dim and net dim\n",
        "    net_dimension = kwargs.get(\"net_dimension\", 2**7)\n",
        "    cwd = kwargs.get(\"cwd\", \"./\" + str(model_name))\n",
        "    print(\"price_array: \", len(price_array))\n",
        "\n",
        "    if drl_lib == \"elegantrl\":\n",
        "        DRLAgent_erl = DRLAgent\n",
        "        episode_total_assets = DRLAgent_erl.DRL_prediction(\n",
        "            model_name=model_name,\n",
        "            cwd=cwd,\n",
        "            net_dimension=net_dimension,\n",
        "            environment=env_instance,\n",
        "        )\n",
        "        return episode_total_assets"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pf5aVHAU-xF6"
      },
      "source": [
        "## Import Dow Jones 30 Symbols"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 217,
      "metadata": {
        "id": "jx25TA_X87F-"
      },
      "outputs": [],
      "source": [
        "ticker_list = DOW_30_TICKER\n",
        "action_dim = len(DOW_30_TICKER)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 218,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UIV0kO_y-inG",
        "outputId": "81d849ff-50ad-4a99-c9bf-6258aa6a41d0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW']\n"
          ]
        }
      ],
      "source": [
        "print(ticker_list)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 219,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CnqQ-cC5-rfO",
        "outputId": "6dab0378-0053-4c98-a76f-060e5bec6f53"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['macd', 'boll_ub', 'boll_lb', 'rsi_30', 'cci_30', 'dx_30', 'close_30_sma', 'close_60_sma']\n"
          ]
        }
      ],
      "source": [
        "print(INDICATORS)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rZMkcyjZ-25l"
      },
      "source": [
        "## Calculate the DRL state dimension manually for paper trading"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 220,
      "metadata": {
        "id": "GLfkTsXK-e90"
      },
      "outputs": [],
      "source": [
        "# amount + (turbulence, turbulence_bool) + (price, shares, cd (holding time)) * stock_dim + tech_dim\n",
        "state_dim = 1 + 2 + 3 * action_dim + len(INDICATORS) * action_dim"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 221,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QqUkvImG-n66",
        "outputId": "354b2d51-ec5f-4edf-de90-a0d9a414a25d"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "333"
            ]
          },
          "metadata": {},
          "execution_count": 221
        }
      ],
      "source": [
        "state_dim"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3rwy7V72-8YY"
      },
      "source": [
        "## Get the API Keys Ready"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 222,
      "metadata": {
        "id": "8Z6qlLXY-fA2"
      },
      "outputs": [],
      "source": [
        "API_KEY = \"PKJNFLDXQ317SYY5482O\"\n",
        "API_SECRET = \"4JzjlzIAtRoezhp6epRLolXUfieCbgdgJ2GCaBFr\"\n",
        "API_BASE_URL = 'https://paper-api.alpaca.markets'\n",
        "data_url = 'wss://data.alpaca.markets'\n",
        "env = StockTradingEnv"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "J25MuZLiGqCP"
      },
      "source": [
        "## Show the data"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "puJZWm8NHtSN"
      },
      "source": [
        "### Step 1. Pick a data source"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 223,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3ZCru8f7GqgL",
        "outputId": "57a8703a-5388-47ba-be97-9ff2e0b169ed"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Alpaca successfully connected\n"
          ]
        }
      ],
      "source": [
        "DP = DataProcessor(data_source = 'alpaca',\n",
        "                  API_KEY = API_KEY,\n",
        "                  API_SECRET = API_SECRET,\n",
        "                  API_BASE_URL = API_BASE_URL\n",
        "                  )"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nvPEW2mYHvkR"
      },
      "source": [
        "### Step 2. Get ticker list, Set start date and end date, specify the data frequency"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 224,
      "metadata": {
        "id": "NPNxj6c8HIiE"
      },
      "outputs": [],
      "source": [
        "data = DP.download_data(start_date = '2021-10-04',\n",
        "                        end_date = '2021-10-08',\n",
        "                        ticker_list = ticker_list,\n",
        "                        time_interval= '1Min')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 225,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pPcazCq1d5ec",
        "outputId": "2f78bfb6-7894-4405-985d-9290d9341c1f"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1950"
            ]
          },
          "metadata": {},
          "execution_count": 225
        }
      ],
      "source": [
        "data['timestamp'].nunique()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "i46jGdE0IAel"
      },
      "source": [
        "### Step 3. Data Cleaning & Feature Engineering"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 226,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x9euUsEPHWFK",
        "outputId": "adbf0929-4b0c-4ab7-dd37-32dcf565d54a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Data cleaning started\n",
            "align start and end dates\n",
            "produce full timestamp index\n",
            "Start processing tickers\n",
            "ticker list complete\n",
            "Start concat and rename\n",
            "Data clean finished!\n",
            "Started adding Indicators\n",
            "Running Loop\n",
            "Restore Timestamps\n",
            "Finished adding Indicators\n",
            "Data cleaning started\n",
            "align start and end dates\n",
            "produce full timestamp index\n",
            "Start processing tickers\n",
            "ticker list complete\n",
            "Start concat and rename\n",
            "Data clean finished!\n"
          ]
        }
      ],
      "source": [
        "data = DP.clean_data(data)\n",
        "data = DP.add_technical_indicator(data, INDICATORS)\n",
        "data = DP.add_vix(data)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 227,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GOcPTaAgHdxa",
        "outputId": "bdb234c2-8d18-46d4-a8a6-53c15a52f12c"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(58500, 16)"
            ]
          },
          "metadata": {},
          "execution_count": 227
        }
      ],
      "source": [
        "data.shape"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bbu03L_UIMWt"
      },
      "source": [
        "### Step 4. Transform to numpy array"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 228,
      "metadata": {
        "id": "Rzj0vjZZHdGM"
      },
      "outputs": [],
      "source": [
        "price_array, tech_array, turbulence_array = DP.df_to_array(data, if_vix=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 229,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "778F_9aVJPNq",
        "outputId": "ffc9b56b-2fb7-4eae-8dae-74bbfea4e8dd"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[141.7993, 213.33  , 174.055 , ...,  54.45  ,  46.73  , 136.94  ],\n",
              "       [142.    , 214.5   , 174.715 , ...,  54.558 ,  46.98  , 137.33  ],\n",
              "       [141.56  , 214.595 , 175.11  , ...,  54.615 ,  46.975 , 137.36  ],\n",
              "       ...,\n",
              "       [143.    , 208.96  , 175.24  , ...,  53.275 ,  47.39  , 139.805 ],\n",
              "       [142.97  , 208.89  , 175.28  , ...,  53.27  ,  47.395 , 139.785 ],\n",
              "       [143.01  , 208.94  , 175.16  , ...,  53.25  ,  47.37  , 139.7   ]])"
            ]
          },
          "metadata": {},
          "execution_count": 229
        }
      ],
      "source": [
        "price_array"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eW0UDAXI1nEa"
      },
      "source": [
        "# Part 2: Train the agent"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lArLOFcJ7VMO"
      },
      "source": [
        "## Train"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 230,
      "metadata": {
        "id": "g1F84mebj4gu"
      },
      "outputs": [],
      "source": [
        "ERL_PARAMS = {\"learning_rate\": 3e-6,\"batch_size\": 2048,\"gamma\":  0.985,\n",
        "        \"seed\":312,\"net_dimension\":[128,64], \"target_step\":5000, \"eval_gap\":30,\n",
        "        \"eval_times\":1}\n",
        "env = StockTradingEnv\n",
        "#if you want to use larger datasets (change to longer period), and it raises error,\n",
        "#please try to increase \"target_step\". It should be larger than the episode steps."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 231,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "BxcNI2fdNjip",
        "outputId": "bc2c9e88-e08b-486e-f400-4f0f914c1c65"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Alpaca successfully connected\n",
            "Data cleaning started\n",
            "align start and end dates\n",
            "produce full timestamp index\n",
            "Start processing tickers\n",
            "ticker list complete\n",
            "Start concat and rename\n",
            "Data clean finished!\n",
            "Started adding Indicators\n",
            "Running Loop\n",
            "Restore Timestamps\n",
            "Finished adding Indicators\n",
            "Data cleaning started\n",
            "align start and end dates\n",
            "produce full timestamp index\n",
            "Start processing tickers\n",
            "ticker list complete\n",
            "Start concat and rename\n",
            "Data clean finished!\n",
            "\n",
            "| `step`: Number of samples, or total training steps, or running times of `env.step()`.\n",
            "| `time`: Time spent from the start of training to this moment.\n",
            "| `avgR`: Average value of cumulative rewards, which is the sum of rewards in an episode.\n",
            "| `stdR`: Standard dev of cumulative rewards, which is the sum of rewards in an episode.\n",
            "| `avgS`: Average of steps in an episode.\n",
            "| `objC`: Objective of Critic network. Or call it loss function of critic network.\n",
            "| `objA`: Objective of Actor network. It is the average Q value of the critic network.\n",
            "|     step      time  |     avgR    stdR    avgS  |     objC      objA\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-231-9d55bb4339a9>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m train(start_date = '2022-08-25', \n\u001b[0m\u001b[1;32m      2\u001b[0m       \u001b[0mend_date\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'2022-08-31'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m       \u001b[0mticker_list\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mticker_list\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m       \u001b[0mdata_source\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'alpaca'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m       \u001b[0mtime_interval\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0;34m'1Min'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-215-3b01b8e605e8>\u001b[0m in \u001b[0;36mtrain\u001b[0;34m(start_date, end_date, ticker_list, data_source, time_interval, technical_indicator_list, drl_lib, env, model_name, if_vix, **kwargs)\u001b[0m\n\u001b[1;32m     58\u001b[0m         )\n\u001b[1;32m     59\u001b[0m         \u001b[0mmodel\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0magent\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_model\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmodel_name\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmodel_kwargs\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merl_params\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 60\u001b[0;31m         trained_model = agent.train_model(\n\u001b[0m\u001b[1;32m     61\u001b[0m             \u001b[0mmodel\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmodel\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcwd\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcwd\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtotal_timesteps\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mbreak_step\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     62\u001b[0m         )\n",
            "\u001b[0;32m<ipython-input-214-ba030c88ba55>\u001b[0m in \u001b[0;36mtrain_model\u001b[0;34m(self, model, cwd, total_timesteps)\u001b[0m\n\u001b[1;32m     75\u001b[0m         \u001b[0mmodel\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcwd\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcwd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     76\u001b[0m         \u001b[0mmodel\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbreak_step\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtotal_timesteps\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 77\u001b[0;31m         \u001b[0mtrain_agent\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmodel\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     78\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     79\u001b[0m     \u001b[0;34m@\u001b[0m\u001b[0mstaticmethod\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-213-ad0e81bd5f5f>\u001b[0m in \u001b[0;36mtrain_agent\u001b[0;34m(args)\u001b[0m\n\u001b[1;32m    322\u001b[0m     \u001b[0mtorch\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mset_grad_enabled\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    323\u001b[0m     \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;31m# start training\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 324\u001b[0;31m         \u001b[0mbuffer_items\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0magent\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexplore_env\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0menv\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0margs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhorizon_len\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    325\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    326\u001b[0m         \u001b[0mtorch\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mset_grad_enabled\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-213-ad0e81bd5f5f>\u001b[0m in \u001b[0;36mexplore_env\u001b[0;34m(self, env, horizon_len)\u001b[0m\n\u001b[1;32m    203\u001b[0m             \u001b[0mary_action\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconvert\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maction\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdetach\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcpu\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnumpy\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    204\u001b[0m             \u001b[0;31m#ary_state, reward, done, _ = env.step(ary_action)  # HSG\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 205\u001b[0;31m             \u001b[0mary_state\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreward\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0menv\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mary_action\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    206\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mdone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    207\u001b[0m                 \u001b[0mary_state\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0menv\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreset\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/site-packages/finrl/meta/env_stock_trading/env_stocktrading_np.py\u001b[0m in \u001b[0;36mstep\u001b[0;34m(self, actions)\u001b[0m\n\u001b[1;32m    117\u001b[0m             \u001b[0;32mfor\u001b[0m \u001b[0mindex\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwhere\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mactions\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0;34m-\u001b[0m\u001b[0mmin_action\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m  \u001b[0;31m# sell_index:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    118\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0mprice\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mindex\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m  \u001b[0;31m# Sell only if current asset is > 0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 119\u001b[0;31m                     \u001b[0msell_num_shares\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstocks\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mindex\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m-\u001b[0m\u001b[0mactions\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mindex\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    120\u001b[0m                     \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstocks\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mindex\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m-=\u001b[0m \u001b[0msell_num_shares\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    121\u001b[0m                     self.amount += (\n",
            "\u001b[0;31mValueError\u001b[0m: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()"
          ]
        }
      ],
      "source": [
        "train(start_date = '2022-08-25',\n",
        "      end_date = '2022-08-31',\n",
        "      ticker_list = ticker_list,\n",
        "      data_source = 'alpaca',\n",
        "      time_interval= '1Min',\n",
        "      technical_indicator_list= INDICATORS,\n",
        "      drl_lib='elegantrl',\n",
        "      env=env,\n",
        "      model_name='ppo',\n",
        "      if_vix=True,\n",
        "      API_KEY = API_KEY,\n",
        "      API_SECRET = API_SECRET,\n",
        "      API_BASE_URL = API_BASE_URL,\n",
        "      erl_params=ERL_PARAMS,\n",
        "      cwd='./papertrading_erl', #current_working_dir\n",
        "      break_step=1e5)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "g37WugV_1pAS"
      },
      "source": [
        "## Test"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "SxYoWCDa02TW"
      },
      "outputs": [],
      "source": [
        "account_value_erl=test(start_date = '2022-09-01',\n",
        "                      end_date = '2022-09-02',\n",
        "                      ticker_list = ticker_list,\n",
        "                      data_source = 'alpaca',\n",
        "                      time_interval= '1Min',\n",
        "                      technical_indicator_list= INDICATORS,\n",
        "                      drl_lib='elegantrl',\n",
        "                      env=env,\n",
        "                      model_name='ppo',\n",
        "                      if_vix=True,\n",
        "                      API_KEY = API_KEY,\n",
        "                      API_SECRET = API_SECRET,\n",
        "                      API_BASE_URL = API_BASE_URL,\n",
        "                      cwd='./papertrading_erl',\n",
        "                      net_dimension = ERL_PARAMS['net_dimension'])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e8aNQ58X7avM"
      },
      "source": [
        "## Use full data to train"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3CQ9_Yv41r88"
      },
      "source": [
        "After tuning well, retrain on the training and testing sets"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cUSgbwt_10V3"
      },
      "outputs": [],
      "source": [
        "train(start_date = '2022-08-25',\n",
        "      end_date = '2022-09-02',\n",
        "      ticker_list = ticker_list,\n",
        "      data_source = 'alpaca',\n",
        "      time_interval= '1Min',\n",
        "      technical_indicator_list= INDICATORS,\n",
        "      drl_lib='elegantrl',\n",
        "      env=env,\n",
        "      model_name='ppo',\n",
        "      if_vix=True,\n",
        "      API_KEY = API_KEY,\n",
        "      API_SECRET = API_SECRET,\n",
        "      API_BASE_URL = API_BASE_URL,\n",
        "      erl_params=ERL_PARAMS,\n",
        "      cwd='./papertrading_erl_retrain',\n",
        "      break_step=2e5)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sIQN6Ggt7gXY"
      },
      "source": [
        "# Part 3: Deploy the agent"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UFoxkigg1zXa"
      },
      "source": [
        "## Setup Alpaca Paper trading environment"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LpkoZpYzfneS"
      },
      "outputs": [],
      "source": [
        "import datetime\n",
        "import threading\n",
        "from finrl.meta.data_processors.processor_alpaca import AlpacaProcessor\n",
        "import alpaca_trade_api as tradeapi\n",
        "import time\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import torch\n",
        "import gym\n",
        "\n",
        "class AlpacaPaperTrading():\n",
        "\n",
        "    def __init__(self,ticker_list, time_interval, drl_lib, agent, cwd, net_dim,\n",
        "                 state_dim, action_dim, API_KEY, API_SECRET,\n",
        "                 API_BASE_URL, tech_indicator_list, turbulence_thresh=30,\n",
        "                 max_stock=1e2, latency = None):\n",
        "        #load agent\n",
        "        self.drl_lib = drl_lib\n",
        "        if agent =='ppo':\n",
        "            if drl_lib == 'elegantrl':\n",
        "                agent_class = AgentPPO\n",
        "                agent = agent_class(net_dim, state_dim, action_dim)\n",
        "                actor = agent.act\n",
        "                # load agent\n",
        "                try:\n",
        "                    cwd = cwd + '/actor.pth'\n",
        "                    print(f\"| load actor from: {cwd}\")\n",
        "                    actor.load_state_dict(torch.load(cwd, map_location=lambda storage, loc: storage))\n",
        "                    self.act = actor\n",
        "                    self.device = agent.device\n",
        "                except BaseException:\n",
        "                    raise ValueError(\"Fail to load agent!\")\n",
        "\n",
        "            elif drl_lib == 'rllib':\n",
        "                from ray.rllib.agents import ppo\n",
        "                from ray.rllib.agents.ppo.ppo import PPOTrainer\n",
        "\n",
        "                config = ppo.DEFAULT_CONFIG.copy()\n",
        "                config['env'] = StockEnvEmpty\n",
        "                config[\"log_level\"] = \"WARN\"\n",
        "                config['env_config'] = {'state_dim':state_dim,\n",
        "                            'action_dim':action_dim,}\n",
        "                trainer = PPOTrainer(env=StockEnvEmpty, config=config)\n",
        "                trainer.restore(cwd)\n",
        "                try:\n",
        "                    trainer.restore(cwd)\n",
        "                    self.agent = trainer\n",
        "                    print(\"Restoring from checkpoint path\", cwd)\n",
        "                except:\n",
        "                    raise ValueError('Fail to load agent!')\n",
        "\n",
        "            elif drl_lib == 'stable_baselines3':\n",
        "                from stable_baselines3 import PPO\n",
        "\n",
        "                try:\n",
        "                    #load agent\n",
        "                    self.model = PPO.load(cwd)\n",
        "                    print(\"Successfully load model\", cwd)\n",
        "                except:\n",
        "                    raise ValueError('Fail to load agent!')\n",
        "\n",
        "            else:\n",
        "                raise ValueError('The DRL library input is NOT supported yet. Please check your input.')\n",
        "\n",
        "        else:\n",
        "            raise ValueError('Agent input is NOT supported yet.')\n",
        "\n",
        "\n",
        "\n",
        "        #connect to Alpaca trading API\n",
        "        try:\n",
        "            self.alpaca = tradeapi.REST(API_KEY,API_SECRET,API_BASE_URL, 'v2')\n",
        "        except:\n",
        "            raise ValueError('Fail to connect Alpaca. Please check account info and internet connection.')\n",
        "\n",
        "        #read trading time interval\n",
        "        if time_interval == '1s':\n",
        "            self.time_interval = 1\n",
        "        elif time_interval == '5s':\n",
        "            self.time_interval = 5\n",
        "        elif time_interval == '1Min':\n",
        "            self.time_interval = 60\n",
        "        elif time_interval == '5Min':\n",
        "            self.time_interval = 60 * 5\n",
        "        elif time_interval == '15Min':\n",
        "            self.time_interval = 60 * 15\n",
        "        else:\n",
        "            raise ValueError('Time interval input is NOT supported yet.')\n",
        "\n",
        "        #read trading settings\n",
        "        self.tech_indicator_list = tech_indicator_list\n",
        "        self.turbulence_thresh = turbulence_thresh\n",
        "        self.max_stock = max_stock\n",
        "\n",
        "        #initialize account\n",
        "        self.stocks = np.asarray([0] * len(ticker_list)) #stocks holding\n",
        "        self.stocks_cd = np.zeros_like(self.stocks)\n",
        "        self.cash = None #cash record\n",
        "        self.stocks_df = pd.DataFrame(self.stocks, columns=['stocks'], index = ticker_list)\n",
        "        self.asset_list = []\n",
        "        self.price = np.asarray([0] * len(ticker_list))\n",
        "        self.stockUniverse = ticker_list\n",
        "        self.turbulence_bool = 0\n",
        "        self.equities = []\n",
        "\n",
        "    def test_latency(self, test_times = 10):\n",
        "        total_time = 0\n",
        "        for i in range(0, test_times):\n",
        "            time0 = time.time()\n",
        "            self.get_state()\n",
        "            time1 = time.time()\n",
        "            temp_time = time1 - time0\n",
        "            total_time += temp_time\n",
        "        latency = total_time/test_times\n",
        "        print('latency for data processing: ', latency)\n",
        "        return latency\n",
        "\n",
        "    def run(self):\n",
        "        orders = self.alpaca.list_orders(status=\"open\")\n",
        "        for order in orders:\n",
        "          self.alpaca.cancel_order(order.id)\n",
        "\n",
        "        # Wait for market to open.\n",
        "        print(\"Waiting for market to open...\")\n",
        "        tAMO = threading.Thread(target=self.awaitMarketOpen)\n",
        "        tAMO.start()\n",
        "        tAMO.join()\n",
        "        print(\"Market opened.\")\n",
        "        while True:\n",
        "\n",
        "          # Figure out when the market will close so we can prepare to sell beforehand.\n",
        "          clock = self.alpaca.get_clock()\n",
        "          closingTime = clock.next_close.replace(tzinfo=datetime.timezone.utc).timestamp()\n",
        "          currTime = clock.timestamp.replace(tzinfo=datetime.timezone.utc).timestamp()\n",
        "          self.timeToClose = closingTime - currTime\n",
        "\n",
        "          if(self.timeToClose < (60)):\n",
        "            # Close all positions when 1 minutes til market close.\n",
        "            print(\"Market closing soon. Stop trading.\")\n",
        "            break\n",
        "\n",
        "            '''# Close all positions when 1 minutes til market close.\n",
        "            print(\"Market closing soon.  Closing positions.\")\n",
        "\n",
        "            positions = self.alpaca.list_positions()\n",
        "            for position in positions:\n",
        "              if(position.side == 'long'):\n",
        "                orderSide = 'sell'\n",
        "              else:\n",
        "                orderSide = 'buy'\n",
        "              qty = abs(int(float(position.qty)))\n",
        "              respSO = []\n",
        "              tSubmitOrder = threading.Thread(target=self.submitOrder(qty, position.symbol, orderSide, respSO))\n",
        "              tSubmitOrder.start()\n",
        "              tSubmitOrder.join()\n",
        "\n",
        "            # Run script again after market close for next trading day.\n",
        "            print(\"Sleeping until market close (15 minutes).\")\n",
        "            time.sleep(60 * 15)'''\n",
        "\n",
        "          else:\n",
        "            trade = threading.Thread(target=self.trade)\n",
        "            trade.start()\n",
        "            trade.join()\n",
        "            last_equity = float(self.alpaca.get_account().last_equity)\n",
        "            cur_time = time.time()\n",
        "            self.equities.append([cur_time,last_equity])\n",
        "            time.sleep(self.time_interval)\n",
        "\n",
        "    def awaitMarketOpen(self):\n",
        "        isOpen = self.alpaca.get_clock().is_open\n",
        "        while(not isOpen):\n",
        "          clock = self.alpaca.get_clock()\n",
        "          openingTime = clock.next_open.replace(tzinfo=datetime.timezone.utc).timestamp()\n",
        "          currTime = clock.timestamp.replace(tzinfo=datetime.timezone.utc).timestamp()\n",
        "          timeToOpen = int((openingTime - currTime) / 60)\n",
        "          print(str(timeToOpen) + \" minutes til market open.\")\n",
        "          time.sleep(60)\n",
        "          isOpen = self.alpaca.get_clock().is_open\n",
        "\n",
        "    def trade(self):\n",
        "        state = self.get_state()\n",
        "\n",
        "        if self.drl_lib == 'elegantrl':\n",
        "            with torch.no_grad():\n",
        "                s_tensor = torch.as_tensor((state,), device=self.device)\n",
        "                a_tensor = self.act(s_tensor)\n",
        "                action = a_tensor.detach().cpu().numpy()[0]\n",
        "            action = (action * self.max_stock).astype(int)\n",
        "\n",
        "        elif self.drl_lib == 'rllib':\n",
        "            action = self.agent.compute_single_action(state)\n",
        "\n",
        "        elif self.drl_lib == 'stable_baselines3':\n",
        "            action = self.model.predict(state)[0]\n",
        "\n",
        "        else:\n",
        "            raise ValueError('The DRL library input is NOT supported yet. Please check your input.')\n",
        "\n",
        "        self.stocks_cd += 1\n",
        "        if self.turbulence_bool == 0:\n",
        "            min_action = 10  # stock_cd\n",
        "            for index in np.where(action < -min_action)[0]:  # sell_index:\n",
        "                sell_num_shares = min(self.stocks[index], -action[index])\n",
        "                qty =  abs(int(sell_num_shares))\n",
        "                respSO = []\n",
        "                tSubmitOrder = threading.Thread(target=self.submitOrder(qty, self.stockUniverse[index], 'sell', respSO))\n",
        "                tSubmitOrder.start()\n",
        "                tSubmitOrder.join()\n",
        "                self.cash = float(self.alpaca.get_account().cash)\n",
        "                self.stocks_cd[index] = 0\n",
        "\n",
        "            for index in np.where(action > min_action)[0]:  # buy_index:\n",
        "                if self.cash < 0:\n",
        "                    tmp_cash = 0\n",
        "                else:\n",
        "                    tmp_cash = self.cash\n",
        "                buy_num_shares = min(tmp_cash // self.price[index], abs(int(action[index])))\n",
        "                if (buy_num_shares != buy_num_shares): # if buy_num_change = nan\n",
        "                    qty = 0 # set to 0 quantity\n",
        "                else:\n",
        "                    qty = abs(int(buy_num_shares))\n",
        "                qty = abs(int(buy_num_shares))\n",
        "                respSO = []\n",
        "                tSubmitOrder = threading.Thread(target=self.submitOrder(qty, self.stockUniverse[index], 'buy', respSO))\n",
        "                tSubmitOrder.start()\n",
        "                tSubmitOrder.join()\n",
        "                self.cash = float(self.alpaca.get_account().cash)\n",
        "                self.stocks_cd[index] = 0\n",
        "\n",
        "        else:  # sell all when turbulence\n",
        "            positions = self.alpaca.list_positions()\n",
        "            for position in positions:\n",
        "                if(position.side == 'long'):\n",
        "                    orderSide = 'sell'\n",
        "                else:\n",
        "                    orderSide = 'buy'\n",
        "                qty = abs(int(float(position.qty)))\n",
        "                respSO = []\n",
        "                tSubmitOrder = threading.Thread(target=self.submitOrder(qty, position.symbol, orderSide, respSO))\n",
        "                tSubmitOrder.start()\n",
        "                tSubmitOrder.join()\n",
        "\n",
        "            self.stocks_cd[:] = 0\n",
        "\n",
        "\n",
        "    def get_state(self):\n",
        "        alpaca = AlpacaProcessor(api=self.alpaca)\n",
        "        price, tech, turbulence = alpaca.fetch_latest_data(ticker_list = self.stockUniverse, time_interval='1Min',\n",
        "                                                     tech_indicator_list=self.tech_indicator_list)\n",
        "        turbulence_bool = 1 if turbulence >= self.turbulence_thresh else 0\n",
        "\n",
        "        turbulence = (self.sigmoid_sign(turbulence, self.turbulence_thresh) * 2 ** -5).astype(np.float32)\n",
        "\n",
        "        tech = tech * 2 ** -7\n",
        "        positions = self.alpaca.list_positions()\n",
        "        stocks = [0] * len(self.stockUniverse)\n",
        "        for position in positions:\n",
        "            ind = self.stockUniverse.index(position.symbol)\n",
        "            stocks[ind] = ( abs(int(float(position.qty))))\n",
        "\n",
        "        stocks = np.asarray(stocks, dtype = float)\n",
        "        cash = float(self.alpaca.get_account().cash)\n",
        "        self.cash = cash\n",
        "        self.stocks = stocks\n",
        "        self.turbulence_bool = turbulence_bool\n",
        "        self.price = price\n",
        "\n",
        "\n",
        "\n",
        "        amount = np.array(self.cash * (2 ** -12), dtype=np.float32)\n",
        "        scale = np.array(2 ** -6, dtype=np.float32)\n",
        "        state = np.hstack((amount,\n",
        "                    turbulence,\n",
        "                    self.turbulence_bool,\n",
        "                    price * scale,\n",
        "                    self.stocks * scale,\n",
        "                    self.stocks_cd,\n",
        "                    tech,\n",
        "                    )).astype(np.float32)\n",
        "        state[np.isnan(state)] = 0.0\n",
        "        state[np.isinf(state)] = 0.0\n",
        "        print(len(self.stockUniverse))\n",
        "        return state\n",
        "\n",
        "    def submitOrder(self, qty, stock, side, resp):\n",
        "        if(qty > 0):\n",
        "          try:\n",
        "            self.alpaca.submit_order(stock, qty, side, \"market\", \"day\")\n",
        "            print(\"Market order of | \" + str(qty) + \" \" + stock + \" \" + side + \" | completed.\")\n",
        "            resp.append(True)\n",
        "          except:\n",
        "            print(\"Order of | \" + str(qty) + \" \" + stock + \" \" + side + \" | did not go through.\")\n",
        "            resp.append(False)\n",
        "        else:\n",
        "          print(\"Quantity is 0, order of | \" + str(qty) + \" \" + stock + \" \" + side + \" | not completed.\")\n",
        "          resp.append(True)\n",
        "\n",
        "    @staticmethod\n",
        "    def sigmoid_sign(ary, thresh):\n",
        "        def sigmoid(x):\n",
        "            return 1 / (1 + np.exp(-x * np.e)) - 0.5\n",
        "\n",
        "        return sigmoid(ary / thresh) * thresh\n",
        "\n",
        "class StockEnvEmpty(gym.Env):\n",
        "    #Empty Env used for loading rllib agent\n",
        "    def __init__(self,config):\n",
        "      state_dim = config['state_dim']\n",
        "      action_dim = config['action_dim']\n",
        "      self.env_num = 1\n",
        "      self.max_step = 10000\n",
        "      self.env_name = 'StockEnvEmpty'\n",
        "      self.state_dim = state_dim\n",
        "      self.action_dim = action_dim\n",
        "      self.if_discrete = False\n",
        "      self.target_return = 9999\n",
        "      self.observation_space = gym.spaces.Box(low=-3000, high=3000, shape=(state_dim,), dtype=np.float32)\n",
        "      self.action_space = gym.spaces.Box(low=-1, high=1, shape=(action_dim,), dtype=np.float32)\n",
        "\n",
        "    def reset(self):\n",
        "        return\n",
        "\n",
        "    def step(self, actions):\n",
        "        return"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "os4C4-4H7ns7"
      },
      "source": [
        "## Run Paper trading"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "7nw0i-0UN3-7"
      },
      "outputs": [],
      "source": [
        "print(DOW_30_TICKER)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "YsSBK9ION1t6"
      },
      "outputs": [],
      "source": [
        "state_dim"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "xYtSv6P1N247"
      },
      "outputs": [],
      "source": [
        "action_dim"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Kl9nulnAJtiI"
      },
      "outputs": [],
      "source": [
        "paper_trading_erl = AlpacaPaperTrading(ticker_list = DOW_30_TICKER,\n",
        "                                       time_interval = '1Min',\n",
        "                                       drl_lib = 'elegantrl',\n",
        "                                       agent = 'ppo',\n",
        "                                       cwd = './papertrading_erl_retrain',\n",
        "                                       net_dim = ERL_PARAMS['net_dimension'],\n",
        "                                       state_dim = state_dim,\n",
        "                                       action_dim= action_dim,\n",
        "                                       API_KEY = API_KEY,\n",
        "                                       API_SECRET = API_SECRET,\n",
        "                                       API_BASE_URL = API_BASE_URL,\n",
        "                                       tech_indicator_list = INDICATORS,\n",
        "                                       turbulence_thresh=30,\n",
        "                                       max_stock=1e2)\n",
        "paper_trading_erl.run()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "srzBZfYEUI1O"
      },
      "source": [
        "# Part 4: Check Portfolio Performance"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "chovN1UhTAht"
      },
      "outputs": [],
      "source": [
        "import alpaca_trade_api as tradeapi\n",
        "import exchange_calendars as tc\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "import pytz\n",
        "import yfinance as yf\n",
        "import matplotlib.ticker as ticker\n",
        "import matplotlib.dates as mdates\n",
        "from datetime import datetime as dt\n",
        "from finrl.plot import backtest_stats\n",
        "import matplotlib.pyplot as plt"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "CaofxMNCfAR1"
      },
      "outputs": [],
      "source": [
        "def get_trading_days(start, end):\n",
        "    nyse = tc.get_calendar('NYSE')\n",
        "    df = nyse.sessions_in_range(pd.Timestamp(start,tz=pytz.UTC),\n",
        "                                pd.Timestamp(end,tz=pytz.UTC))\n",
        "    trading_days = []\n",
        "    for day in df:\n",
        "        trading_days.append(str(day)[:10])\n",
        "\n",
        "    return trading_days\n",
        "\n",
        "def alpaca_history(key, secret, url, start, end):\n",
        "    api = tradeapi.REST(key, secret, url, 'v2')\n",
        "    trading_days = get_trading_days(start, end)\n",
        "    df = pd.DataFrame()\n",
        "    for day in trading_days:\n",
        "        df = df.append(api.get_portfolio_history(date_start = day,timeframe='5Min').df.iloc[:78])\n",
        "    equities = df.equity.values\n",
        "    cumu_returns = equities/equities[0]\n",
        "    cumu_returns = cumu_returns[~np.isnan(cumu_returns)]\n",
        "\n",
        "    return df, cumu_returns\n",
        "\n",
        "def DIA_history(start):\n",
        "    data_df = yf.download(['^DJI'],start=start, interval=\"5m\")\n",
        "    data_df = data_df.iloc[:]\n",
        "    baseline_returns = data_df['Adj Close'].values/data_df['Adj Close'].values[0]\n",
        "    return data_df, baseline_returns"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5CHiZRVpURpx"
      },
      "source": [
        "## Get cumulative return"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Hmmo-iG1s_rd"
      },
      "outputs": [],
      "source": [
        "API_KEY = \"\"\n",
        "API_SECRET = \"\"\n",
        "API_BASE_URL = 'https://paper-api.alpaca.markets'\n",
        "data_url = 'wss://data.alpaca.markets'"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "O_YT7v-LSdfV"
      },
      "outputs": [],
      "source": [
        "df_erl, cumu_erl = alpaca_history(key=API_KEY,\n",
        "                                  secret=API_SECRET,\n",
        "                                  url=API_BASE_URL,\n",
        "                                  start='2022-09-01', #must be within 1 month\n",
        "                                  end='2022-09-12') #change the date if error occurs\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "IMcQjwHOS6Zb"
      },
      "outputs": [],
      "source": [
        "df_djia, cumu_djia = DIA_history(start='2022-09-01')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "PJXPwmx9Ts5o"
      },
      "outputs": [],
      "source": [
        "df_erl.tail()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "o1Iaw90FTNfU"
      },
      "outputs": [],
      "source": [
        "returns_erl = cumu_erl -1\n",
        "returns_dia = cumu_djia - 1\n",
        "returns_dia = returns_dia[:returns_erl.shape[0]]\n",
        "print('len of erl return: ', returns_erl.shape[0])\n",
        "print('len of dia return: ', returns_dia.shape[0])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "2IawaMsDwZni"
      },
      "outputs": [],
      "source": [
        "returns_erl"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5Z0LEm7KUZ5W"
      },
      "source": [
        "## plot and save"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Foqk1wIQTQJ3"
      },
      "outputs": [],
      "source": [
        "import matplotlib.pyplot as plt\n",
        "plt.figure(dpi=1000)\n",
        "plt.grid()\n",
        "plt.grid(which='minor', axis='y')\n",
        "plt.title('Stock Trading (Paper trading)', fontsize=20)\n",
        "plt.plot(returns_erl, label = 'ElegantRL Agent', color = 'red')\n",
        "#plt.plot(returns_sb3, label = 'Stable-Baselines3 Agent', color = 'blue' )\n",
        "#plt.plot(returns_rllib, label = 'RLlib Agent', color = 'green')\n",
        "plt.plot(returns_dia, label = 'DJIA', color = 'grey')\n",
        "plt.ylabel('Return', fontsize=16)\n",
        "plt.xlabel('Year 2021', fontsize=16)\n",
        "plt.xticks(size = 14)\n",
        "plt.yticks(size = 14)\n",
        "ax = plt.gca()\n",
        "ax.xaxis.set_major_locator(ticker.MultipleLocator(78))\n",
        "ax.xaxis.set_minor_locator(ticker.MultipleLocator(6))\n",
        "ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.005))\n",
        "ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=2))\n",
        "ax.xaxis.set_major_formatter(ticker.FixedFormatter(['','10-19','','10-20',\n",
        "                                                    '','10-21','','10-22']))\n",
        "plt.legend(fontsize=10.5)\n",
        "plt.savefig('papertrading_stock.png')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "O_LsHVj_TZGL"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "colab": {
      "collapsed_sections": [
        "0EVJIQUR6_fu",
        "9tzAw9k26nAC",
        "zjLda8No6pvI",
        "pf5aVHAU-xF6",
        "rZMkcyjZ-25l",
        "3rwy7V72-8YY",
        "J25MuZLiGqCP",
        "eW0UDAXI1nEa",
        "UFoxkigg1zXa"
      ],
      "provenance": []
    },
    "gpuClass": "standard",
    "kernelspec": {
      "display_name": "Python 3.8.10 ('venv': venv)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8.10"
    },
    "vscode": {
      "interpreter": {
        "hash": "005d14239094016f48a03a57365c4ccb734e3f38c20ed0ca595d84f773bc39cd"
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}