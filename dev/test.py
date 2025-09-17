

from src.cob_ai.client import COB

cob_api_key = "cob_a_4340e5060dd211964157bcee3d5bb7f311c6f4c537cbcb33ee4968edda44c8ab"

cob = COB(
    apikey=cob_api_key,
)

cob.status()