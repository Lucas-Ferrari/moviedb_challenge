from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def configure_retry_policy():
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["GET", "POST"],
    )
    return HTTPAdapter(max_retries=retry_strategy) 
