# Lumi Python SDK (`mailifica`)

> SDK oficial em Python para a infraestrutura de e-mails transacionais **Lumi**, com interface drop-in replacement compatível com o Resend.

---

## 📦 Instalação

```bash
pip install mailifica
# ou com Poetry
poetry add mailifica
```

---

## 🚀 Como Usar

### 1. Envio Estático (Estilo Resend)

```python
import lumi

# Configurar API Key
lumi.api_key = "ma_live_123456789"

params: lumi.Emails.SendParams = {
    "from": "onboarding@suaempresa.ao",
    "to": ["cliente@gmail.com"],
    "subject": "Boas-vindas!",
    "html": "<h1>Olá!</h1><p>Seu e-mail transacional foi entregue.</p>",
}

email = lumi.Emails.send(params)
print("E-mail ID:", email["id"])
```

### 2. Envio Orientado a Objetos / Instância

```python
from lumi import Lumi

client = Lumi("ma_live_123456789")

response = client.emails.send({
    "from": "suporte@suaempresa.ao",
    "to": "usuario@empresa.com",
    "subject": "Notificação",
    "text": "Seu chamado foi atualizado.",
})
```

### 3. Envio em Lote (Batch)

```python
import lumi

lumi.api_key = "ma_live_123456789"

batch_response = lumi.Batch.send([
    {
        "from": "novidades@suaempresa.ao",
        "to": "cliente1@gmail.com",
        "subject": "Atualização Mensal",
        "html": "<p>Novidades do mês</p>",
    },
    {
        "from": "novidades@suaempresa.ao",
        "to": "cliente2@gmail.com",
        "subject": "Atualização Mensal",
        "html": "<p>Novidades do mês</p>",
    }
])
```

### 4. Gestão de Domínios & API Keys

```python
import lumi

# Criar domínio
domain = lumi.Domains.create({"name": "meudominio.ao"})

# Verificar registros DNS
verified = lumi.Domains.verify(domain["id"])

# Listar API Keys
keys = lumi.ApiKeys.list()
```

### 5. Validação de Webhooks HMAC

```python
from lumi import Webhooks

is_valid = Webhooks.verify_signature(
    payload=raw_body,
    signature=headers.get("mailifica-signature"),
    secret="seu_webhook_secret"
)
```

---

## 📄 Licença

MIT © [Lumi](https://lumi.com)
