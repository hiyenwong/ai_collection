#!/bin/bash
# Install agent-bootstrap

set -e

echo "🚀 Installing agent-bootstrap..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install in development mode
pip install -e .

# Make executable
chmod +x agent_bootstrap.py

# Create symlink
ln -sf "$(pwd)/agent_bootstrap.py" /usr/local/bin/agent-bootstrap 2>/dev/null || echo "Note: Could not create symlink. Use: source venv/bin/activate && agent-bootstrap"

echo ""
echo "✅ Installation complete!"
echo ""
echo "Usage:"
echo "  source venv/bin/activate"
echo "  agent-bootstrap init"
echo ""
echo "Or run directly:"
echo "  python agent_bootstrap.py init"
echo ""