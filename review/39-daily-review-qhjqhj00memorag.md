# 🚀 qhjqhj00/MemoRAG

## Review
- [x] The key idea of the project (Dual System Architecture)
- [x] Brief understanding the cache mechanism used in the project (transformers library)
- [ ] The dataset used in the project
- [ ] The evaluation metric used in the project

## Dual System Architecture
1. A light but long-range LLM
2. An expensive but expressive LLM

### Light but long-range LLM
This LLM is used to form the global memory of the database. Once a task is presented, it won't generate the ultimate answer but will generate draft answers, cluing the retrieval tools to locate useful information within the database.

### Expensive but expressive LLM
This LLM generates the ultimate answer based on the retrieved information.

## Understanding the Project

```shell
gitingest https://github.com/qhjqhj00/MemoRAG -i "*.py"
```

### Cache
```python
# File: /memorag/memorag_lite.py
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, DynamicCache

# File: /memorag/memorag.py
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, DynamicCache
```

In their implementation, they used the `DynamicCache` class from the `transformers` library. This class caches the model's output and reuses it for future predictions. Seven methods from the `transformers` library can be found [here](https://huggingface.co/docs/transformers/en/kv_cache).

1. `Dynamic Cache`
1. `Static Cache`
1. `Offloaded Cache`
1. `Offloaded Static Cache`
1. `Quantized Cache`
1. `Sliding Window Cache`
1. `Sink Cache`

![alt text](image-9.png)

#### How to Use the Cache

In `transformers` library, the cache can be used by two ways:
1. `generate` method - Default. Automatically handles the cache
2. `forward` method - Good for flexible tasks, where you can customize the cache (like removing unnecessary tokens or adding prompt tokens).



<!-- 3. light but longrange LLM to form the global memory of database (Once a task is presented, it generates draft answers, cluing the retrieval tools to locate useful information within the database.)
1. On the other hand, it leverages an expensive but expressive
LLM, which generates the ultimate answer based on the retrieved information. -->