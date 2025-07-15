from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def generate_persona(user_data, api_key):
    comments_text = "\n".join([f"ID: {c['id']}\nPermalink: https://reddit.com{c['permalink']}\nBody: {c['body'][:200]}\n" for c in user_data['comments']])
    posts_text = "\n".join([f"ID: {p['id']}\nPermalink: https://reddit.com{p['permalink']}\nTitle: {p['title']}\nSelftext: {p['selftext'][:500]}\n" for p in user_data['posts']])

    llm = ChatGroq(
        model="llama3-8b-8192",
        api_key=api_key,
        temperature=0.2,
    )

    system_prompt = ("""
        You are a professional UX researcher creating a user persona based on Reddit activity. 

        Create a detailed persona following this structure:
        - Name: [Create a fictional name]
        - Age: [Estimate or mark as "Unknown"]
        - Occupation: [Infer from posts/comments or mark as "Unknown"]
        - Status: [Relationship status if mentioned]
        - Location: [If mentioned or "Unknown"]

        BEHAVIOR & HABITS:
        - List 3-5 key behaviors observed

        MOTIVATIONS:
        - List primary motivations and interests

        FRUSTRATIONS:
        - List main pain points and complaints

        GOALS & NEEDS:
        - List what they're trying to achieve

        PERSONALITY:
        - Describe personality traits

        For EACH characteristic mentioned, you MUST provide a citation in this format:
        [Citation: Item ID, Subreddit Name, Post/Comment Title or Body Snippet]

        Be honest about uncertainty. If something isn't clear from the data, say so.
        Format as a clean, readable text document suitable for saving as a .txt file.
        """)

    human_prompt = (
        "Analyze the following Reddit comments and posts to create a user persona. "
        "Include citations for each characteristic. \n\n"
        "Comments:\n{comments}\n\n"
        "Posts:\n{posts}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", human_prompt)
    ])

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"comments": comments_text, "posts": posts_text})
    return response
