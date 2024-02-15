# Multi-contextual learning through in-context pruning using Knowledge Graphs


An approach where a model is trained to adapt to various contexts, pruned for efficiency within each context, and enriched with domain-specific knowledge using a bio-medical knowledge graph. This could be particularly useful in applications where the operating conditions or requirements vary, and leveraging context-specific knowledge is essential for optimal performance.

The proposed solution is to implement "multicontextual learning through incontext pruning" by incorporating a biomedical knowledge graph, enabling the LLM to access and utilize detailed, domain-specific data for improved accuracy.

Retrieval-Augmented Generation (RAG) was recently introduced. This method involves enhancing a parametric pre-trained LLM with the ability to access a non-parametric memory containing updated knowledge about the world (for e.g., Wikipedia) 

Here we use Knowledge graph based RAG to provide domain-specific ground truth context at the prompt level. 

Uniqueness lies in improving the framework to build accurate biomedical prompts for LLM leveraging biomedical knowledge graphs.



