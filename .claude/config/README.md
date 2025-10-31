# Claude Code Configuration Files

This directory contains configuration files for the AI automated website generation workflow.

## Files

### `zhipu_api_key.txt`
Contains your Zhipu AI API key for image generation.

**Setup:**
1. Copy `zhipu_api_key.txt.example` to `zhipu_api_key.txt`
2. Replace the placeholder with your actual API key
3. Keep this file secure and never commit it to version control

**Getting an API Key:**
1. Visit [Zhipu AI Open Platform](https://open.bigmodel.cn/)
2. Sign up or log in to your account
3. Navigate to the API Keys section
4. Create a new API key
5. Copy and paste it into `zhipu_api_key.txt`

**Usage:**
The `/auto-website` workflow will automatically read this file when generating images.

## Security

**IMPORTANT**:
- The `zhipu_api_key.txt` file should be added to `.gitignore`
- Never share your API key publicly
- Never commit your API key to version control
- Regenerate your API key if it's accidentally exposed

## API Documentation

For more information about the Zhipu AI API:
- [Zhipu AI Documentation](https://open.bigmodel.cn/dev/api)
- [CogView-3 Image Generation API](https://open.bigmodel.cn/dev/api#cogview)

## Pricing

Zhipu AI CogView-3 pricing (as of 2025):
- ~¥0.10 per image
- Standard image size: 1024x1024
- Higher resolution may cost more

A typical website generation requires 15-20 images, costing approximately ¥1.50-¥2.00.

## Troubleshooting

**API Key Not Found:**
- Ensure `zhipu_api_key.txt` exists in `.claude/config/`
- Check that the file contains only the API key (no extra spaces or newlines)

**API Key Invalid:**
- Verify the key is copied correctly
- Check your account status on the Zhipu AI platform
- Ensure you have sufficient credits/quota

**Image Generation Fails:**
- Check your API quota/balance
- Verify network connectivity
- Review the error message for details
- Try a simpler prompt if the request is too complex
