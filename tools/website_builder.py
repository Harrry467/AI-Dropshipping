from langchain.tools import tool
import os
import subprocess
from jinja2 import Environment, FileSystemLoader
from config import STRIPE_SECRET_KEY

@tool
def create_and_deploy_product_page(product: dict) -> str:
    """
    Generates a static HTML landing page with a Stripe checkout button,
    deploys to a local folder (or Vercel via API). Returns the page URL.
    """
    # TODO: Replace mock URL with real deployment (e.g., Vercel API, Netlify)
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("landing_page.html")
    html_content = template.render(product=product, stripe_public_key="pk_test_XXX")
    
    output_dir = f"output/sites/{product['name'].replace(' ', '_').lower()}"
    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/index.html", "w") as f:
        f.write(html_content)
    
    # Mock URL – in reality, you'd upload to a hosting service
    page_url = f"https://yourdomain.com/{product['name'].replace(' ', '_').lower()}"
    return page_url
