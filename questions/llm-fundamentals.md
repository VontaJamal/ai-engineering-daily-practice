# LLM Fundamentals

Imported from [Outcome School's AI Engineering Interview Questions](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions) at commit `f0a843b8428f`.

Question count: **66**

Use the linked material for study after cold recall. When no material is linked, prefer a current primary source.

### LLM-001

What are foundation models, and how have they changed AI engineering?

- Answer: Explained in this video: [AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization](https://www.youtube.com/watch?v=lnfWvX66FUk)

### LLM-002

What is a Large Language Model (LLM), and how does it work?

- Answer: Explained in this video: [AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization](https://www.youtube.com/watch?v=lnfWvX66FUk)

### LLM-003

Inside ChatGPT: What Happens After You Hit Enter?

- Answer: [Inside ChatGPT: What Happens After You Hit Enter](https://outcomeschool.substack.com/p/inside-chatgpt-what-happens-after)

### LLM-004

What is the Transformer architecture and how does it work?

- Answer: [Decoding Transformer Architecture](https://outcomeschool.com/blog/decoding-transformer-architecture)

### LLM-005

What are the key components of the Transformer architecture?

- Answer: [Decoding Transformer Architecture](https://outcomeschool.com/blog/decoding-transformer-architecture)

### LLM-006

What is tokenization in LLMs?

- Answer: [Tokenization in Large Language Models (LLMs)](https://www.youtube.com/watch?v=sK2s9I84EVI)

### LLM-007

Explain BPE (Byte Pair Encoding).

- Answer: [Byte Pair Encoding](https://outcomeschool.com/blog/bpe-in-llms)

### LLM-008

Explain WordPiece and SentencePiece.

- Supporting material: not linked in the source bank.

### LLM-009

What is positional encoding, and why is it needed in Transformers?

- Answer: [Positional Embeddings in LLMs](https://outcomeschool.substack.com/p/positional-embeddings-in-llms)

### LLM-010

What are embeddings?

- Answer: [Embeddings in Machine Learning](https://www.youtube.com/watch?v=LedXW6xl21s)

### LLM-011

Explain the Query(Q), Key(K), and Value(V) in attention.

- Answer: [Math behind Attention - Q, K, and V](https://outcomeschool.com/blog/math-behind-attention-qkv)

### LLM-012

What is self-attention, and how does it work in Transformers?

- Answer: [Self Attention in Transformers](https://outcomeschool.com/blog/self-attention-in-transformers)

### LLM-013

What is Cross Attention in Transformers?

- Answer: [Cross Attention in Transformers](https://outcomeschool.com/blog/cross-attention-in-transformers)

### LLM-014

Why do we scale the dot product attention by √dₖ in the Transformer architecture?

- Answer: [Math behind √dₖ Scaling Factor in Attention](https://outcomeschool.com/blog/scaling-dot-product-attention)

### LLM-015

What is causal masking?

- Answer: [Causal Masking in Attention](https://outcomeschool.com/blog/causal-masking-in-attention)

### LLM-016

What are multi-head attention mechanisms? Why use multiple attention heads?

- Answer: [Multi-Head Attention in Transformers](https://outcomeschool.com/blog/multi-head-attention-in-transformers)

### LLM-017

What are Feed-Forward Networks in LLMs?

- Answer: [Feed-Forward Networks in LLMs](https://outcomeschool.com/blog/feed-forward-networks-in-llms)

### LLM-018

What is the context window in LLMs, and why does it matter?

- Answer: [Context Window in LLMs](https://www.linkedin.com/posts/amit-shekhar-iitbhu_the-context-window-is-the-llms-working-memory-activity-7437754426175672320-MH9c)

### LLM-019

Why is the context window limited in LLMs?

- Answer: [Why is the context window limited in LLMs?](https://www.youtube.com/watch?v=CGIhxIaOg3M&lc)

### LLM-020

What is temperature in the context of LLMs, and how does it affect output?

- Answer: [What is temperature in the context of LLMs?](https://x.com/amitiitbhu/status/1964990603927687493)

### LLM-021

Why is the first token slower than the rest in an LLM?

- Answer: [The First-Token Latency Problem in LLMs](https://www.youtube.com/watch?v=XD8DD4cEHu0)

### LLM-022

Explain Top-p (nucleus) sampling and Top-k sampling. How do they differ?

- Supporting material: not linked in the source bank.

### LLM-023

What are logits, and how are they used in text generation?

- Answer: [Understanding Logits in Machine Learning](https://x.com/amitiitbhu/status/1927927814923207146)

### LLM-024

What are skip connections (residual connections) in Transformers?

- Answer: [Skip connections (residual connections) in Transformers](https://www.linkedin.com/posts/amit-shekhar-iitbhu_machinelearning-llm-deeplearning-share-7414239846707392512-pQdQ)

### LLM-025

What is the difference between open-source and closed-source LLMs? When would you choose one over the other?

- Supporting material: not linked in the source bank.

### LLM-026

What is the difference between encoder-only, decoder-only, and encoder-decoder Transformer architectures?

- Answer: [Encoder vs Decoder in Transformers](https://outcomeschool.com/blog/encoder-vs-decoder-in-transformers)

### LLM-027

What is KV cache, and how does it speed up inference?

- Answer: [What is KV Cache in LLMs?](https://outcomeschool.com/blog/kv-cache-in-llms)

### LLM-028

What is model distillation, and how is it used with LLMs?

- Answer: [How does Knowledge Distillation work?](https://outcomeschool.com/blog/how-does-knowledge-distillation-work)

### LLM-029

What is Mixture of Experts (MoE), and how does it work in models like Mixtral?

- Answer: [Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts)

### LLM-030

What is the difference between dense and sparse models?

- Answer: [Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts)

### LLM-031

What is Flash Attention?

- Answer: [Decoding Flash Attention in LLMs](https://outcomeschool.com/blog/decoding-flash-attention)

### LLM-032

What is Cross-Entropy Loss?

- Answer: [Math Behind Cross-Entropy Loss](https://outcomeschool.com/blog/math-behind-cross-entropy-loss)

### LLM-033

What is Grouped-Query Attention (GQA), and how does it differ from Multi-Head Attention (MHA)?

- Answer: [Grouped Query Attention](https://outcomeschool.com/blog/grouped-query-attention)

### LLM-034

How does Rotary Position Embedding (RoPE) work, and why is it preferred over learned positional embeddings?

- Answer: [Math Behind RoPE (Rotary Position Embedding)](https://outcomeschool.com/blog/math-behind-rope-rotary-position-embedding)

### LLM-035

Explain Layer Normalization

- Answer: [Batch Normalization vs Layer Normalization](https://outcomeschool.com/blog/batch-normalization-vs-layer-normalization)

### LLM-036

Explain RMSNorm (Root Mean Square Layer Normalization)

- Answer: [RMSNorm (Root Mean Square Layer Normalization)](https://outcomeschool.com/blog/rmsnorm-root-mean-square-layer-normalization)

### LLM-037

Your LLM keeps ignoring your instructions. How do you make it follow structured output formats?

- Supporting material: not linked in the source bank.

### LLM-038

Your LLM-powered tool hits the context window limit on long documents. How do you handle it?

- Supporting material: not linked in the source bank.

### LLM-039

Your LLM does not admit when it does not know the answer. How do you make it say "I don't know"?

- Supporting material: not linked in the source bank.

### LLM-040

Your LLM generates responses that are too verbose. How do you control response length?

- Supporting material: not linked in the source bank.

### LLM-041

Your LLM memorized proprietary training data and leaks it in responses. How do you prevent this?

- Supporting material: not linked in the source bank.

### LLM-042

Your LLM coding assistant generates outdated code using deprecated libraries. How do you fix it?

- Supporting material: not linked in the source bank.

### LLM-043

Your tokenizer splits important domain terms into meaningless subword pieces. How do you fix it?

- Supporting material: not linked in the source bank.

### LLM-044

Your Transformer's KV cache grows too large during long sequence generation. How do you manage memory?

- Answer: [Paged Attention in LLMs](https://outcomeschool.com/blog/paged-attention-in-llms)

### LLM-045

Your Transformer runs out of memory on long documents due to quadratic self-attention. How do you scale it?

- Supporting material: not linked in the source bank.

### LLM-046

Your distilled student model fails on the complex reasoning that the teacher model handled. How do you close the gap?

- Supporting material: not linked in the source bank.

### LLM-047

After RLHF alignment, your LLM became safer but lost capability on hard tasks. How do you manage the alignment tax?

- Supporting material: not linked in the source bank.

### LLM-048

Your RLHF-trained LLM is gaming the reward model instead of being genuinely helpful. How do you fix reward hacking?

- Answer: [Reinforcement Learning from Human Feedback (RLHF)](https://outcomeschool.com/blog/reinforcement-learning-from-human-feedback-rlhf)

### LLM-049

Your chatbot loses context after 10 turns in a conversation. How do you maintain a long conversation context?

- Answer: [AI Agent Memory](https://outcomeschool.com/blog/ai-agent-memory)

### LLM-050

Your chatbot fails when users switch topics mid-conversation. How do you handle topic switches?

- Supporting material: not linked in the source bank.

### LLM-051

Your QA system always generates an answer even when no answer exists in the context. How do you detect unanswerable questions?

- Supporting material: not linked in the source bank.

### LLM-052

Your summarization system hallucinated facts not in the original article. How do you fix it?

- Supporting material: not linked in the source bank.

### LLM-053

Your text generation repeats phrases in long outputs. How do you fix repetition?

- Supporting material: not linked in the source bank.

### LLM-054

Transformers work on text, so can they also understand images?

- Answer: [Decoding Vision Transformer (ViT)](https://outcomeschool.com/blog/decoding-vision-transformer-vit)

### LLM-055

Small Language Models (SLMs)

- Answer: [Small Language Models (SLMs)](https://outcomeschool.com/blog/small-language-models-slms)

### LLM-056

Large Reasoning Models (LRMs)

- Answer: [Large Reasoning Models (LRMs)](https://outcomeschool.com/blog/large-reasoning-models)

### LLM-057

What are Autoregressive Models?

- Answer: [Autoregressive Models](https://outcomeschool.com/blog/autoregressive-models)

### LLM-058

Explain the difference between autoregressive and masked language modeling.

- Supporting material: not linked in the source bank.

### LLM-059

Proximal Policy Optimization (PPO)

- Answer: [Proximal Policy Optimization (PPO)](https://outcomeschool.com/blog/proximal-policy-optimization-ppo)

### LLM-060

Direct Preference Optimization (DPO)

- Answer: [Direct Preference Optimization (DPO)](https://outcomeschool.com/blog/direct-preference-optimization-dpo)

### LLM-061

Group Relative Policy Optimization (GRPO)

- Answer: [Group Relative Policy Optimization (GRPO)](https://outcomeschool.com/blog/group-relative-policy-optimization-grpo)

### LLM-062

Recursive Language Models (RLMs)

- Answer: [Recursive Language Models (RLMs)](https://outcomeschool.com/blog/recursive-language-models)

### LLM-063

Continual Learning in LLMs

- Answer: [Continual Learning in LLMs](https://outcomeschool.com/blog/continual-learning-in-llms)

### LLM-064

How do Diffusion Language Models (DLMs) work?

- Answer: [How do Diffusion Language Models (DLMs) work?](https://outcomeschool.com/blog/how-do-diffusion-language-models-dlms-work)

### LLM-065

How Does LLM Watermarking Work?

- Answer: [How Does LLM Watermarking Work?](https://outcomeschool.com/blog/how-does-llm-watermarking-work)

### LLM-066

How do RNNs and Transformers differ?

- Answer: [How do RNNs and Transformers differ?](https://outcomeschool.com/blog/how-do-rnns-and-transformers-differ)
