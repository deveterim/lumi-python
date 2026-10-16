import lumi

# Definir API Key globalmente ou via LUMI_API_KEY no ambiente
lumi.api_key = "ma_live_123456789"

params: lumi.Emails.SendParams = {
    "from": "onboarding@suaempresa.ao",
    "to": ["cliente@gmail.com"],
    "subject": "Boas-vindas ao Lumi!",
    "html": "<h1>Olá!</h1><p>Seu e-mail transacional foi entregue com sucesso.</p>",
}

try:
    response = lumi.Emails.send(params)
    print("E-mail enviado com sucesso. ID:", response.get("id"))
except lumi.LumiError as e:
    print(f"Erro ({e.status_code}): {e.message}")
