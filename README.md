🇩🇪 Deutsch:
openwebui-litellm-proxy ist ein Setup-Projekt zur Integration von LiteLLM als universelle API-Schnittstelle für verschiedene LLM-Anbieter in OpenWebUI.
Es ermöglicht die Anbindung von Modellen wie OpenAI, Mistral, Ollama, Anthropic u. v. m. über eine zentrale Proxy-Konfiguration.

🇬🇧 English:
openwebui-litellm-proxy is a setup project to integrate LiteLLM as a universal API gateway for multiple LLM providers into OpenWebUI.
It enables seamless use of models like OpenAI, Mistral, Ollama, Anthropic, and others via one central proxy configuration.

# openwebui-litellm-proxy

🇩🇪 **OpenWebUI + LiteLLM Proxy Setup**

Dies ist ein Setup-Projekt zur Integration von [LiteLLM](https://github.com/BerriAI/litellm) als universelle API-Schnittstelle für verschiedene LLM-Anbieter in OpenWebUI. Es ermöglicht die Anbindung von Modellen wie OpenAI, Mistral, Ollama, Anthropic u. v. m. über eine zentrale Proxy-Konfiguration.

## 🔧 Features

- 🔁 Proxy für beliebige LLMs via LiteLLM
- 🤖 Unterstützung für OpenAI, Mistral, Anthropic, Ollama etc.
- ⚙️ Konfigurierbar via `.env` + `config.yaml`

## 📦 Schnellstart

```bash
git clone <repo-url>
cd openwebui-litellm-proxy
cp .env.example .env
# Bearbeite .env mit deinem OpenAI-Key etc.
python main.py


## 🇬🇧 English

**openwebui-litellm-proxy** is a setup project to integrate [LiteLLM](https://github.com/BerriAI/litellm) as a **universal API interface** for various LLM providers into **OpenWebUI**.  
It enables connecting models like **OpenAI**, **Mistral**, **Ollama**, **Anthropic**, and many more via a central proxy configuration.

### 🔧 Features

- 🔁 Proxy for any LLM via LiteLLM  
- 🤖 Support for OpenAI, Mistral, Anthropic, Ollama, and others  
- ⚙️ Easily configurable using `.env` & `config.yaml`

### ▶️ Quickstart

```bash
git clone <REPOSITORY-URL>
cd openwebui-litellm-proxy
cp .env.example .env
# Edit .env with your OpenAI key etc.
python main.py