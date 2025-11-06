# Website Tools and Agent Guide
# 网站工具和代理指南

## 📁 Project Structure

```
bowen-education-manchester/
├── tools/                      # Testing and automation tools
│   ├── screenshot_website.py   # Website screenshot tool
│   └── README.md               # Tools documentation
├── .claude/
│   └── agents/
│       └── website_tester.md   # Website testing agent configuration
├── templates/                  # Jinja2 templates
├── static/                     # Static files (CSS, JS, images)
├── app/                        # FastAPI application
└── venv/                       # Python virtual environment
```

## 🛠️ Available Tools

### 1. Screenshot Tool

**Location:** `tools/screenshot_website.py`

**Purpose:** Automated website screenshots for visual testing and documentation

**Quick Start:**
```bash
source venv/bin/activate
export DISPLAY=:99
python tools/screenshot_website.py http://192.168.31.205:8002 homepage.png
```

**Features:**
- ✅ Headless Chrome screenshots
- ✅ Automatic overlay detection/closure
- ✅ Page statistics reporting
- ✅ Custom resolution support
- ✅ Error handling

**When to Use:**
- After CSS/HTML changes
- Before/after comparisons
- Bug investigation
- Documentation
- Visual regression testing

## 🤖 AI Agents

### Website Tester Agent

**Location:** `.claude/agents/website_tester.md`

**Purpose:** Specialized agent for comprehensive website testing

**Capabilities:**
1. Visual inspection via screenshots
2. Functional testing
3. Performance checking
4. Issue reporting
5. Before/after comparisons

**How to Use:**

The agent is automatically available when working in this project. It knows how to:
- Use the screenshot tool
- Analyze screenshots
- Identify visual issues
- Suggest fixes
- Document problems

**Example Workflow:**
```markdown
User: "Please test the homepage navigation"

Agent will:
1. Take screenshot of homepage
2. Analyze navigation layout
3. Check for CSS issues
4. Test dropdown menus
5. Verify responsive design
6. Report findings
```

## 📋 Common Tasks

### Task 1: Visual Testing After Changes

```bash
# 1. Take "before" screenshot
python tools/screenshot_website.py http://192.168.31.205:8002 before.png

# 2. Make your changes (edit CSS, HTML, etc.)

# 3. Take "after" screenshot
python tools/screenshot_website.py http://192.168.31.205:8002 after.png

# 4. Compare using Read tool or image viewer
```

### Task 2: Full Site Screenshot Audit

```bash
#!/bin/bash
# Save as: tools/screenshot_all_pages.sh

source venv/bin/activate
export DISPLAY=:99

mkdir -p screenshots

pages=(
  "http://192.168.31.205:8002:homepage"
  "http://192.168.31.205:8002/about:about"
  "http://192.168.31.205:8002/contact:contact"
)

for page in "${pages[@]}"; do
  url="${page%%:*}"
  name="${page##*:}"
  python tools/screenshot_website.py "$url" "screenshots/${name}.png"
done

echo "All screenshots saved to screenshots/"
```

### Task 3: Testing Specific Components

```bash
# Test navigation
python tools/screenshot_website.py http://192.168.31.205:8002 nav_test.png

# Then use Chrome DevTools to inspect:
# - Check if nav-menu is display: flex
# - Verify dropdown-menu has display: none
# - Confirm nav-link styling is correct
```

## 🎯 Agent Integration Examples

### Example 1: Ask Agent to Check Header

```markdown
User: "Please check if the header navigation is displaying correctly"

Agent Response:
I'll take a screenshot and analyze the header...

[Uses screenshot tool]
[Analyzes image with Read tool]
[Reports findings]:

✅ Header displays correctly:
- Logo: visible and properly sized
- Navigation: horizontal layout
- Dropdown menus: hidden by default
- Book Now button: visible on desktop

Issues found:
None - header is working perfectly!
```

