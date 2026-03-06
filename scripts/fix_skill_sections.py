AKSHARE_APPEND = """

## Activation Keywords
- stock data
- 股票数据
- akshare
- 期货数据
- 基金数据
- 宏观经济
- 行情查询
- A股
- 港股
- 美股

## Tools Used
- exec: Run Python scripts using the akshare library to fetch financial data
- read: Read fetched data files and output results
- write: Save analysis results and fetched data to files

## Instructions for Agents

When a user asks for Chinese financial market data, use the AkShare Python library.

### Step 1: Identify Data Type
Determine which data category the user needs: stock, futures, fund, macro economics, etc.

### Step 2: Select Correct Function
Choose the appropriate AkShare function from the Data Categories section.

### Step 3: Execute Python Code
Run the AkShare function via exec tool to fetch the data.

### Step 4: Present Results
Format and present the data clearly as a table or summary.

## Examples

### Example 1: Fetch A-share Stock Data
```
User: "帮我查询000001平安银行最近30天的股价数据"

Agent:
1. Identify: A-share historical stock data
2. Use ak.stock_zh_a_hist() function
3. Execute Python script to fetch data
4. Present as a table

Agent: "以下是平安银行(000001)近30天的股价数据..."
```
"""

TEACH_APPEND = """

## Instructions for Agents
See **Instruction Flow** section above for detailed step-by-step guidance on how to teach users progressively, ask Socratic questions, and adapt to learning styles.

## Examples
See **Example Interactions** section above for complete conversation examples demonstrating Socratic questioning, progressive complexity, and adaptive teaching.
"""

base = "/Users/hiyenwong/projects/ai_projects/ai_collection/collection/skills"

# Fix akshare
akshare_path = f"{base}/akshare/SKILL.md"
with open(akshare_path, "r") as f:
    content = f.read()
# Strip any partial duplicates from previous failed attempts
if "## Activation Keywords" in content:
    content = content[: content.index("## Activation Keywords")].rstrip()
with open(akshare_path, "w") as f:
    f.write(content + "\n" + AKSHARE_APPEND)
print("akshare: done")

# Fix teach-cofounder
teach_path = f"{base}/teach-cofounder/SKILL.md"
with open(teach_path, "r") as f:
    content = f.read()
# Only add if sections are missing
if "## Instructions for Agents" not in content:
    content = content.rstrip() + "\n" + TEACH_APPEND
    with open(teach_path, "w") as f:
        f.write(content)
    print("teach-cofounder: done")
else:
    print("teach-cofounder: already has Instructions for Agents")
