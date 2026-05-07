from agent import create_agent

def run_pipeline():
    agent = create_agent()
    result = agent.invoke({
        "input": "Find a weird kitchen gadget, set up a store with auto-dropshipping, make a video, and post it to YouTube Shorts. Use a webhook at https://myapi.com/stripe-webhook for fulfillment."
    })
    print("\n===== AGENT OUTPUT =====")
    print(result["output"])

if __name__ == "__main__":
    run_pipeline()
