# Website Testing Tools
# 网站测试工具

This directory contains automated testing and inspection tools for the Bowen Education Group website.

## Available Tools

### 1. Screenshot Website (`screenshot_website.py`)

Take automated screenshots of web pages using headless Chrome.

**Requirements:**
- Python 3.11+
- Selenium (`pip install selenium`)
- Chrome or Chromium browser
- Xvfb (for headless mode on Linux)

**Usage:**

```bash
# Activate virtual environment
source venv/bin/activate

# Set display for headless mode (Linux)
export DISPLAY=:99

# Basic usage
python tools/screenshot_website.py <url>

# With custom output file
python tools/screenshot_website.py <url> <output_file>
```

**Examples:**

```bash
# Screenshot homepage
python tools/screenshot_website.py http://192.168.31.205:8002

# Screenshot with custom filename
python tools/screenshot_website.py http://192.168.31.205:8002 homepage.png

# Screenshot different pages
python tools/screenshot_website.py http://192.168.31.205:8002/about about_page.png
python tools/screenshot_website.py http://192.168.31.205:8002/contact contact_page.png
```

**Features:**
- ✅ Headless Chrome screenshot
- ✅ Automatic overlay detection and closure
- ✅ Page statistics (navigation links, sections)
- ✅ 1920x1080 default resolution
- ✅ Error handling and reporting

**Output:**
```
📸 Taking screenshot of: http://192.168.31.205:8002
   Output: homepage.png
   Size: 1920x1080
   Title: Home - Bowen Education Group | Manchester Chinese School
   ✓ Closed search overlay

📊 Page Statistics:
   Navigation links: 9
   Sections: 6

✅ Screenshot saved successfully!
```

## Setup

### 1. Install Dependencies

```bash
# Install system packages (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y google-chrome-stable xvfb

# Or install Chromium
sudo apt-get install -y chromium-browser xvfb

# Install Python packages
pip install selenium
```

### 2. Start X Virtual Framebuffer (for headless mode)

```bash
# Start Xvfb on display :99
Xvfb :99 -screen 0 1920x1080x24 &

# Or use in a screen session
screen -S xvfb
Xvfb :99 -screen 0 1920x1080x24
# Press Ctrl+A then D to detach
```

### 3. Verify Setup

```bash
# Check if Xvfb is running
ps aux | grep Xvfb

# Test screenshot tool
source venv/bin/activate
export DISPLAY=:99
python tools/screenshot_website.py http://localhost:8002
```

## Integration with AI Agents

The screenshot tool is integrated with the `website_tester` agent. See `.claude/agents/website_tester.md` for details.

**Agent Usage:**
```markdown
You can use the screenshot tool by running:

source venv/bin/activate && export DISPLAY=:99 && python tools/screenshot_website.py <url> <output>

Then use the Read tool to view the generated screenshot.
```

## Troubleshooting

### Issue: "Could not find Google Chrome executable"

**Solution:**
```bash
# Install Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f -y
```

### Issue: "Missing X server"

**Solution:**
```bash
# Start Xvfb
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99
```

### Issue: "selenium module not found"

**Solution:**
```bash
source venv/bin/activate
pip install selenium
```

### Issue: Screenshot is all black

**Solution:**
- Wait longer for page to load (increase `time.sleep()` in script)
- Check if website is running and accessible
- Verify Xvfb is running correctly

## Best Practices

1. **Always use virtual environment**
   ```bash
   source venv/bin/activate
   ```

2. **Set DISPLAY before running**
   ```bash
   export DISPLAY=:99
   ```

3. **Use descriptive filenames**
   ```bash
   python tools/screenshot_website.py http://... homepage_before_fix.png
   python tools/screenshot_website.py http://... homepage_after_fix.png
   ```

4. **Take screenshots before and after changes**
   - Helps with visual comparison
   - Documents your work
   - Easy to spot regressions

5. **Keep screenshots organized**
   ```bash
   mkdir -p screenshots/homepage
   mkdir -p screenshots/about
   mkdir -p screenshots/contact
   ```

## Future Tools (Planned)

- [ ] Performance testing tool
- [ ] Accessibility checker
- [ ] SEO analyzer
- [ ] Link checker
- [ ] Form validation tester
- [ ] Mobile responsive tester
- [ ] Cross-browser screenshot comparison

## Contributing

To add new tools:

1. Create Python script in `tools/` directory
2. Make it executable: `chmod +x tools/your_tool.py`
3. Add documentation to this README
4. Update `.claude/agents/website_tester.md` if needed

## License

Copyright © 2025 Bowen Education Group. All rights reserved.
