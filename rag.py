import os
import chromadb
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
llm=Groq(api_key=os.getenv("GROQ_API_KEY"))
text=open("resume.txt",encoding="UTF-8").read()
size=500
chunks=[text[i:i+size] for i in range(0,len(text),size)]
db=chromadb.Client()
col=db.get_or_create_collection("resume")
col.add(document=chunks,ids=[str(i)for i in range(len(chunks))])
question=input("question")
hits=col.query(query_texts=[question],n_results=3)["documents"][0]
prompt=("Answer only from the content below .If the answer is not there say 'I dont know.\n\n"
	"context:\n"+"\n---\n".join(hits)+"\n\nQuestions"+question
	)
reply=llm.chat.completion.create(
				model=os.getenv("GROQMODEL"),
				message=[{"role":"user","content":prompt}],
				)
print(reply.choices[0].messagecontent)

