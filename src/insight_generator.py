import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0
)


def generate_insights(text):

    prompt = f"""
Analyze this research paper.

Extract only:
- Abstract
- Methodology
- Findings
- Conclusion

Use only information present in the paper.
Do not invent information.

Return ONLY a JSON object.
Use double quotes for all keys and values.

Example:
{{
    "Abstract": "text",
    "Methodology": "text",
    "Findings": "text",
    "Conclusion": "text"
}}

Research Paper:
{text}
"""

    response = llm.invoke(prompt)

    result = response.content

    if isinstance(result, list):
        result = "".join(
            item.get("text", "") if isinstance(item, dict)
            else str(item)
            for item in result
        )

    result = str(result)

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    try:
        return json.loads(result)

    except json.JSONDecodeError:
        raise ValueError(
            "Gemini did not return valid JSON."
        )