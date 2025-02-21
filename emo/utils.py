import chromadb
from chromadb.utils import embedding_functions
import numpy as np
from json import load as jsonLoad


client = chromadb.EphemeralClient()

# 创建不自动生成嵌入的集合（重要！）
emo_vec_coll = client.get_or_create_collection(
    name="emo_vec",
    embedding_function=None,  # 禁用自动嵌入生成
    metadata={"hnsw:space": "cosine"},
)
def insertVecs(vecs,metadatas,ids):
    emo_vec_coll.add(
    embeddings=vecs,  # 必须二维列表
    metadatas=metadatas,
    ids=ids
    )

def readEmoConfig():
    EmoConfig = None
    with open("EmoConfig.json","r",encoding="utf8") as f:
        EmoConfig = jsonLoad(f)
    vecs = [i["emo_vector"] for i in EmoConfig]
    metadatas = []
    for d in EmoConfig:
        d.pop('emo_vector',None)
        metadatas.append(d)
    ids = [f'init_{i}' for i in range(len(EmoConfig))]
    insertVecs(vecs,metadatas,ids)
    return

def queryVecs(vec , top_k = 1):
    results = emo_vec_coll.query(
    query_embeddings=[vec],
    n_results=top_k,
    include=["embeddings", "metadatas", "distances"]
    )
    return results








