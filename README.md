# AI_Engineer_102
A Python application that uses multiple AI agents to collaboratively develop product briefs. This system simulates a product development team with specialized roles working together to create comprehensive MVP (Minimum Viable Product) documentation.

## What This Application Does

This application creates an AI-powered product development workflow that includes:
- **UX Researcher**: Analyzes user needs and pain points
- **Product Architect**: Designs technical architecture and implementation plans
- **Quality Analyst**: Reviews for compliance, safety, and testing requirements
- **Product Manager**: Orchestrates the team and synthesizes insights
- **Product Writer**: Creates the final deliverable document

## Prerequisites

Before you start, make sure you have:

1. **Python 3.8 or higher** installed on your computer
2. **OpenAI API key** (you'll need to sign up at https://openai.com)
3. **Ollama installed** (for local AI model - download from https://ollama.ai)
4. Basic familiarity with command line/terminal

## Step-by-Step Setup Guide

### Step 1: Clone or Download the Project

If you have this code, make sure you're in the project directory where you can see the `product_dev.py` file.

### Step 2: Create a Virtual Environment (Recommended)

A virtual environment keeps your project dependencies separate from other Python projects.

```bash
# Create virtual environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Activate it (Mac/Linux)
source .venv/bin/activate
```

### Step 3: Install Required Packages

Install all the necessary Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- `autogen` - The main AI agent framework
- `autogen-agentchat` - Chat functionality for agents
- `autogen-ext[openai,ollama]` - Extensions for OpenAI and Ollama models
- `python-dotenv` - For managing environment variables

### Step 4: Set Up Ollama (Local AI Model)

1. Download and install Ollama from https://ollama.ai
2. Once installed, download the required model:
   ```bash
   ollama pull llama3.2:3b
   ```
3. Start Ollama (it usually starts automatically, but you can run `ollama serve` if needed)

### Step 5: Configure Environment Variables

Create a `.env` file in your project directory with your API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
OLLAMA_BASE_URL=http://localhost:11434/v1
```

**To get your OpenAI API key:**
1. Go to https://platform.openai.com
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste it into your `.env` file

### Step 6: Run the Application

Now you're ready to run the product development workflow:

```bash
python product_dev.py
```

## How It Works

### The Workflow Process

1. **Input**: You provide a product idea or requirement
2. **Team Collaboration**: The AI agents work in sequence:
   - UX Researcher analyzes user needs
   - Product Architect designs the technical solution
   - Quality Analyst reviews for compliance and testing
3. **Synthesis**: Product Manager coordinates the insights
4. **Documentation**: Product Writer creates the final MVP brief

### Current Example

The application is currently configured to create an MVP brief for "burnout monitoring software" that:
- Tracks employee well-being signals
- Provides anonymized dashboards for managers
- Offers early warning indicators
- Suggests preventive actions
- Ensures privacy compliance

## Customizing for Your Own Product Ideas

To use this for your own product development:

1. Open `product_dev.py`
2. Find the `task` variable near the bottom
3. Replace the current description with your product idea
4. Run the application again

Example:
```python
task = (
    "INPUT: Create a one-page MVP brief for a [YOUR PRODUCT IDEA HERE]. "
    "[Add your specific requirements and constraints]"
)
```

## Understanding the Output

The application will generate a comprehensive product brief including:
- **Problem Statement**: What problem you're solving
- **Target Users**: Who will use your product
- **Proposed Solution**: How your product works
- **System Architecture**: Technical implementation overview
- **MVP Scope**: What to build first
- **Acceptance Criteria**: How to test success
- **Risks & Next Steps**: Potential challenges and recommendations

## Troubleshooting

### Common Issues

**"OpenAI API key not found"**
- Make sure your `.env` file is in the same directory as `product_dev.py`
- Check that your API key is correct and has credits

**"Connection to Ollama failed"**
- Make sure Ollama is running (`ollama serve`)
- Verify the model is downloaded (`ollama pull llama3.2:3b`)
- Check that the base URL in `.env` is correct

**"Module not found" errors**
- Make sure your virtual environment is activated
- Run `pip install -r requirements.txt` again

### Getting Help

If you encounter issues:
1. Check that all prerequisites are installed
2. Verify your `.env` file configuration
3. Make sure your virtual environment is activated
4. Try running each step again from the beginning

## Next Steps

Once you have the basic setup working:
- Experiment with different product ideas
- Modify the agent roles and responsibilities
- Adjust the system messages to change how agents behave
- Add more agents or change the workflow structure

## Cost Considerations

- OpenAI API calls cost money (usually a few cents per run)
- Ollama runs locally and is free
- Monitor your OpenAI usage at https://platform.openai.com/usage
