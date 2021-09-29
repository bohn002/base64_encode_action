# base64_encode_action
Encode a ENV Var without exposing it.
[![Integration Test](https://github.com/bohn002/base64_encode_action/actions/workflows/integration.yml/badge.svg)](https://github.com/bohn002/base64_encode_action/actions/workflows/integration.yml)

### Usage
```
steps:
    - name: Encode Var
    id: b64encode
    uses: bohn002/base64_encode_action@main
    with:
      env_name: "RANDOM"

    - name: Check outputs
    run: |
      echo "${{ steps.b64encode.outputs.encoded_string }}"
```
