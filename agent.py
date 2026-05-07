from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import Tool

from tools.product_researcher import find_winning_product
from tools.website_builder import create_and_deploy_product_page
from tools.video_creator import create_ai_video
from tools.social_poster import upload_to_social
from tools.dropshipper import setup_auto_fulfillment

from config import OPENAI_API_KEY

def create_agent():
    llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY, temperature=0.2)
    
    tools = [
        Tool.from_function(
            func=find_winning_product,
            name="FindProduct",
            description="Find a trending product for dropshipping. Input can be a category like 'kitchen gadgets'."
        ),
        Tool.from_function(
            func=create_and_deploy_product_page,
            name="CreateWebPage",
            description="Builds a product landing page and returns its URL. Input is the product dict."
        ),
        Tool.from_function(
            func=create_ai_video,
            name="MakeVideo",
            description="Creates a short promo video for the product. Input is the product dict. Returns video file path."
        ),
        Tool.from_function(
            func=upload_to_social,
            name="PostToSocial",
            description="Uploads a video to social platforms. Input must be a JSON with 'video_path', 'caption', and optional 'platforms' list."
        ),
        Tool.from_function(
            func=setup_auto_fulfillment,
            name="SetupFulfillment",
            description="Sets up automatic dropshipping for a product. Input: a dict with product info and a webhook URL."
        ),
    ]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an AI that automates a viral product business.
        Your goal: research a product, create a shop page, produce a video ad, post it to YouTube Shorts,
        and configure auto-dropshipping. Use the tools step by step. After finishing, output a summary."""),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    agent = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)
