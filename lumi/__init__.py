import os
from typing import Optional
from lumi.emails import Emails
from lumi.batch import Batch
from lumi.domains import Domains
from lumi.api_keys import ApiKeys
from lumi.webhooks import Webhooks
from lumi.errors import (
    LumiError,
    AuthenticationError,
    InvalidRequestError,
    RateLimitError,
    InternalServerError,
)
from lumi._version import __version__

api_key: Optional[str] = os.environ.get("LUMI_API_KEY")
api_url: Optional[str] = os.environ.get("LUMI_BASE_URL")

class Lumi:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("LUMI_API_KEY")
        self.emails = Emails(api_key=self.api_key)
        self.batch = Batch(api_key=self.api_key)
        self.domains = Domains(api_key=self.api_key)
        self.api_keys = ApiKeys(api_key=self.api_key)
        self.webhooks = Webhooks()

__all__ = [
    "Lumi",
    "Emails",
    "Batch",
    "Domains",
    "ApiKeys",
    "Webhooks",
    "LumiError",
    "AuthenticationError",
    "InvalidRequestError",
    "RateLimitError",
    "InternalServerError",
    "api_key",
    "api_url",
    "__version__",
]