### Example 2: Ask Agent to Fix Styling Issue

```markdown
User: "The hero section looks too dark"

Agent Response:
Let me investigate...

[Takes screenshot]
[Analyzes CSS]
[Identifies issue in hero overlay opacity]
[Suggests fix]
[Makes fix with Edit tool]
[Takes new screenshot]
[Confirms fix]

✅ Fixed: Reduced hero overlay opacity from 0.7 to 0.4
See before/after screenshots for comparison.
```

## 🔧 Prerequisites

### System Requirements

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y \
    google-chrome-stable \
    xvfb \
    python3.11 \
    python3.11-venv

# Verify installation
google-chrome --version
which xvfb-run
python3.11 --version
```

### Python Environment

```bash
# Create virtual environment (if not exists)
python3.11 -m venv venv

# Activate
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install selenium  # If not already in requirements.txt
```

### Start Services

```bash
# 1. Start Xvfb (X virtual framebuffer)
Xvfb :99 -screen 0 1920x1080x24 &

# 2. Start web server
source venv/bin/activate
uvicorn app.main:app --host 192.168.31.205 --port 8002 --reload

# 3. Verify both are running
ps aux | grep Xvfb
curl http://192.168.31.205:8002
```

## 📖 Documentation

- **Tools Documentation:** `tools/README.md`
- **Agent Documentation:** `.claude/agents/website_tester.md`
- **Project README:** `README.md`
- **Test Reports:** `WEBSITE_TEST_REPORT.md`

## 🎓 Best Practices

### 1. Always Use Virtual Environment

```bash
# ✅ Good
source venv/bin/activate
python tools/screenshot_website.py ...

# ❌ Bad
python tools/screenshot_website.py ...
```

### 2. Set DISPLAY Environment Variable

```bash
# ✅ Good
export DISPLAY=:99
python tools/screenshot_website.py ...

# ❌ Bad (on Linux)
python tools/screenshot_website.py ...  # Will fail
```

### 3. Use Descriptive Filenames

```bash
# ✅ Good
homepage_before_header_fix.png
homepage_after_header_fix.png
navigation_issue_2025-11-05.png

# ❌ Bad
screenshot.png
test.png
1.png
```

### 4. Organize Screenshots

```bash
# Create organized structure
mkdir -p screenshots/{before,after,issues,documentation}

# Save to organized locations
python tools/screenshot_website.py ... screenshots/before/homepage.png
python tools/screenshot_website.py ... screenshots/after/homepage.png
```

## 🐛 Troubleshooting

### Problem: "selenium module not found"
```bash
source venv/bin/activate
pip install selenium
```

### Problem: "Chrome not found"
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f -y
```

### Problem: "Display :99 not found"
```bash
# Start Xvfb
Xvfb :99 -screen 0 1920x1080x24 &

# Verify it's running
ps aux | grep Xvfb
export DISPLAY=:99
```

### Problem: "Screenshot is black/empty"
```bash
# 1. Check if website is running
curl http://192.168.31.205:8002

# 2. Increase wait time in script (edit tools/screenshot_website.py)
time.sleep(3)  # Change to time.sleep(5)

# 3. Check for overlays blocking content
# The tool auto-closes search overlay and mobile menu
```

## 📞 Support

For issues or questions:
1. Check `tools/README.md` for detailed tool documentation
2. Review `.claude/agents/website_tester.md` for agent capabilities
3. Check error messages carefully
4. Verify all prerequisites are installed

## 🚀 Future Enhancements

Planned tools:
- [ ] Performance testing tool
- [ ] Accessibility checker (WCAG 2.1)
- [ ] SEO analyzer
- [ ] Mobile responsive tester
- [ ] Cross-browser screenshot tool
- [ ] Automated link checker
- [ ] Form validation tester

---

**Last Updated:** 2025-11-05
**Version:** 1.0.0
**Maintainer:** AI Development Team
