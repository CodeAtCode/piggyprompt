openai_models = [
    "o4-mini",
    "o3",
    "o3-mini",
    "o1",
    "o1-pro",
    "o1-mini",
    "gpt-4.1",
    "gpt-4o",
    "gpt-4o-audio",
    "chatgpt-4o",
    "gpt-4.1-mini",
    "gpt-4.1-nano",
    "gpt-4o-mini",
    "gpt-4o-mini-audio",
    "o3-mini",
    "o1-mini",
    "gpt-4o-realtime",
    "gpt-4o-mini-realtime",
    "gpt-image-1",
    "dall-e-3",
    "dall-e-2",
    "gpt-4o-mini-tts",
    "tts-1",
    "tts-1-hd",
    "gpt-4-turbo",
    "gpt-4",
    "gpt-3.5-turbo"
]

anthropic_models = [
    "claude-opus-4",
    "claude-sonnet-4",
    "claude-3-7-sonnet",
    "claude-3-5-haiku",
    "claude-3-5-sonnet",
    "claude-3-opus",
    "claude-3-sonnet",
    "claude-3-haiku"
]

google_models = [
    "gemini-2.5-pro",
    "gemini-2.5-flash",
    "gemini-2.5-flash-native-audio",
    "gemini-2.5-pro-native-audio",
    "gemma-3n",
    "medgemma",
    "signgemma",
    "dolphingemma",
    "imagen-4",
    "veo-3",
    "flow"
]

meta_models = [
    "llama-4o-70b-groq",
    "llama-4o-70b-cerebras",
    "llama-4o-70b-chat",
    "llama-4o-70b",
    "llama-4-70b-chat",
    "llama-4-70b",
    "llama-3-5-70b-chat",
    "llama-3-5-70b",
    "llama-3-3-70b-chat",
    "llama-3-3-70b",
    "llama-3-3-8b",
    "llama-3-2-90b-vision-chat",
    "llama-3-2-90b-vision",
    "llama-3-2-11b-vision-chat",
    "llama-3-2-11b-vision",
    "llama-3-2-3b-chat",
    "llama-3-2-3b",
    "llama-3-2-1b-chat",
    "llama-3-2-1b",
    "llama-3-1-405b-chat",
    "llama-3-1-405b",
    "llama-3-1-70b-chat",
    "llama-3-1-70b",
    "llama-3-1-8b-chat",
    "llama-3-1-8b"
]

deepseek_models = [
    "DeepSeek-R1-Llama-70BLLMR1LlamaTRT-LLMH100",
    "DeepSeek-R1-Qwen-32BLLMR1QwenTRT-LLMH100",
    "DeepSeek-R1-LLMR1SGLangH200",
    "DeepSeek-R1-Qwen-7BLLMR1QwenTRT-LLMH100-MIG-40GB",
    "DeepSeek-R1-ZeroLLMR1ZeroSGLangH200",
    "DeepSeek-V3-LLMV3SGLangH200",
    "DeepSeek-LLM-7B",
    "DeepSeek-LLM-67B",
    "DeepSeek-LLM-7B-Chat",
    "DeepSeek-LLM-67B-Chat",
    "DeepSeek-Coder-Base-v1.5-7B",
    "DeepSeek-Coder-V2-236B",
    "DeepSeek-V2-MoE-236B",
    "DeepSeek-V2.5-MoE",
    "DeepSeek-V3-MoE-671B",
    "DeepSeek-Math",
    "DeepSeek-Prover-V1",
    "DeepSeek-Prover-V1.5",
    "JanusFlow",
    "Janus-Pro",
    "JanusPro-7B",
    "DeepSeek-VL",
    "DeepSeek-VL2-Tiny",
    "DeepSeek-VL2-Small",
    "DeepSeek-VL2"
]

alibaba_models = [
    "QwQ-32B-Preview",
    "Qwen-Max",
    "Qwen-Plus",
    "Qwen-Turbo",
    "Qwen-3",
    "Qwen-2.5-Dense",
    "Qwen-2.5-Sparse",
    "Qwen-2.5-VL-3B",
    "Qwen-2.5-VL-7B",
    "Qwen-2.5-VL-32B",
    "Qwen-2.5-VL-72B",
    "Qwen-2.5-VL-32B-Instruct",
    "Qwen-2.5-Omni-7B",
    "Qwen-2-Dense",
    "Qwen-2-Sparse",
    "Qwen-2-VL-2B",
    "Qwen-2-VL-7B",
    "Qwen-1.5",
    "Qwen2-VL-2B",
    "Qwen2-VL-7B",
    "Qwen2-Math"
]

mistral_models = [
    "Mistral Large",
    "Mistral Medium",
    "Mistral Small",
    "Mistral Small v3.1",
    "Mistral 7B",
    "Mixtral 8x7B",
    "Mixtral 8x22B",
    "Codestral",
    "Codestral Mamba",
    "Mistral Moderation",
    "Mistral Saba",
    "Pixtral",
    "Pixtral Large",
    "NeMo",
    "Mathstral 7B",
    "Devstral Small",
    "Mistral OCR"
]

xai_models = [
    "grok-2",
    "grok-2-latest",
    "grok-2.5",
    "grok-3-fast",
    "grok-3-standard"
]


def get_models(provider):
    if provider == "OpenAI":
        return openai_models
    elif provider == "Anthropic":
        return anthropic_models
    elif provider == "Google":
        return google_models
    elif provider == "Meta":
        return meta_models
    elif provider == "DeepSeek":
        return deepseek_models
    elif provider == "Alibaba":
        return alibaba_models
    elif provider == "Mistral":
        return mistral_models
    elif provider == "xAI":
        return xai_models
    elif provider == "Other":
        return []
    return []